<template>
  <div id="building">
        <div class="login_title">

          <h1>Exchange Rate</h1>
        </div>

    <el-tabs type="border-card" style="width: 90%; height:80%;  margin: auto" stretch
             v-model="activeTab"
             @tab-click="handleClick">

      <el-tab-pane name="uni">
        <span slot="label">
          <svgIcon name="uni" :scale="12" />
          Uniswap
        </span>

        <el-table
          :data="tableData1"
          height="650"

          stripe
          style="width: 90% ;margin: auto"
          empty-text="please wait..."
        >

          <el-table-column
            prop="symbol"
            label="Token Name"
            align="center"
          >
            <template v-slot="{row}">
              <el-link :href="'https://info.uniswap.org/#/tokens/'+row.id" target="_blank" class="buttonText"  type="primary" :underline="true">{{row.symbol}} </el-link>
            </template>

          </el-table-column>

          <el-table-column
            prop="derivedETH"
            label="Exchange rate to ETH"
            align="center"
          >
          </el-table-column>

        </el-table>

      </el-tab-pane>

      <el-tab-pane name="sushi">
        <span slot="label">
          <svgIcon name="sushiswap" :scale="6" />
          Sushiswap
        </span>

        <el-table
          :data="tableData2"
          height="650"

          stripe
          style="width: 90% ;margin: auto"
          empty-text="please wait..."
        >

          <el-table-column
            prop="symbol"
            label="Token Name"
            align="center"
          >
            <template v-slot="{row}">
              <el-link :href="'https://etherscan.io/address/'+row.id" target="_blank" class="buttonText"  type="primary" :underline="true">{{row.symbol}} </el-link>
            </template>

          </el-table-column>

          <el-table-column
            prop="derivedETH"
            label="Exchange rate to ETH"
            align="center">
          </el-table-column>

        </el-table>

      </el-tab-pane>

      <el-tab-pane name="binance">
          <span slot="label">
          <svgIcon name="binance" :scale="70" />
          Binance
        </span>

        <el-table
          :data="tableData3"
          height="650"

          stripe
          style="width: 90% ;margin: auto"
          empty-text="please wait..."
        >

          <el-table-column
            prop="symbol"
            label="Pool"
            align="center"
          >
          </el-table-column>

          <el-table-column
            prop="price"
            label="Exchange rate"
            align="center"
          >
          </el-table-column>

        </el-table>
      </el-tab-pane>
    </el-tabs>

  </div>

</template>

<script>
export default {
  data() {
    return {
      tableData1: [],
      tableData2: [],
      tableData3: [],
      activeTab: 'uni'
    }
  },


  methods: {
    handleClick(tab, event) {
      console.log(tab, event);
      if (tab.name === 'uni'){
        this.getFromUni()
      }
      else if(tab.name === 'sushi'){
        this.getFromSushi()
      }else{
        this.getFromBinance()
      }
    },
    getFromUni(){
      this.tableData1 = []
      this.$axios.post('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3', {
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
    },
    getFromSushi(){
      this.tableData2 = []
      this.$axios.post('https://api.thegraph.com/subgraphs/name/sushiswap/exchange', {
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
              this.tableData2.push(tokeninfo)
            }

          }
        )
        .catch((error) => {
          console.error(error)
        })
    },
    getFromBinance(){
      this.tableData3 = []
      this.$axios.get('https://data.binance.com/api/v3/ticker/price')
        .then((result) => {
            for (const tokeninfo of result.data) {
              var name = tokeninfo.symbol
              if(name === '')
                tokeninfo.symbol = 'Null'
              this.tableData3.push(tokeninfo)
            }

          }
        )
        .catch((error) => {
          console.error(error)
        })
    },




  }
}

</script>

<style scoped>
.login_title {
  /* 字体水平左右居中 */
  text-align:center;
  /*color: white;*/

}
#building{
  /*background:url("../assets/back2.jpeg");*/
  width:100%;
  height:100%;
  position:fixed;
  background-size:100% 100%;
}
</style>
