import json
from pathlib import Path
from brownie import (
    accounts,
    config,
    KaiECOToken721,
)

def main():
    dev = accounts.add(config['wallets']['from_key'])
	# Get the most recent deployment of our contract
    kai_collection = KaiECOToken721[-1]
    #Getting Our Existing Tokens 
    existing_tokens = kai_collection.tokenIds()
    for i in range(1,existing_tokens+1):
        tokenURi = kai_collection.tokenURI(i)
        print('tokenURI: ', tokenURi)
    
    #once updated now we have to set the 0th token to be the first token in the metadata file and therefore change the metadata file
