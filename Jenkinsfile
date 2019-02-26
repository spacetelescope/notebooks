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

if (utils.scm_checkout()) return

bc = new BuildConfig()
bc.nodetype = 'linux'
bc.name = 'build'
//bc.conda_channels = conda_channels
//bc.conda_packages = conda_packages
bc.build_cmds = [
  "conda env create -f environment.yml",
  "with_env -n notebooks python convert.py",
// "pip install k2flix",
// "pip install git+https://github.com/eteq/nbpages.git",
// "pip install astroquery --pre",
// "pip install astroquery --upgrade",
 "with_env python convert.py",
]
bc.test_cmds = [
  'with_env -n notebooks python -m "nbpages.check_nbs"'
]

utils.run([bc])
