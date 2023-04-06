// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

contract SecondPriceOracle {
  
  uint256 public tkPerETH;
 
  // 定义事件
  event UpdateSPrice (uint256 _price);
  
  address private _owner;

  constructor() {
      _owner = msg.sender;
  }


  modifier onlyOwner() {
    require( _owner == msg.sender, "Ownership Assertion: Caller of the function is not the owner.");
    _;
  }
  // 预言机回调方法，预言机获取到数据后通过这个方法将数据提交到链上
  function updateSPrice (uint256 _price) public onlyOwner{
    tkPerETH = _price;
    emit UpdateSPrice(_price);
  }
  function getPrice() public view returns(uint256){
      return tkPerETH;
  }
}