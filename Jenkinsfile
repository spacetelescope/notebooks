def conda_packages = [
    "astropy",
    "scipy",
    "astroquery",
    "matplotlib",
    "jupyter",
    "pandas",
    "drizzlepac",
    "crds",
    "ccdproc",
    "acstools",
    "photutils",
    "regions",
    "pyregion"
]

def conda_channels = [
  "astropy-ci-extras",
  "astropy",
  "http://ssb.stsci.edu/astroconda",
]

def pip_install_args = "--progress-bar=off"

if (utils.scm_checkout()) return

bc = new BuildConfig()
bc.nodetype = 'linux'
bc.name = 'build'
bc.conda_channels = conda_channels
bc.conda_packages = conda_packages
bc.build_cmds = [
"python --version"
 "pip install k2flix",
 "pip install git+https://github.com/eteq/nbpages.git",
 "python3 convert.py",
]
bc.test_cmds = [
  'python3 -m "nbpages.check_nbs"'
]

utils.run([bc])
