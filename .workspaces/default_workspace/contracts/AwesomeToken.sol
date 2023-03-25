// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "./StandardToken.sol";

/**
 * @title Awesome Token
 * @dev Simple ERC20 Token with standard token functions.
 */
contract AwesomeToken is StandardToken {
    string private constant NAME = "RockingToken";
    string private constant SYMBOL = "RKT";

    uint256 private INITIAL_SUPPLY = 80 * 10**decimals();

    /**
     * Token Constructor
     * @dev Create and issue tokens to msg.sender.
     */
    constructor() {
        _name = NAME;
        _symbol = SYMBOL;
        _totalSupply = INITIAL_SUPPLY;
        _balances[msg.sender] = INITIAL_SUPPLY;
    }
}
