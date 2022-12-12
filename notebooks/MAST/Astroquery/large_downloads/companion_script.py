'''
This script downloads large queries from the MAST Archive. This is
often necessary when you have many observations. By default, this script
pulls data from JWST program 1173 and generates a separate bash script to
download the files.
'''
# Necessary imports. We use astroquery to search the MAST archives.
# Search results are returned as an astropy table, so we also import some
# useful table methods.
from astroquery.mast import Observations
from astropy.table import unique, vstack
import argparse

def fetch_files(progID, chunk_size):
    # Observation search criteria. You can customize the search using the fields
    # listed and described at https://mast.stsci.edu/api/v0/_c_a_o_mfields.html
    matched_obs = Observations.query_criteria(
            obs_collection = 'JWST'
            , proposal_id = progID
            , instrument_name = 'Miri'
            , filters = 'OPAQUE'
            )

    # Make sure the search returned results. If not, exit the program.
    if len(matched_obs) == 0:
        print('The program query returned no matching observations. Check your',
        'query criteria and try again.')
        quit()

    # Go through the observations in "chunks", five at a time, and request the
    # associated data products. This is faster than doing one at a time.
    # After getting products, keep only the unique set to remove any duplicate files.
    chunks = [matched_obs[i:i+sz_chunk] for i in range(0,len(matched_obs), chunk_size)]
    t = [Observations.get_product_list(obs) for obs in chunks]
    files = unique(vstack(t), keys='productFilename')

    # If the observations are not public, you will need a valid Auth.MAST
    # token for retrieval (see: https://auth.mast.stsci.edu/info). Specify
    # the token as an argument to the login() method respond to the terminal
    # prompt, or put it in the environment variable $MAST_API_TOKEN.

    #Observations.login(store_token=True)

    # This generates a curl script, which can be used to download the files.
    # You can download directly by setting 'curl_flag = False'
    # You can also add aditional filters, which are listed and described at
    # https://mast.stsci.edu/api/v0/_productsfields.html
    manifest = Observations.download_products(
               files
               , curl_flag=True
               , productType=['SCIENCE', 'INFO']
               )

if __name__ == '__main__':
    '''
    Input the JWST program ID and "chunk" size (default is five; this is fastest.)
    Script will return a separate bash file that uses curl to download your data.
    '''
    descr_text = 'Fetch a script for downloading data products from a JWST Program'
    parser = argparse.ArgumentParser(description=descr_text)
    parser.add_argument('-id', '--progID', type=str, default='1073',
                        help='JWST Program ID')
    parser.add_argument('-c', '--chunk_size', type=int, default=5,
                        help='Number of Obs to process at a time')
    args = parser.parse_args()
    fetch_files(args.progID, args.chunk_size)
