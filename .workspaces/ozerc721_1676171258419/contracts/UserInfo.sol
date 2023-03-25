//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract UserInfo {
       struct User{
            uint8 age;
            string gender;
            string nickname;
            string introduction;
       }
        mapping(address=>User) Info;
        function GetUserInfo(address _target) 
        public
        view
        returns(User memory){
                User memory ans = Info[_target];
                return ans;
        }
        function ChangeUserInfo(address  _target, uint8  _Age, string calldata _Gender, string calldata _Nickname, string calldata _Introduction)
        public
        returns(bool){
                User memory _tar = Info[_target];
                _tar.age = _Age;
                _tar.gender = _Gender;
                _tar.nickname = _Nickname;
                _tar.introduction = _Introduction; 
                Info[_target] = _tar;
                return true;
        }
}