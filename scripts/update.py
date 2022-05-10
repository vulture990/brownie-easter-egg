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
    meta_data_hashes = json.load(open(f"metadata/data.json"))
    print("9bl",meta_data_hashes)
    #updating the 0th token to be the first token imge in the metadata file
    transaction = kai_collection.updateNFT(1,
            meta_data_hashes[2], {'from': dev,  "gas_limit": 2074044, "allow_revert": True})
    transaction.wait(3)
    #once updated now we have to set the 0th token to be the first token in the metadata file and therefore change the metadata file
