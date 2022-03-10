from os import environ
from py import process
from web3 import Web3
import schedule
from brownie import config, network, Wei
from scripts.tooling import get_account, getPayee
from dotenv import load_dotenv

load_dotenv()

GASLIMIT = 100000  ## this needs to be changed to be realistic


def issuePayouts():
    payees = getPayee()
    account = get_account()
    balance = Web3.fromWei(account.balance())
    print("Balance of bot is ", balance)
    payout = int(balance / len(payees))
    if payout >= config["min_payout_in_eth"]:
        for pay in payees:
            tx = account.transfer(pay, payout, GASLIMIT)
            tx.wait(1)


def main():
    schedule.every().monday.at("12:00").do(issuePayouts())


if __name__ == "__main__":
    main()
