// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

contract STKPriceOracle {
  
  uint256 public stkPerETH;
 
  // 定义事件
  event UpdateSTKPrice (uint256 _price);
  

  // 预言机回调方法，预言机获取到数据后通过这个方法将数据提交到链上
  function updateSTKPrice (uint256 _price) public {
    stkPerETH = _price;
    emit UpdateSTKPrice(_price);
  }
  function getPrice() public view returns(uint256){
      return stkPerETH;
  }
}