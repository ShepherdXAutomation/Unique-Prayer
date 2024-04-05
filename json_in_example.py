import openai # TODO: The 'openai.api_' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(api_="json_in_example.py")'
# openai.api_ = "json_in_example.py"

# Initialize the ApifyClient with your API token


# Prepare the Actor input
run_input = {
    "directUrls": ["https://www.instagram.com/humansofny/"],
    "resultsType": "posts",
    "resultsLimit": 1,
    "searchType": "hashtag",
    "searchLimit": 1,
    "addParentData": False,
}


st.text("hello");