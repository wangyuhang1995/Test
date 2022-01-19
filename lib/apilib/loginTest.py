# -*- coding:utf-8 -*-
# @author:Jhon
# @software: PyCharm
# @file:loginTest.py
# @time:2022/1/10 14:30
import requests
import hashlib
from configs.config import HOST
#对密码进行加密操作
def get_md5(psw):
    md5 = hashlib.md5() #进行加密实例化
    md5.update(psw.encode('utf-8')) #更新一下md5加密的数据
    return md5.hexdigest() #返回加密数据
class Login:
    def login(self,inData,getToken=True):
        url = f'{HOST}/account/sLogin' #请求地址
        inData['password'] = get_md5(inData['password']) #获取到加密的数据
        payload = inData
        resp = requests.post(url,data=payload)
        if getToken:
            return resp.json()['data']['token']
        else:
            return resp.json()
        print("111")
if __name__ == '__main__':
    print(Login().login({"username":"ma0367","password":"17359"}))