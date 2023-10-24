from linkedin_api import Linkedin
from dotenv import load_dotenv
import os
from urllib.parse import urlparse





def scrape_linkedin_profile(linked_in_url: str):
    """scrape information from linkedin profiles,
    Manually scrape info from linkedin profiles.
    """
    load_dotenv()
    username = os.getenv("L_USER")
    pwd = os.getenv("L_PASS")
    api = Linkedin(username=username, password=pwd)
    parsed_url = urlparse(linked_in_url)
    path_components = parsed_url.path.split('/')
    linked_in_username = path_components[-1]
    data = api.get_profile(linked_in_username)
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["certifciations"]
    }
    return data
