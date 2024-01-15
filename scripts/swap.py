from scripts.deploy import deploy
from scripts.helpful_scripts import get_account






def main():
    weth_address = '0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6'
    router = deploy()
    dai_address = '0x6B175474E89094C44Da98b954EedeAC495271d0F'
    path = [weth_address,dai_address]
    my_address = '0xC5D2b35A410334d4D11b5f07Ee95b0E3EFCA6c28'

    router.swapExactETHForTokens(0,path,my_address,2000000000000000,{'from':get_account(), 'value':0.01, 'gas_limit': 10**8})
    print('swapped!')