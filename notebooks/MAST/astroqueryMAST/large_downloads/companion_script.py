'''
This script downloads large queries from the MAST archives. This is
often necessary when you have many observations.
'''
# Necessary imports
from astroquery.mast import Observations
from astropy.table import unique, vstack

# Observation search criteria
matched_obs = Observations.query_criteria(
        obs_collection = 'JWST'
        , proposal_id = '1173'
        , instrument_name = 'Miri'
        , filters = 'OPAQUE'
        )

# Go through each observation, one-by-one, and request the associated data products
t = [Observations.get_product_list(obs) for obs in matched_obs]
files = unique(vstack(t), keys='productFilename')

# This requires you to enter your token only once, until it needs to be renewed
Observations.login(store_token=True)

# This generates a curl script, which can be used to download the files.
# You can download directly by setting 'curl_flag = False'
manifest = Observations.download_products(
           files,
           productSubGroupDescription='UNCAL',
           curl_flag=True
           )
