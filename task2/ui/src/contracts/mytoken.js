import Web3 from 'web3'
import mytokenABI from './mytokenABI.json'
const web3 = new Web3(window.ethereum);

class MyContract {
  constructor() {
    const contractAddress = '0x9F603d3B60b1E15c18ae6A82d57824A3D8bB4839'
    this.contract = new web3.eth.Contract(mytokenABI, contractAddress);
  }

  async getBalance(accountAddress) {
    const balance = await this.contract.methods.balanceOf(accountAddress).call();
    return balance/(10**18);
  }

  async transfer(toAddress, amount) {
    const accounts = await web3.eth.getAccounts();
    const txHash = await this.contract.methods.transfer(toAddress, amount).send({ from: accounts[0] });
    return txHash;
  }
}

export default MyContract;
