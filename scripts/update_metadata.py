import requests
import os
import json
from brownie import (
    accounts,
    config,
    KaiECOToken721,
)


# 1- need function to pass local file and upload through Pinanta
def pass_data_pinanta(data):
    # Get our Pinata credentials from our .env file
    pinata_api_key = os.environ["PINATA_API_KEY"]
    pinata_api_secret = os.environ["PINATA_API_SECRET"]
    
    # Get the endpoint that we are going to pin    
    endpoint = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    
    # Get the headers that we are going to use
    headers = {
        'pinata_api_key': pinata_api_key,
        'pinata_secret_api_key': pinata_api_secret
    }
    body = {
        'file': data
    }

    response = requests.post(endpoint, headers=headers, files=body)
    print(response.json())







def img_to_binary(img_path): 
    img_path = f"images/"+str(img_path)+".jpg"
    print(img_path)
    with open(img_path, "rb") as f:
        img_binary = f.read()
    return img_binary



# 2- need to get the URI info

def get_uri():
    dev = accounts.add(config['wallets']['from_key'])
	# Get the most recent deployment of our contract
    kai_collection = KaiECOToken721[-1]
    #Getting Our Existing Tokens 
    existing_tokens = kai_collection.tokenIds()
    for i in range(1,existing_tokens+1):
        tokenURi = kai_collection.tokenURI(i)
        print('tokenURI: ', tokenURi)



# 3- take URI info and create a single json file with the same name as image (most likely they will be numbered)

def handle_token_uri(token_uri):
    dev = accounts.add(config['wallets']['from_key'])
    kai_collection = KaiECOToken721[-1]
    tkn_uri=kai_collection.tokenURI(token_uri)
    sr='metadata/updated_'+str(token_uri)+'.json'
    with open(sr, 'w') as f:
        # Finally, we'll write the array of metadata URIs to a file
        json.dump(tkn_uri, f)

# 4) need a single function that then uploads the metadata json file up to IPFS through Pinata


def upload_new_metadata(img_num):
    new_data=img_to_binary(img_num)
    pinata_api_key = os.environ["PINATA_API_KEY"]
    pinata_api_secret = os.environ["PINATA_API_SECRET"]
    
    # Get the endpoint that we are going to pin    
    endpoint = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    
    # Get the headers that we are going to use
    headers = {
        'pinata_api_key': pinata_api_key,
        'pinata_secret_api_key': pinata_api_secret
    }
    body = {
        'file': new_data
    }

    requests.post(endpoint, headers=headers, files=body)



# 5- Need single function where I can call update function in sol file that takes TOkendID and new URI data

def update_metadata(img_num_updated,img_num_to_update):
    dev = accounts.add(config['wallets']['from_key'])
    kai_collection = KaiECOToken721[-1]
    sr=f'metadata/updated_'+str(img_num_to_update)+'.json'
    meta_data_hash = json.load(open(sr))
    transaction = kai_collection.updateNFT(img_num_updated,
            meta_data_hash, {'from': dev,  "gas_limit": 2074044, "allow_revert": True})
    transaction.wait(3)
    #once updated now we have to set the 0th token to be the first token in the metadata file and therefore change the metadata file


def main():
    # pass_data_pinanta(img_to_binary(2))
    get_uri()
    handle_token_uri(2)
    upload_new_metadata(2)
    update_metadata(1,2)





