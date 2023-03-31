var Web3 = require("web3");
var web3 = new Web3(new Web3.providers.HttpProvider('http://127.0.0.1:7545'));

var fs = require("fs");
var data = fs.readFileSync("oracle-2.abi", "utf-8");


var contract = new web3.eth.Contract(JSON.parse(data),'0x5B5723155D8Ec4bBCb17aC162b4775e3Dfca06F2');


function update(from,price) {
    

    contract.methods.updateSPrice(price).send({from:from},function(err,result){
        if (err) {
            console.log(err)
        }
        console.log(result)
    })
}



var max = 1040
var min = 990
Math.random = function(seed){return ('0.'+Math.cos(seed).toString().substr(6));} //改为cos函数
var result 
var i = 1

let timerId = setInterval(() => {
    result = Math.random(i++)*(max - min) + min
    result = Math.floor(result)
    update("0xE80d399c6A73E94f9D6d10D2d3e2fCFBD0B78eDD",result)
    console.log(result)
}, 10000);


