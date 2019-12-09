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
    import convert
    # args = make_parser().parse_args()
    # # Used for debugging the .circleci pipeline
    # # converted = [item for item in converted if not os.path.basename(item) in ['test-fail.html', 'test-succeed.html']]
    # to_exclude = []
    # if os.path.isfile('exclude_notebooks'):
    #     with open('exclude_notebooks') as f:
    #         for line in f:
    #             if line.strip() != '':
    #                 to_exclude.append(line.split('#')[0].strip())

    # if to_exclude:
    #     args.exclude = ','.join(to_exclude)
    # 
    # logger.info('Converting notebooks into HTML')
    # converted = run_parsed('.', output_type='HTML', args=args)
    # logger.info('Creating HTML Index')
    # make_html_index(converted, './index.tpl')

if __name__ in ['__main__']:
    main()

