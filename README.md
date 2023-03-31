# defi

任务1：你自己的市场
- [x] 为ETH与一个代币建立两个去中心化的市场平台

首先建立一种代币

| 代币名称 | 数量     | 地址                                       |
| -------- | -------- | ------------------------------------------ |
| MTK      | 500,0000 | 0x9F603d3B60b1E15c18ae6A82d57824A3D8bB4839 |

| 供应商 | address                                    | 流动性                   |
| ------ | ------------------------------------------ | ------------------------ |
| 1      | 0xb5Db319d2F46289abe4BAd820951A51F53919Eee | 5ether         500000MTK |
| 2      | 0xAe523F875DC4524Bbd335252e54Ac940A45a900e | 5ether         500000MTK |

| 预言机 | address                                    |
| ------ | ------------------------------------------ |
| 1      | 0x34eC3536dA51Ebc2cB65C2CEbFF4421Ba4eE2e06 |
| 2      | 0x5B5723155D8Ec4bBCb17aC162b4775e3Dfca06F2 |



- [x] Oracles每30秒向链上发送一次速率更新

- [x] 在一定范围内（例如，ETH->USDC，在1000-1010之间）的随机价格波动（从固定的种子开始的确定性，以实现可重复性）

随机数要在一定的范围内，使用伪随机数，使用了正余弦函数

- [x] 预定义的流动性

供应商合约转账

- [x] 实现买入（）、卖出（）功能

0.3%手续费

- [x] 建立一个客户端，监测来自两个不同市场的价格更新，例如，在Python中（使用web3py）。



- [x] 计算交易费用加上平台费用与买入/卖出费率，决定何时进行交易，报告所有费用和费率（以及区块#），进行一次交易，在两个市场上买入和卖出代币，以赚取ETH利润







- [x] 监控币价Uniswap, Sushiswap,  Binance







tracking 不同平台 汇率 + fees



[Entities | SushiSwap](https://docs.sushi.com/docs/Developers/Subgraphs/Exchange/Entities)

[Query Examples | Uniswap](https://docs.uniswap.org/api/subgraph/guides/examples#token-daily-aggregated)

[Exchange Information – Binance API Documentation (binance-docs.github.io)](https://binance-docs.github.io/apidocs/spot/en/#exchange-information)





Uniswap和SushiSwap的交易费用（每笔交易0.3%）；

以太坊网络交易费用（撰写本文时每笔交易大约4美元）；

Uniswap市场和SushiSwap市场的滑点； 
