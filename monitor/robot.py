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


platform2 = "0xAe523F875DC4524Bbd335252e54Ac940A45a900e"
p_abi_path2 = "p2.abi"
p2_abi = open(p_abi_path2, encoding='utf-8').read()
p2 = w3.eth.contract(address=platform2, abi=p2_abi)

my_address = "0x5f1c458D46691c63b287aA4ECf8341a30EA6A6F2" #用于交易的账户
gas_price = 2000000000
wei = int(math.pow(10,18))


def handle_event(event):
   # currentDateAndTime = datetime.now()
    log = json.loads(Web3.toJSON(event))
    price = log["args"]["_price"]
    bn = log["blockNumber"]

    
    blocktime = w3.eth.get_block(bn)
    blocktime = blocktime["timestamp"]
    reg_time = time.localtime(blocktime)
    reg_time = time.strftime("%m-%d %H:%M:%S", reg_time)
    
    
    return (bn,blocktime,price,reg_time)

async def log_loop(event_filter, poll_interval, queue):
    # for event in event_filter.get_all_entries():
    #         await queue.put(handle_event(event,symbol))             
    while True:
        for event in event_filter.get_new_entries():
            await queue.put(handle_event(event))

        await asyncio.sleep(poll_interval)


def make_deal(p1,first_price,p2,second_price):
    balance = w3.eth.get_balance(my_address)
    balance_eth1 = w3.fromWei(balance, 'ether')
    print("Before balance: "+str(balance_eth1))
    value = int(math.pow(10, 17)) # 出价
    fee1 = p1.functions.getFee(value).call()
    fee1 = fee1 / wei
    tx_hash1 = p1.functions.buyTokens().transact({'from': my_address,'value':value})
    receipt1 = w3.eth.waitForTransactionReceipt(tx_hash1)
    receipt1 = json.loads(Web3.toJSON(receipt1))
    gas_fee1 = int(receipt1["gasUsed"]) * gas_price / wei
    
    slide = 0.00001
    exp_get_tk = value * first_price * (1 - 0.03 - slide)
    
    fee2 = p2.functions.getFee(value).call()
    fee2 = fee2/second_price/wei
    
    tx_hash2 = p2.functions.sellTokens(int(exp_get_tk)).transact({'from': my_address})
    receipt2 = w3.eth.waitForTransactionReceipt(tx_hash2)
    receipt2 = json.loads(Web3.toJSON(receipt2))
    gas_fee2 = int(receipt2["gasUsed"]) * gas_price / wei
    
    balance = w3.eth.get_balance(my_address)
    balance_eth2 = w3.fromWei(balance, 'ether')
    print("After balance: "+str(balance_eth2))
    print("Balance change: "+str(balance_eth2-balance_eth1))
    print("gas fee in eth: " + str(gas_fee1+gas_fee2))
    print("fee in eth: "+ str(fee1+fee2))
    print("Buy price in eth: " + str(1/first_price)) 
    print("Sell price in eth: " + str(1/second_price))
    print("Rate: "+str(second_price/first_price))
    print("Tx hash: "+receipt2["transactionHash"])
    print("BlockNumber: " + str(receipt2["blockNumber"]))

def handle_deal(first_price,second_price):
    diff = first_price - second_price
    if abs(diff) < 42:
        return

    if diff > 0:
        make_deal(p1,first_price,p2,second_price)
    
    
    if diff < 0:
        make_deal(p2,second_price,p1,first_price)


async def robot(queue0, queue1):
  
    while True:
        item = await asyncio.gather(queue0.get(), queue1.get())
        first_price = float(item[0][2])
        second_price = float(item[1][2])
        print(first_price,second_price)
        #两平台差值
        
        handle_deal(first_price,second_price)
        
        await asyncio.sleep(1.5)
        
        queue0.task_done()
        queue1.task_done()
        


def main():
    
    queue0 = asyncio.Queue()
    queue1 = asyncio.Queue()
    
    event_filter1 = ftk.events.UpdateFPrice.createFilter(fromBlock=w3.eth.blockNumber)
    event_filter2 = stk.events.UpdateSPrice.createFilter(fromBlock=w3.eth.blockNumber)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(event_filter1, 1,queue0),log_loop(event_filter2,1,queue1),robot(queue0,queue1)))
    finally:
        # close loop to free up system resources
        loop.close()
    

if __name__ == "__main__":
    plt.ion()
    main()

