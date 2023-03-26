from web3 import Web3
import json
import time
import asyncio
import matplotlib.pyplot as plt

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



plt.rcParams["figure.figsize"] = (12,8)
plt.rcParams['toolbar'] = 'None'


plt.style.use('ggplot')
plt.gcf().canvas.manager.set_window_title('Monitor')

def handle_event(event,symbol):
   # currentDateAndTime = datetime.now()
    log = json.loads(Web3.toJSON(event))
    price = log["args"]["_price"]
    bn = log["blockNumber"]

    
    blocktime = w3.eth.get_block(bn)
    blocktime = blocktime["timestamp"]
    reg_time = time.localtime(blocktime)
    reg_time = time.strftime("%m-%d %H:%M:%S", reg_time)
    
    
    return (bn,blocktime,symbol,price,reg_time)

async def log_loop(symbol,event_filter, poll_interval, queue):
    for event in event_filter.get_all_entries():
            await queue.put(handle_event(event,symbol))             
    while True:
        for event in event_filter.get_new_entries():
            await queue.put(handle_event(event,symbol))

        await asyncio.sleep(poll_interval)


async def drawer(queue0, queue1):
    data0 = []
    data1 = []
    while True:
        item = await asyncio.gather(queue0.get(), queue1.get())
        data0.append(item[0])
        data1.append(item[1])
        if len(data0) > 6:
            data0.pop(0)
        if len(data1) > 6:
            data1.pop(0)
        plt.clf()
        plt.plot([x[4] for x in data0],[x[3] for x in data0],color="red",marker='*', label="FTK/ETH")
        plt.plot([x[4] for x in data1],[x[3] for x in data1],color="blue",marker='*', label="STK/ETH")
        plt.xticks(rotation=45)
        
        plt.legend()
        plt.title("Live Data")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.grid(axis='x')
        plt.pause(1.5)
        queue0.task_done()
        queue1.task_done()
        


def main():
    
    queue0 = asyncio.Queue()
    queue1 = asyncio.Queue()
    
    event_filter1 = ftk.events.UpdateFTKPrice.createFilter(fromBlock=w3.eth.blockNumber-4)
    event_filter2 = stk.events.UpdateSTKPrice.createFilter(fromBlock=w3.eth.blockNumber-4)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop("FTK",event_filter1, 1,queue0),log_loop("STK",event_filter2,1,queue1),drawer(queue0,queue1)))
    finally:
        # close loop to free up system resources
        loop.close()
    

if __name__ == "__main__":
    plt.ion()
    main()

