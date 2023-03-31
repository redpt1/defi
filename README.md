# defi

任务1：你自己的市场
- [x] 为ETH与一个代币建立两个去中心化的市场平台

首先建立两种代币

| 代币名称 | 数量      | 地址                                       |
| -------- | --------- | ------------------------------------------ |
| FTK      | 500,0000  | 0x88207b39c2d2b52Ee6a1a7200Bf3E54Dcb6aD92E |
| STK      | 1000,0000 | 0xa6E20fAaBCD933dE87a670dc9Af3B1de674deB83 |

- [x] Oracles每30秒向链上发送一次速率更新

每30s更新一回

| 预言机 | address                                    |
| ------ | ------------------------------------------ |
| ftk    | 0x16d74cBebCa74D7e08f250B438c543556e6B03B6 |
| stk    | 0x4819ec52B9A74020EcDc6A212d7F9b428127A33b |

| 供应商 | address                                    |
| ------ | ------------------------------------------ |
| ftk    | 0x379161255F44E70Ffe5B8b83E32Ec6040ab1D3f7 |
| stk    | 0x66D667A78E1001B4022c345708e7a3A379889145 |

- [x] 在一定范围内（例如，ETH->USDC，在1000-1010之间）的随机价格波动（从固定的种子开始的确定性，以实现可重复性）

随机数要在一定的范围内，使用伪随机数，使用了正余弦函数

- [x] 预定义的流动性

供应商合约转账

- [x] 实现买入（）、卖出（）功能

- [x] 建立一个客户端，监测来自两个不同市场的价格更新，例如，在Python中（使用web3py）。

增加ui

应该把ganache的自动挖矿关掉，要不然绘制图形会出现小问题。

- [ ] 计算交易费用加上平台费用与买入/卖出费率，决定何时进行交易，报告所有费用和费率（以及区块#），进行一次交易，在两个市场上买入和卖出代币，以赚取ETH利润







- [ ] 监控币价Uniswap, Sushiswap,  Binance







tracking 不同平台 汇率 + fees



[Entities | SushiSwap](https://docs.sushi.com/docs/Developers/Subgraphs/Exchange/Entities)

[Query Examples | Uniswap](https://docs.uniswap.org/api/subgraph/guides/examples#token-daily-aggregated)

[Exchange Information – Binance API Documentation (binance-docs.github.io)](https://binance-docs.github.io/apidocs/spot/en/#exchange-information)





Uniswap和SushiSwap的交易费用（每笔交易0.3%）；

以太坊网络交易费用（撰写本文时每笔交易大约4美元）；

Uniswap市场和SushiSwap市场的滑点； 
