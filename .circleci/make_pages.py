#!/usr/bin/env python

import logging
import os
import sys

from nbpages import make_parser, run_parsed, make_html_index

root = logging.getLogger()
root.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
root.addHandler(handler)

logger = logging.getLogger(__file__)

def main():
    import sys; os
    repo_path = os.getcwd()
    logger.info(f'Added path[{repo_path}]')
    sys.path.append(repo_path)
    with open("convert.py") as f:
        exec(f.read())

if __name__ in ['__main__']:
    main()
