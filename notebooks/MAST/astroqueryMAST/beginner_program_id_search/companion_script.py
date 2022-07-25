import sys
from astroquery.mast import Observations

def download_by_jwst_pid (pid, curl_flag):
    """
    This function retrieves all of the level 2 science products for a single program ID.
    Inputs:
    pid [int] – program ID number
    curl_flag [Boolean] – If set to true, function returns a curl script.
    """

    # Login, search for observations
    Observations.login(store_token=True)
    obs_list = Observations.query_criteria(proposal_id=pid)
    data_products = Observations.get_product_list(obs_list)
    filtered_prod = Observations.filter_products(data_products, calib_level=[2], productType='SCIENCE')

    # Filesize check
    total = 0
    for fsize in filtered_prod['size']:
        total = total+fsize
    # Use curl for large downloads.
    if total/10**9 > 1 and curl_flag==False:
        curl_flag = True
        print("\nDownload too large. Switching to curl script.")
    # User must confirm download size
    prompt = "Total download size is: " + '{:.2f}'.format(total/10**9) + ' GB. Proceed? (y/n)\n'
    resp = input(prompt)
    if resp != 'y':
        quit()

    # Check for curl flag
    if curl_flag:
        path = Observations.download_products(filtered_prod, curl_flag=True)
        return path
    else:
        manifest = Observations.download_products(filtered_prod)
        return manifest

def main():
    return download_by_jwst_pid(a, b)

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = sys.argv[2]
    if b == 'True': b=True
    if b == 'False': b=False
sys.exit(main())
