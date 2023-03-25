// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

import "@openzeppelin/contracts@4.8.2/token/ERC20/ERC20.sol";

contract SecondToken is ERC20 {
    constructor() ERC20("SecondToken", "STK") {
        _mint(msg.sender, 10000000 * 10 ** decimals());
    }
}
