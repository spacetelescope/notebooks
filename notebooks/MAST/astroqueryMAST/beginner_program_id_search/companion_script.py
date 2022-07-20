import sys
from astroquery.mast import Observations

def download_by_jwst_pid (pid, curl_flag = False):
    """
    This function retrieves all of the minimum recommend products for a single program ID.
    Inputs:
    pid [int] – program ID number
    curl_flag [Boolean] – If set to true, function returns a curl script.
    """

    Observations.login(store_token=True)
    obs_list = Observations.query_criteria(proposal_id=pid)
    data_products = Observations.get_product_list(obs_list)
    filtered_prod = Observations.filter_products(data_products, mrp_only=True)
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
sys.exit(main())
