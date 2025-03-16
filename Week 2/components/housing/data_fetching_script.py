# os interacts with the file system (creating directories, paths)
# tarfile handles .tgz (tar + gzip) com
# six.moves.urllib is a compatibility wrapper for handling URLs across Python 2 &3 

import os
import tarfile
from six.moves import urllib

# Defines the data source (this is a github-hosted dataset)
# HOUSING_PATH is the local storage directory
# HOUSING_URL is the full URL to download the dataset

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


# This is the scripts core function
# This function fetches and extracts housing data.
    # Uses default values for its parameters if the caller doesn't provide them
    # 

def fetch_housing_data(housing_url= HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urlliblrequest.url