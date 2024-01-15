from brownie import config, UniswapV2Router02
from scripts.helpful_scripts import get_account

def deploy():
    account = get_account()
    factory_address = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f'
    weth_address = '0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6'
    router = UniswapV2Router02.deploy(factory_address, weth_address,{'from':account})
    print("Deployed!")
    return router

def main():
    deploy()