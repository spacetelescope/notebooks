#!/usr/bin/env python3

import os
import logging

from nbpages import make_parser, run_parsed, make_html_index

args = make_parser().parse_args()
if args.template_file is None and os.path.exists('nb_html.tpl'):
    args.template_file = 'nb_html.tpl'

if args.exclude is None:
    # If there is an "exclude_notebooks" file, use that to find which ones to
    # skip.  Format is one pattern per line, "#" for comments.
    # note that this will be ignored if exclude is given at the command line.
    to_exclude = []
    if os.path.isfile('exclude_notebooks'):
        with open('exclude_notebooks') as f:
            for line in f:
                if line.strip() != '':
                    to_exclude.append(line.split('#')[0].strip())

    if to_exclude:
        args.exclude = ','.join(to_exclude)

converted = run_parsed('.', output_type='HTML', args=args)

logging.getLogger('nbpages').info('Generating index.html')
make_html_index(converted, './index.tpl')
