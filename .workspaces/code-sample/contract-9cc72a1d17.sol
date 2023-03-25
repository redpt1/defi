// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

import "@openzeppelin/contracts@4.8.2/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts@4.8.2/access/Ownable.sol";

contract FirstToken is ERC20, Ownable {
    constructor() ERC20("FirstToken", "FTK") {
        _mint(msg.sender, 5000000 * 10 ** decimals());
    }
}
