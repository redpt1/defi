// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

import "./MyToken.sol";
import "./SecondOracle.sol";
// Learn more about the ERC20 implementation 
// on OpenZeppelin docs: https://docs.openzeppelin.com/contracts/4.x/api/access#Ownable
import "@openzeppelin/contracts@4.8.2/access/Ownable.sol";

contract STKVendor is Ownable {

  // Our Token Contract
  MyToken myToken;
  SecondPriceOracle stkOracle;

  // token price for ETH
  uint256 private tokensPerEth;
  uint256 private feeRate;

  // 定义买卖事件
  event BuyTokens(address buyer, uint256 amountOfETH, uint256 amountOfTokens);
  event SellTokens(address seller, uint256 amountOfTokens, uint256 amountOfETH);

  constructor(address tokenAddress, address oracleAddress) {
    //创建 ERC20合约实例
    myToken = MyToken(tokenAddress);
    stkOracle = SecondPriceOracle(oracleAddress);
    tokensPerEth = stkOracle.getPrice();
    feeRate = 3;
  }
  function getTokenPrice() private {
    tokensPerEth = stkOracle.getPrice();
  }
  function getFee(uint256 _amount) public view returns(uint256 fee){
       fee = _amount *  feeRate / 1000;
        return fee;
  }


  /**
  * 购买 Token
  */

  function buyTokens() public payable returns (uint256 tokenAmount) {
    

    //获取价格
    getTokenPrice();

    // 发送的数量必须大于0
    require(msg.value > 0, "Send ETH to buy some tokens");

    
    // 计算后的代币买入数量
    uint256 fee = getFee(msg.value * tokensPerEth);
    uint256 amountToBuy = msg.value * tokensPerEth - fee;

    // 检查合约中的代币是否足够
    uint256 vendorBalance = myToken.balanceOf(address(this));
    require(vendorBalance >= amountToBuy, "Vendor contract has not enough tokens in its balance");

    // 向合约的调用者发送代币 
    (bool sent) = myToken.transfer(msg.sender, amountToBuy);
    require(sent, "Failed to transfer token to user");

    // 注册事件
    emit BuyTokens(msg.sender, msg.value, amountToBuy);

    return amountToBuy;
  }

  /**
  * 卖出 Token
  */
    function sellTokens(uint256 tokenAmountToSell) public {
    getTokenPrice();
    // 检查数量是否大于0
    require(tokenAmountToSell >= 1000, "Specify an amount of token greater than 1000");

    // 检测调用合约者的代币是否足够
    uint256 userBalance = myToken.balanceOf(msg.sender);
    require(userBalance >= tokenAmountToSell, "Your balance is lower than the amount of tokens you want to sell");

    // 检查该合约中的ETH余额是否足够
    uint256 fee = getFee(tokenAmountToSell); 
    uint256 amountOfETHToTransfer = (tokenAmountToSell - fee) / tokensPerEth;
    uint256 ownerETHBalance = address(this).balance;
    require(ownerETHBalance >= amountOfETHToTransfer, "Vendor has not enough funds to accept the sell request");


    //获取权限
    (bool approved) = myToken.approve(address(this), tokenAmountToSell);
    require(approved, "Failed to approve transfer of tokens from user to vendor");


    // 从合约调用者向合约发送代币
    (bool sent) = myToken.transferFrom(msg.sender, address(this), tokenAmountToSell);
    require(sent, "Failed to transfer tokens from user to vendor");

    // 向合约调用者发送eth
    (sent,) = msg.sender.call{value: amountOfETHToTransfer}("");
    require(sent, "Failed to send ETH to the user");

    // 注册事件
    emit SellTokens(msg.sender, tokenAmountToSell, amountOfETHToTransfer);

  }
  function withdraw() public onlyOwner {
    uint256 ownerBalance = address(this).balance;
    require(ownerBalance > 0, "Owner has not balance to withdraw");
    (bool sent,) = msg.sender.call{value: address(this).balance}("");
    require(sent, "Failed to send user balance back to the owner");
  }

  receive() external payable{}
}