import os
import requests
import json

# Set the API key and secret
client_id = os.environ['77kr99ecweogg2']
client_secret = os.environ['zLWBdqeMWqLb4J36']

# Set the access token
access_token = os.environ['AQU7kp57iWKp2XvF9a3pNsaWsO7decQSLEtVgy_f7WjSU7u5WJvQBiq0DfRKlftmLJmDbBh40cs7o5P8fbhyCkhsnEam41KU_4-iEhOgtgnwVbenbZ0Jm5Z4ulq0P7yz2-IDWEgvFJNb6fB9acghkSIRanNuAF70xcQJUAl507QYMgolvz7hMMMgTATQTP1hsi8t2XXDNk-RSjvMG0kVMh-we-yNY2gOqxg34MKOyMl_GYwqMGWpiiN6H16FEo_NdgMI3TEakZUOZDHbmTjwHNSl3sC5VDCdajNzy5JslHt0xHw8aFYwfhsSk8UZbrjwFmCddRE_4PhiXyNd2YNTM0013S5VMw']
h
# Set the base URL for the API requests
base_url = 'https://api.linkedin.com/v2/'

# Define a function to make API requests
def make_request(url):
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=headers)
    data = json.loads(response.content)
    return data

# Example: get the user's profile
profile_url = base_url + 'me?projection=(id,firstName,lastName)'
profile_data = make_request(profile_url)
print(profile_data)
