// SPDX-License-Identifier: MIT

pragma solidity ^0.7.3;

contract Token {

  address public owner;
  string public currency;
  string  public last_operation;
  
  address public last_transfer_to;
  uint public total_transfers_amount;
  uint public last_transfer_amount;
  
  uint public total_produce_amount;
  uint public last_produce_amount;
  
  
  

  constructor() {
    owner = msg.sender;
    currency = "Jamaica coin";
    last_operation = "produce";
    
    last_transfer_to = msg.sender;
    total_transfers_amount = 0;
    last_transfer_amount = 0;
    
    total_produce_amount = 0;
    last_produce_amount = 0;
    
    
    
  }


  mapping(address => uint) public balance;

  function produce(uint amount) public {
    require (msg.sender == owner);
    balance[owner] += amount;
    total_produce_amount += amount;
    last_produce_amount = amount;
    last_operation = "produce";
  }

  function transfer(uint amount, address to) public {
    require (balance[msg.sender] >= amount);
    balance[msg.sender] -= amount;
    balance[to] += amount;
    last_transfer_to = to;
    total_transfers_amount += amount;
    last_transfer_amount = amount;
    last_operation = "transfer";

  }
} 
