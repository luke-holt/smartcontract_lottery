from brownie import Lottery, accounts, config, network
from web3 import Web3


# 0.0115915
# 120000000000000000
def test_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    assert lottery.getEntranceFee() > Web3.toWei(0.010, "ether")
    assert lottery.getEntranceFee() < Web3.toWei(0.013, "ether")
