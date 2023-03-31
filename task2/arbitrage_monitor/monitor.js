var axios = require("axios")


function getFromUni(){
    axios.post('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3', {
      query: `
{
  tokens(orderBy: volumeUSD, orderDirection: desc){
        id
        symbol
        derivedETH

  }
}
`
    })
      .then((result) => {

          for (const tokeninfo of result.data.data.tokens) {
            var address = tokeninfo.id
            var name = tokeninfo.symbol
            tokeninfo.derivedETH = tokeninfo.derivedETH.match(/^\d+(?:\.\d{0,10})?/)

            if(name === '')
              tokeninfo.symbol = 'Null'
            this.tableData1.push(tokeninfo)
       //     console.log("======================Token address: "+address+"==============================")
        //    console.log(name+" / ETH: "+ tkperEth.match(/^\d+(?:\.\d{0,10})?/))
            //console.log("TVL(USD): "+TVL.match(/^\d+(?:\.\d{0,2})?/))
          }

        }
      )
      .catch((error) => {
        console.error(error)
      })
  }


function getFromSushi(){
    axios.post('https://api.thegraph.com/subgraphs/name/sushiswap/exchange', {
      query: `
{
  tokens(orderBy: volumeUSD, orderDirection: desc){
        id
        symbol
        derivedETH

  }
}
`
    })
      .then((result) => {

          for (const tokeninfo of result.data.data.tokens) {
            var address = tokeninfo.id
            var name = tokeninfo.symbol
            tokeninfo.derivedETH = tokeninfo.derivedETH.match(/^\d+(?:\.\d{0,10})?/)

            if(name === '')
              tokeninfo.symbol = 'Null'
            this.tableData1.push(tokeninfo)
       //     console.log("======================Token address: "+address+"==============================")
        //    console.log(name+" / ETH: "+ tkperEth.match(/^\d+(?:\.\d{0,10})?/))
            //console.log("TVL(USD): "+TVL.match(/^\d+(?:\.\d{0,2})?/))
          }

        }
      )
      .catch((error) => {
        console.error(error)
      })
  }

