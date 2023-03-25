from web3 import Web3
import json
import time
import asyncio
from datetime import datetime
import threading

# HTTPProvider:
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
 
# WebsocketProvider:
#w3 = Web3(Web3.WebsocketProvider('wss://127.0.0.1:7545'))
account_address = "0xE80d399c6A73E94f9D6d10D2d3e2fCFBD0B78eDD"
filePath1 = "oracle.abi"
abi1 = open(filePath1, encoding='utf-8').read()
contract_addr1 = '0x16d74cBebCa74D7e08f250B438c543556e6B03B6'
ftk = w3.eth.contract(address=contract_addr1, abi=abi1)

filePath2 = "oracle-2.abi"
abi2 = open(filePath2, encoding='utf-8').read()
contract_addr2 = '0x4819ec52B9A74020EcDc6A212d7F9b428127A33b'
stk = w3.eth.contract(address=contract_addr2, abi=abi2)

def handle_event(event,symbol):
    currentDateAndTime = datetime.now()
    price = json.loads(Web3.toJSON(event))["args"]["_price"]
    print(symbol,price,currentDateAndTime)

async def log_loop(symbol,event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event,symbol)
        await asyncio.sleep(poll_interval)


# when main is called
# create a filter for the latest block and look for the "PairCreated" event for the uniswap factory contract
# run an async loop
# try to run the log_loop function above every 2 seconds
def main():
    event_filter1 = ftk.events.UpdateFTKPrice.createFilter(fromBlock='0')
    event_filter2 = stk.events.UpdateSTKPrice.createFilter(fromBlock='0')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop("FTK",event_filter1, 1),log_loop("STK",event_filter2,1)))
    finally:
        # close loop to free up system resources
        loop.close()


if __name__ == "__main__":
    main()

