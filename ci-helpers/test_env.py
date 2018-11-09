import os
import re
import sys
from distutils.version import LooseVersion

import pytest

PYTEST_LT_3 = LooseVersion(pytest.__version__) < LooseVersion('3')

# Remove this assert once we remove pinning pytest
PYTEST_LT_37 = LooseVersion(pytest.__version__) < LooseVersion('3.7')
assert PYTEST_LT_37


# If we are on Travis or AppVeyor, we should check if we are running the tests
# in the ci-helpers repository, or whether for example someone else is running
# 'py.test' without arguments after having cloned ci-helpers.

if 'APPVEYOR_PROJECT_SLUG' in os.environ:
    if os.environ['APPVEYOR_PROJECT_SLUG'] != 'ci-helpers':
        if PYTEST_LT_3:
            pytest.skip()
        else:
            pytestmark = pytest.mark.skip()

if 'TRAVIS_REPO_SLUG' in os.environ:
    if os.environ['TRAVIS_REPO_SLUG'].split('/')[1] != 'ci-helpers':
        if PYTEST_LT_3:
            pytest.skip()
        else:
            pytestmark = pytest.mark.skip()

# The test scripts accept 'stable' for ASTROPY_VERSION to test that it's
# properly parsed hard-wire the latest stable branch version here


if not LooseVersion(sys.version) < '3.5':
    LATEST_ASTROPY_STABLE = '3.0.5'
    LATEST_ASTROPY_STABLE_WIN = '3.0.5'
else:
    LATEST_ASTROPY_STABLE = '2.0.9'
    LATEST_ASTROPY_STABLE_WIN = '2.0.9'

LATEST_ASTROPY_LTS = '2.0.9'
LATEST_NUMPY_STABLE = '1.15'
LATEST_SUNPY_STABLE = '0.9.2'

if os.environ.get('PIP_DEPENDENCIES', None) is not None:
    PIP_DEPENDENCIES = os.environ['PIP_DEPENDENCIES'].split(' ')
else:
    PIP_DEPENDENCIES = []

if os.environ.get('CONDA_DEPENDENCIES', None) is not None:
    CONDA_DEPENDENCIES = os.environ['CONDA_DEPENDENCIES'].split(' ')
else:
    CONDA_DEPENDENCIES = []


# In this dependency list we should only store the package names,
# not the required versions
dependency_list = ([re.split('=|<|>', PIP_DEPENDENCIES[i])[0]
                    for i in range(len(PIP_DEPENDENCIES))] +
                   [re.split('=|<|>', CONDA_DEPENDENCIES[i])[0]
                    for i in range(len(CONDA_DEPENDENCIES))])


def test_python_version():
    if 'PYTHON_VERSION' in os.environ:
        assert sys.version.startswith(os.environ['PYTHON_VERSION'])
    elif 'TRAVIS_PYTHON_VERSION' in os.environ:
        assert sys.version.startswith(os.environ['TRAVIS_PYTHON_VERSION'])


def test_exported_variables():
    if 'TRAVIS' in os.environ:
        assert os.environ.get('ASTROPY_LTS_VERSION', '') == LATEST_ASTROPY_LTS
        assert os.environ.get('LATEST_NUMPY_STABLE', '') == LATEST_NUMPY_STABLE
        assert os.environ.get('LATEST_SUNPY_STABLE', '') == LATEST_SUNPY_STABLE

def test_numpy():
    if 'NUMPY_VERSION' in os.environ:
        import numpy
        np_version = numpy.__version__
        os_numpy_version = os.environ['NUMPY_VERSION'].lower()
        if 'dev' in os_numpy_version:
            assert 'dev' in np_version
        elif 'pre' in os_numpy_version:
            assert re.match("[0-9.]*[0-9](a[0-9]|b[0-9]|rc[0-9])", np_version)
        else:
            if 'stable' in os_numpy_version:
                assert np_version.startswith(LATEST_NUMPY_STABLE)
            else:
                assert np_version.startswith(os_numpy_version)
            assert re.match("^[0-9]+\.[0-9]+\.[0-9]", np_version)


def test_astropy():
    if 'ASTROPY_VERSION' in os.environ:
        import astropy
        os_astropy_version = os.environ['ASTROPY_VERSION'].lower()
        if 'dev' in os_astropy_version:
            assert 'dev' in astropy.__version__
        else:
            if 'pre' in os_astropy_version:
                assert re.match("[0-9.]*[0-9](rc[0-9])", astropy.__version__)
            elif 'stable' in os_astropy_version:
                if 'APPVEYOR' in os.environ:
                    assert astropy.__version__.startswith(LATEST_ASTROPY_STABLE_WIN)
                else:
                    assert astropy.__version__.startswith(LATEST_ASTROPY_STABLE)
            elif 'lts' in os_astropy_version:
                assert astropy.__version__.startswith(LATEST_ASTROPY_LTS)
            else:
                assert astropy.__version__.startswith(os_astropy_version)
            assert 'dev' not in astropy.__version__

    # We should not install pytest-astropy for the 2.0.x series, since
    # pytest-astropy is a metapackage, check one of its components
    if LATEST_ASTROPY_STABLE.startswith('2'):
        with pytest.raises(ImportError):
            import pytest_doctestplus


def test_mpl():
    if 'MATPLOTLIB_VERSION' in os.environ:
        import matplotlib
        os_mpl_version = os.environ['MATPLOTLIB_VERSION'].lower()

        # Revise when figured out the exact rule behind mpl dev versioning
        if 'dev' in os_mpl_version:
            assert '+' in matplotlib.__version__
        else:
            assert matplotlib.__version__.startswith(os_mpl_version)
            assert '+' not in matplotlib.__version__


def test_sunpy():
    if 'SUNPY_VERSION' in os.environ:
        import sunpy
        os_sunpy_version = os.environ['SUNPY_VERSION'].lower()
        if 'dev' in os_sunpy_version:
            assert 'dev' in sunpy.__version__
        else:
            if 'pre' in os_sunpy_version:
                assert re.match("[0-9.]*[0-9](rc[0-9])", sunpy.__version__)
            elif 'stable' in os_sunpy_version:
                assert sunpy.__version__.startswith(LATEST_SUNPY_STABLE)
            else:
                assert sunpy.__version__.startswith(os_sunpy_version)
            assert 'dev' not in sunpy.__version__


# Check whether everything is installed and importable
def test_dependency_imports():

    # We have to ignore the special case where we are running with --no-deps
    # because we don't expect that import to work.
    if os.environ.get('CONDA_DEPENDENCIES_FLAGS', '') == '--no-deps':
        return

    for package in dependency_list:
        if package == 'pyqt5':
            __import__('PyQt5')
        elif package == 'scikit-image':
            __import__('skimage')
        elif package == 'scikit-learn':
            __import__('sklearn')
        elif package == 'openjpeg':
            continue
        elif package == 'pytest-cov':
            __import__('pytest_cov')
        elif package == 'nomkl':
            import subprocess
            assert 'nomkl' in str(subprocess.check_output(["conda", "list"]))
        elif package == 'mkl':
            import subprocess
            assert 'nomkl' not in str(subprocess.check_output(["conda", "list"]))
            assert 'mkl' in str(subprocess.check_output(["conda", "list"]))
        elif package == '':
            continue
        else:
            __import__(package)


def test_sphinx():
    if 'SETUP_CMD' in os.environ:
        if ('build_sphinx' in os.environ['SETUP_CMD'] or
                'build_docs' in os.environ['SETUP_CMD']):
            import sphinx


def test_open_files():
    if 'open-files' in os.environ.get('SETUP_CMD', ''):
        import psutil


def test_conda_flags():
    if (os.environ.get('CONDA_DEPENDENCIES_FLAGS', '') == '--no-deps' and
            os.environ.get('CONDA_DEPENDENCIES', '') == 'matplotlib'):
        try:
            import numpy
        except:
            pass
        else:
            raise Exception("Numpy should not be installed")
    else:
        pass


def test_pip_flags():
    pip_flags = os.environ.get('PIP_DEPENDENCIES_FLAGS', '')
    if pip_flags.startswith('--log'):
        assert os.path.exists(pip_flags.split()[1])
    else:
        pass


def test_regression_mkl():

    # Regression test to make sure that if the developer version of Numpy is
    # used, scipy still works correctly. At some point, the conda packages for
    # Numpy and Scipy were compiled with the MKL, and this then led to issues
    # if installing Numpy dev with pip without making sure it was also using
    # the MKL. The solution is to simply make sure that we install the
    # ``nomkl`` conda pacakge when installing the developer version of Numpy.

    if os.environ.get('NUMPY_VERSION', '') == 'dev':

        try:
            import scipy
        except ImportError:
            return

        import numpy as np
        from scipy.linalg import inv

        x = np.random.random((3, 3))
        inv(x)


def test_conda_channel_priority():

    channel_priority = os.environ.get('CONDA_CHANNEL_PRIORITY', 'False')

    with open(os.path.expanduser('~/.condarc'), 'r') as f:
        content = f.read()

    assert 'channel_priority: {0}'.format(channel_priority.lower()) in content


if __name__ == '__main__':
    pytest.main(__file__)
