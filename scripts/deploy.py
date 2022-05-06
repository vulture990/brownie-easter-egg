from brownie import KaiECOToken721, accounts, config
def main():
    dev = accounts.add(config['wallets']['from_key'])
    KaiECOToken721.deploy(
        {'from': dev}
    )