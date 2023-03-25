// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

contract FTKPriceOracle {
  
  uint256 public ftkPerETH;
 
  // 定义事件
  event UpdateFTKPrice (uint256 _price);
  

  // 预言机回调方法，预言机获取到数据后通过这个方法将数据提交到链上
  function updateFTKPrice (uint256 _price) public {
    ftkPerETH = _price;
    emit UpdateFTKPrice(_price);
  }
  function getPrice() public view returns(uint256){
      return ftkPerETH;
  }
}