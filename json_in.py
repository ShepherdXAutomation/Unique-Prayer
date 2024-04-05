
# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_iF4aQzNxrGfGUhN99P8oPbJSoZuLRH2AKIZy")

# Prepare the Actor input
messages = [
    {"role": "system", "content": "You are a christian pastor. The prayers you provide are in first person context. You provide prayers to users based off the details you give them."}
]


st.text("hello");

messages = [
    {"role": "system", "content": "You are a christian pastor. The prayers you provide are in first person context. You provide prayers to users based off the details you give them."}
]
response = openai.Completion.create(
        model="gpt-4",
        messages=messages
    )
print("ChatGPT:", response.choices[0].message["content"])