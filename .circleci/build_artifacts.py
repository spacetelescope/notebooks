#!/usr/bin/env python

import logging
import json
import os
import subprocess
import shutil
import sys
import tarfile
import tempfile
import time
import types
import typing

from datetime import datetime

from junitparser import TestCase, TestSuite, JUnitXml, Skipped, Error

root = logging.getLogger()
root.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
root.addHandler(handler)

logger = logging.getLogger(__file__)

IPYDB_REQUIRED_FILES: typing.List[str] = ['requirements.txt']
ENCODING: str = 'utf-8'
ARTIFACT_DEST_DIR: str = '/tmp/artifacts'
TEST_OUTPUT_DIR: str = '/tmp/test-results'
BUILD_STATE: typing.Dict[str, typing.Any] = {}
if not os.path.exists(TEST_OUTPUT_DIR):
    os.makedirs(TEST_OUTPUT_DIR)
TEST_CASES: typing.List[TestCase] = []

def run_command(cmd: typing.List[str]) -> types.GeneratorType:
    proc = subprocess.Popen(' '.join(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    while proc.poll() is None:
        time.sleep(.1)

    if proc.poll() > 0:
        yield proc.poll(), proc.stderr.read().decode(ENCODING)

    elif proc.poll() != None:
        yield proc.poll(), proc.stdout.read().decode(ENCODING)

    else:
        # if proc.poll() is None, its still running the subprocess.
        # block until done
        pass


def find_artifacts(start_dir: str) -> types.GeneratorType:
    for root, dirnames, filenames in os.walk(start_dir):
        for filename in filenames:
            if filename.endswith('.tar.gz'):
                yield os.path.join(start_dir, filename)

for artifact_path in find_artifacts(ARTIFACT_DEST_DIR):
    logger.info(f'Found Artifact in path[{artifact_path}]. Building Artifact')
    notebook_name: str = os.path.basename(artifact_path).rsplit('.', 1)[0]
    extraction_path: str = tempfile.mkdtemp(prefix=notebook_name)
    build_script_path: str = None
    with tarfile.open(artifact_path, "r:gz") as tar:
        for member in tar.getmembers():
            if member.isdir():
                dir_path: str = os.path.join(extraction_path, member.path)
                os.makedirs(dir_path)

            elif member.isfile():
                filepath: str = os.path.join(extraction_path, member.path)
                with open(filepath, 'wb') as stream:
                    stream.write(tar.extractfile(member).read())

                if os.path.basename(member.path) == 'build.sh':
                    build_script_path = filepath

            else:
                raise NotImplementedError


    owd: str = os.getcwd()
    build_dir: str = os.path.dirname(build_script_path)
    logger.info(f'Changing to build_dir[{build_dir}]')
    os.chdir(build_dir)
    BUILD_STATE[notebook_name] = {'stdout': [], 'stderr': []}
    start = datetime.utcnow()
    for return_code, comm, in run_command(['bash', 'build.sh']):
        if return_code > 0:
            logger.error(comm)
            BUILD_STATE[notebook_name]['exit-code'] = return_code
            BUILD_STATE[notebook_name]['stderr'].append(comm)

        else:
            BUILD_STATE[notebook_name]['exit-code'] = return_code
            BUILD_STATE[notebook_name]['stdout'].append(comm)
            logger.info(comm)

    delta = datetime.utcnow() - start
    logger.info(f'Changing back to old working dir[{owd}]')
    os.chdir(owd)
    test_case = TestCase(f'{notebook_name} Test')
    if BUILD_STATE[notebook_name]['exit-code'] > 0:
        test_case.result = Error('\n'.join(BUILD_STATE[notebook_name]['stderr']), BUILD_STATE[notebook_name]['exit-code'])
        TEST_CASES.append(test_case)

    TEST_CASES.append(test_case)

test_suite = TestSuite(f'Notebooks Test Suite')
[test_suite.add_testcase(case) for case in TEST_CASES]
test_output_path: str = os.path.join(TEST_OUTPUT_DIR, f'results.xml')
xml = JUnitXml()
xml.add_testsuite(test_suite)
xml.write(test_output_path)

# from nbpages import make_parser, run_parsed, make_html_index
# 
# args = make_parser().parse_args()
# 
# converted = run_parsed('.', output_type='HTML', args=args)
# 
# converted = [item for item in converted if not os.path.basename(item) in ['test-fail.html', 'test-succeed.html']]
# make_html_index(converted, './index.tpl')

