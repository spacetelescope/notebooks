import sys
import argparse
from astropy.table import unique, vstack
from astroquery.mast import Observations

def download_by_jwst_pid (pid, curl_flag):
    """
    This function retrieves all of the level 2 science products for a single program ID.
    Inputs:
    pid [int] – program ID number
    curl_flag [Boolean] – If set to true, function returns a curl script.
    """

    # Login, search for observations (token from https://auth.mast.stsci.edu/tokens)
    # If accessing public data, you can commment out the line below:
    Observations.login(store_token=True)
    obs_list = Observations.query_criteria(obs_collection='JWST', proposal_id=pid)

    # Give each observation one at time and find associated products
    data_products = [Observations.get_product_list(obs) for obs in obs_list]
    unq_products = unique(vstack(data_products), keys='productFilename')

    # Filter for desired products
    filtered_prod = Observations.filter_products(unq_products, calib_level=[2],
                                                 productType='SCIENCE')
    # Filesize check
    total = sum(filtered_prod['size'])
    # Use curl for large downloads.
    if total/10**9 > 1 and curl_flag is False:
        curl_flag = True
        print("\nDownload too large. Switching to curl script.")
    # User must confirm download size
    prompt = f"Total download size is: {total/10**9} GB. Proceed? (y/n) "
    resp = input(prompt)
    if resp != 'y':
        sys.exit()

    # Check for curl flag
    if curl_flag:
        Observations.download_products(filtered_prod, curl_flag=True)
    else:
        Observations.download_products(filtered_prod)

def setup_args():
    '''
    Define arguments, set up --help
    '''
    parser = (argparse.ArgumentParser(description =
    'This function retrieves all of the level 2 science products for a single program ID.'))
    parser.add_argument('pid', help='[int] Program ID Number')
    parser.add_argument('curl_flag', help='[Boolean] If true, download via curl script')
    return parser.parse_args()

args = setup_args()
download_by_jwst_pid(args.pid, args.curl_flag)
