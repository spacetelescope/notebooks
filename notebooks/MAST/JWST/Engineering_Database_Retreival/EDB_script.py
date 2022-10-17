"""
This script takes a csv file containing one mnemonic, start time,
and end time per line. It will return the associated engineering data, and
includes an example file if no data is specified.
"""

import argparse
import csv
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

# default file to use if no file specified
DEFAULT_FILE = "SA_ZADUCMDX-20220601T000000-20220601T060000.csv"


def download_edb_datafiles(filenames, folder, prefix=""):
    """Download filenames to directory"""
    Path(folder).mkdir(exist_ok=True)

    status = 0
    for fname in filenames:
        print(
            f"Downloading File: mast:jwstedb/{fname}\n",
            f" To: {folder}/{fname}",
        )
        url = f"https://mast.stsci.edu{prefix}/api/v0.1/Download/file?uri=mast:jwstedb/{fname}"
        try:
            urllib.request.urlretrieve(url, filename=f"{folder}/{fname}")
        except urllib.error.HTTPError:
            print("  ***Error downloading file***")
            status = 1

    return status


def _convert_datetime_to_compact_iso(dt):
    return dt.strftime("%Y%m%dT%H%M%S")


def parse_mnemonic_starttime_endtime(req):
    """Given a dictionary with mnemonic, starttime, and endtime construct the edb filename"""

    if "mnemonic" not in req or "starttime" not in req or "endtime" not in req:
        raise ValueError("Request data objects must have mnemonic, startime and endtime defined")
    starttime = _convert_datetime_to_compact_iso(req["starttime"])
    endtime = _convert_datetime_to_compact_iso(req["endtime"])
    mnemonic = req["mnemonic"]
    return f"{mnemonic}-{starttime}-{endtime}.csv"


def parse_edb_query(csvfile):
    """from a csvfile containing lines of mnemonic, starttime, and endtimes, return edb filenames"""
    filenames = []
    with open(csvfile, "r", encoding="utf-8-sig") as csvfh:
        query_reader = csv.reader(csvfh, delimiter=",", quoting=csv.QUOTE_NONE)
        for row in query_reader:
            req = {
                "mnemonic": row[0].strip(),
                "starttime": datetime.fromisoformat(row[1].strip()),
                "endtime": datetime.fromisoformat(row[2].strip()),
            }
            filenames.append(parse_mnemonic_starttime_endtime(req))
    return filenames


def download_edb_datafiles_by_mnemonic_starttime_endtime(requests, folder):
    """Download datafiles by mnemonic/starttime/endtime to directory

    Example

    ```python
    from datetime import datetime

    request = dict()
    request["mnemonic"] = "SA_ZADUCMDX"
    request["starttime"] = datetime(2016,1,22,17,28,18)
    request["endtime"] = datetime(2016,1,22,18,46,4)
    requests = list()
    requests.append(request)
    download_edb_datafiles_by_mnemonic_starttime_endtime(requests, "test")
    ```
    """

    filenames = []
    for req in requests:
        filename = parse_mnemonic_starttime_endtime(req)
        print(f"adding file: {filename}")
        filenames.append(filename)
    download_edb_datafiles(filenames, folder)


def parse_args(args):
    """Get command line arguments, use defaults if not specified """
    if args is None:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--folder", type=str, default="edb-data", help="Folder to download to"
    )
    parser.add_argument(
        "-p", "--prefix", type=str, default="", help="Prefix path to use (example: '/jwst')"
    )
    parser.add_argument(
        "-q",
        "--query",
        type=str,
        help="Query file (csv) containing a mnemonic, starttime, endtime per line",
    )
    parser.add_argument("file", nargs="*", type=str, help="File(s) to download")
    args = parser.parse_args(args)

    filenames = args.file
    if not filenames:
        filenames = []

    folder = args.folder
    prefix = args.prefix

    csvfile = args.query
    if csvfile:
        mnemonics = parse_edb_query(csvfile)
        filenames += mnemonics

    filenames = set(filenames)

    if not filenames:
        print(f"No files specified, using default file: {DEFAULT_FILE}")
        filenames = {DEFAULT_FILE}

    return filenames, folder, prefix


def main(args=None):
    """Collect args from user input, give them to the download function"""
    filenames, folder, prefix = parse_args(args)
    return download_edb_datafiles(filenames, folder, prefix)


if __name__ == "__main__":
    sys.exit(main())
