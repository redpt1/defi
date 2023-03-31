from web3 import Web3
import json
import time
import asyncio
import matplotlib.pyplot as plt
import math
# HTTPProvider:
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
 
# WebsocketProvider:
#w3 = Web3(Web3.WebsocketProvider('wss://127.0.0.1:7545'))
account_address = "0xE80d399c6A73E94f9D6d10D2d3e2fCFBD0B78eDD"
filePath1 = "oracle.abi"
abi1 = open(filePath1, encoding='utf-8').read()
contract_addr1 = '0x34eC3536dA51Ebc2cB65C2CEbFF4421Ba4eE2e06'
ftk = w3.eth.contract(address=contract_addr1, abi=abi1)

filePath2 = "oracle-2.abi"
abi2 = open(filePath2, encoding='utf-8').read()
contract_addr2 = '0x5B5723155D8Ec4bBCb17aC162b4775e3Dfca06F2'
stk = w3.eth.contract(address=contract_addr2, abi=abi2)



platform1 = "0xb5Db319d2F46289abe4BAd820951A51F53919Eee" 
p_abi_path1 = "p1.abi"
p1_abi = open(p_abi_path1, encoding='utf-8').read()
p1 = w3.eth.contract(address=platform1, abi=p1_abi)


value = int(math.pow(10, 16)) # 出价

balance = w3.eth.get_balance(account_address)
print(balance)