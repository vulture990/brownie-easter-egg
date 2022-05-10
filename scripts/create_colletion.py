import json
from pathlib import Path
from brownie import (
    accounts,
    config,
    KaiECOToken721,
)
#KaiECOToken721
from scripts.create_metadata import write_metadata
def main():
    # Get our account info
    dev = accounts.add(config['wallets']['from_key'])
	# Get the most recent deployment of our contract
    kai_collection = KaiECOToken721[-1]
	# Check the number of currently minted tokens
    existing_tokens = kai_collection.tokenIds()
    print(existing_tokens)
    # Check if we'eve already got our metadata hashes ready
    if Path(f"metadata/data.json").exists():
        print("Metadata already exists. Skipping ...")
        meta_data_hashes = json.load(open(f"metadata/data.json"))
        print("done")
    else:
        meta_data_hashes = write_metadata(3)

    print("9bl",meta_data_hashes)

    for token_id in range(existing_tokens, 3):
        # Get the metadata hash for this token's URI
        meta_data_hash = meta_data_hashes[token_id]
        # Call our createCollectible function to mint a token
        transaction = kai_collection.mintNFT(
            meta_data_hash, {'from': dev,  "gas_limit": 2074044, "allow_revert": True})
        print("done")
    # Wait for 3 blocks to be created atop our transactions
        transaction.wait(3)
