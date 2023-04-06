<template>
  <el-card style="margin: auto 20%">
    <div>
      <h1>Second Marketplace</h1>


      <div>
        <el-button @click="connectWallet"> connect wallet</el-button>
        <span>address: {{ currentAccount }}</span>
      </div>

      <el-divider> </el-divider>

      <div>Token amount in the vendor: {{ tokenBalance }}</div>
      <el-divider> </el-divider>
      <div>Ether amount in the vendor: {{ ethBalance }}</div>
      <el-divider> </el-divider>

      <div>You have MTK: {{ yourTokenAmount }}</div>

      <el-divider> </el-divider>

      <el-row>
        <el-col :span="6"><div class="grid-content bg-purple"><p>ETH to MTK:</p></div></el-col>
        <el-col :span="12"><div class="grid-content bg-purple-light">
          <el-input placeholder="Wei" type="number" v-model="buyAmount" />
        </div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple">
          <el-button @click="buyTokens">BUY</el-button>
        </div></el-col>
      </el-row>


      <el-divider> </el-divider>


      <el-row>
        <el-col :span="6"><div class="grid-content bg-purple"><p>MTK to ETH:</p></div></el-col>
        <el-col :span="12"><div class="grid-content bg-purple-light">
          <el-input type="number" v-model="sellAmount" />
        </div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple">
          <el-button @click="sellTokens">SELL</el-button>
        </div></el-col>
      </el-row>


    </div>
  </el-card>
</template>

<script>
import Token from '../contracts/mytoken';
import First from '../contracts/second'
export default {
  data() {
    return {
      currentAccount: null,
      tokenBalance: 0,
      buyAmount: 0,
      sellAmount: 0,
      ethBalance:0,
      tokenContract: null,
      firstmkContract:null,
      yourTokenAmount:0,
      vendorAddress:'0xAe523F875DC4524Bbd335252e54Ac940A45a900e',
    };
  },
  async created() {
    // 获取当前钱包地址
    this.currentAccount = await this.getCurrentAccount();
    // 初始化代币合约实例
    this.tokenContract = new Token();
    this.firstmkContract = new First();
    // 获取当前代币余额和价格
    await this.updateTokenBalance();
    await this.updateEthBalance();
    await this.updateUserTokenBalance();
  },
  methods: {
    async connectWallet() {
      try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        this.currentAccount = await this.getCurrentAccount();
        await this.updateTokenBalance();
        await this.updateEthBalance();
        await this.updateUserTokenBalance();
      } catch (error) {
        console.error(error);
      }
    },
    async getCurrentAccount() {
      const accounts = await window.ethereum.request({ method: 'eth_accounts' });
      return accounts[0];
    },
    async updateUserTokenBalance() {
      if (!this.currentAccount) {
        return;
      }
      const balance = await this.tokenContract.getBalance(this.currentAccount);
      this.yourTokenAmount = balance.toString();
    },

    async updateTokenBalance() {
      if (!this.currentAccount) {
        return;
      }
      const balance = await this.tokenContract.getBalance(this.vendorAddress);
      this.tokenBalance = balance.toString();
    },
    async updateEthBalance() {
      if (!this.currentAccount) {
        return;
      }
      const balance = await this.firstmkContract.getEthBalance();
      this.ethBalance = balance.toString();
    },
    async buyTokens() {
      if (!this.currentAccount) {
        return;
      }
      const get = await this.firstmkContract.buyTokens(this.currentAccount, this.buyAmount);
      await this.updateTokenBalance();
      await this.updateEthBalance();
      await this.updateUserTokenBalance();

    },
    async sellTokens() {
      if (!this.currentAccount) {
        return;
      }
      await this.firstmkContract.sellTokens(this.currentAccount, this.sellAmount);
      await this.updateTokenBalance();
      await this.updateEthBalance();
      await this.updateUserTokenBalance();
    },
  },
};
</script>
