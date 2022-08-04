'''
This script is for downloading large queries from the MAST archives. This is
often necessary when you have many observations.
'''

from astroquery.mast import Observations
from astropy.table import unique, vstack

matched_obs = Observations.query_criteria(
        obs_collection = 'JWST'
        , proposal_id = '1173'
        , instrument_name = 'Miri'
        , filters = 'OPAQUE'
        )

t = [Observations.get_product_list(obs) for obs in matched_obs]
files = unique(vstack(t), keys='productFilename')

# This requires you to enter your token only once... until it expires
Observations.login(store_token=True)

manifest = Observations.download_products(
           files,
           productSubGroupDescription='UNCAL',
           curl_flag=True
           )
