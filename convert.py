#!/usr/bin/env python3

import os
import logging
import subprocess

from nbpages import make_parser, run_parsed, make_html_index

args = make_parser().parse_args()
if args.template_file is None and os.path.exists('nb_html.tpl'):
    args.template_file = 'nb_html.tpl'

if args.changed:
    # If changed option is set, only convert notebooks that where changed.
    # This command will list all changed files on current commit from master.
    list_changed_files_cmd = "git show --pretty=format: --name-only -r master"

    # Get list of changed files using git
    # git must be installed and accessible from the calling shell
    changed_files = subprocess.check_output(list_changed_files_cmd,
                                                shell=True).decode()
    # Only get changed noteobook files, strip path from their name
    to_include = [os.path.split(x)[1].replace('.ipynb', '')
            for x in changed_files.strip().split('\n') if ".ipynb" in x]

    if to_include:
        args.include = ",".join(to_include)

if args.exclude is None and args.changed is None:
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
