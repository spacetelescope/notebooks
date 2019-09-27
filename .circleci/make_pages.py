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

args = make_parser().parse_args()
logger.info('Converting notebooks into HTML')
converted = run_parsed('.', output_type='HTML', args=args)
# converted = [item for item in converted if not os.path.basename(item) in ['test-fail.html', 'test-succeed.html']]

logger.info('Creating HTML Index')
make_html_index(converted, './index.tpl')
