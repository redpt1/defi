import asyncio
import random
import matplotlib.pyplot as plt

plt.rcParams['toolbar'] = 'None'
async def produce(queue, num):
    while True:
        await asyncio.sleep(random.randint(0, 3))
        item = random.randint(0, 10)
        await queue.put((num, item))


async def consume(queue0, queue1):
    data0 = []
    data1 = []
    while True:
        item = await asyncio.gather(queue0.get(), queue1.get())
        data0.append(item[0])
        data1.append(item[1])
        if len(data0) > 10:
            data0.pop(0)
        if len(data1) > 10:
            data1.pop(0)
        plt.clf()
        plt.plot([x[1] for x in data0], label="Producer 0")
        plt.plot([x[1] for x in data1], label="Producer 1")
        plt.legend()
        plt.title("Live Data")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.grid(True)
        plt.pause(0.1)
        queue0.task_done()
        queue1.task_done()


async def main():
    queue0 = asyncio.Queue()
    queue1 = asyncio.Queue()

    producers = [
        asyncio.create_task(produce(queue0, 0)),
        asyncio.create_task(produce(queue1, 1)),
    ]
    consumer = asyncio.create_task(consume(queue0, queue1))

    await asyncio.gather(*producers)
    await asyncio.gather(consumer)


if __name__ == "__main__":
    plt.ion()
    asyncio.run(main())