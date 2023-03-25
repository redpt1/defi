var Web3 = require("web3");
var web3 = new Web3(new Web3.providers.WebsocketProvider('ws://127.0.0.1:7545'));

var fs = require("fs");
var data = fs.readFileSync("oracle.abi", "utf-8");


var contract = new web3.eth.Contract(JSON.parse(data),'0x16d74cBebCa74D7e08f250B438c543556e6B03B6');


Date.prototype.Format = function(fmt) { //author: meizz
        let o = {
                "M+": this.getMonth() + 1, //月份
                "d+": this.getDate(), //日
                "h+": this.getHours(), //小时
                "m+": this.getMinutes(), //分
                "s+": this.getSeconds(), //秒
                "q+": Math.floor((this.getMonth() + 3) / 3), //季度
                "S": this.getMilliseconds() //毫秒
            };
            if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
            for (let k in o)
                if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (
                    ("00" + o[k]).substr(("" + o[k]).length)));
            return fmt;
}

contract.events.UpdateFTKPrice({
    fromBlock: "latest",
   
}, function(error, event){ /*console.log("result:\n"+JSON.stringify(event)); */})
.on('data', function(event){
    var price = event.raw.data
 
    var time = (new Date()).Format("yyyy-MM-dd hh:mm:ss")


    console.log(parseInt(price,16),time); 
})
.on('changed', function(event){
    // remove event from local database
})
.on('error', console.error);