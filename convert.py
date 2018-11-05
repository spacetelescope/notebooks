#!/usr/bin/env python3

import os
import logging

from nbpages import make_parser, run_parsed, make_html_index

args = make_parser().parse_args()
if args.template_file is None and os.path.exists('nb_html.tpl'):
    args.template_file = 'nb_html.tpl'
converted = run_parsed('.', output_type='HTML', args=args)

logging.getLogger('nbpages').info('Generating index.html')
make_html_index(converted, './index.tpl')
