import Web3 from 'web3'
import firstABI from './secondABI.json'
const web3 = new Web3(window.ethereum);

class MyContract {
  contractAddress =  '0xAe523F875DC4524Bbd335252e54Ac940A45a900e';
  constructor() {
    this.contract = new web3.eth.Contract(firstABI, this.contractAddress);
  }

  async getEthBalance() {
    const balance = await web3.eth.getBalance(this.contractAddress)
    return balance/(10**18);
  }
  async buyTokens(address,amount){

    const get = await this.contract.methods.buyTokens().send({from:address,value:amount},(err,result) =>{
        if (err){
          alert(err)
        }
      }
    )
    const ans = parseFloat(get['events']['BuyTokens']['returnValues']['2'])/10**18
    return alert("you get:" + ans.toFixed(18) + " MTK!")
  }
  async sellTokens(address,amount){



    const get = await this.contract.methods.sellTokens(amount).send({from:address},(err,result) =>{
        if (err){
          alert(err)
        }
      }
    )

    const ans = parseFloat(get['events']['SellTokens']['returnValues']['amountOfETH'])/10**18

    return alert("you get:" + ans.toFixed(18) + " ETH!")



  }

}

export default MyContract;
