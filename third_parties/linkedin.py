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
        if v not in ([], "", "", None) 
    }
    keys_to_keep = ['industryName','firstName', 'lastName', 'locationName', 'student', 'education', 'experience','projects']
    relevant_data = {key: data[key] for key in keys_to_keep if key in data}
    print(f"length:{len(relevant_data)}")
    print(type(relevant_data))
    print(relevant_data.keys())
    print(relevant_data)
    
    return relevant_data
