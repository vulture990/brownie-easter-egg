from brownie import KaiECOToken721, network, accounts, config, Contract
from brownie.network.gas.strategies import GasNowStrategy


def main():
    gas_strategy = GasNowStrategy("fast")
    # Fill your own MetaMask public key here
    creator_address = "0x931afCdbdEC78bA090b9794e5a6c9E9314aFB1F8"
    net = network.show_active()
    water_collection = KaiECOToken721[-1]
    # Get the asks contract depening on the network
    if net == "polygon-main":
        asks_address = "0x3634e984Ba0373Cfa178986FD19F03ba4dD8E469"
        asksv1 = Contract.from_explorer(asks_address)
        module_manager = Contract.from_explorer("0xCCA379FDF4Beda63c4bB0e2A3179Ae62c8716794")
        erc721_helper_address = "0xCe6cEf2A9028e1C3B21647ae3B4251038109f42a"
        water_address = "0xe6a315a94b4796CEcEe05e174423922fAce1FCA2"
        weth_address = "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619"
    elif net == "rinkeby":
        asks_address = "0xA98D3729265C88c5b3f861a0c501622750fF4806"
        asksv1 = Contract.from_explorer(asks_address)
        module_manager = Contract.from_explorer("0xa248736d3b73A231D95A5F99965857ebbBD42D85")
        erc721_helper_address = "0x029AA5a949C9C90916729D50537062cb73b5Ac92"
        water_address = "0xe6a315a94b4796CEcEe05e174423922fAce1FCA2"
        weth_address = "0xc778417E063141139Fce010982780140Aa0cD5Ab"
    dev = accounts.add(config['wallets']['from_key'])
    # Give Zora permission to facilitate transactions with the ASK contract
    module_manager.setApprovalForModule(asks_address, True, {"from": dev})

    water_collection.setApprovalForAll(erc721_helper_address, True, {'from': dev,  "gas_limit": 20740440, "allow_revert": True}) 
    for token_id in range(3):
        price = (3- token_id) * 10 ** 16
        asksv1.createAsk(water_address, # Address of our contract
                         token_id, # Token ID of the NFT to be listed
                         price, # Our asking price
                         weth_address, # The address of the token required to pay for our NFT
                         creator_address, # The address where the funds will be sent to
                         0, # A finder reward


                        
                         
                         {'from': dev,  "gas_limit": 20740440, "allow_revert": True}) # Sign our transaction with our account