import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_iF4aQzNxrGfGUhN99P8oPbJSoZuLRH2AKIZy")

# Prepare the Actor input
run_input = {
    "directUrls": ["https://www.instagram.com/humansofny/"],
    "resultsType": "posts",
    "resultsLimit": 1,
    "searchType": "hashtag",
    "searchLimit": 1,
    "addParentData": False,
}
