# -*- coding:utf-8 -*-
# @author:Jhon
# @software: PyCharm
# @file:myshop.py
# @time:2022/1/10 15:32
import requests
from configs.config import HOST
from lib.apilib.loginTest import Login
import pprint
class MyShop:
    #1-需要操作的商铺--需要一个token值
    def __init__(self,intoken):
        self.header = {'Authorization':intoken} #请求头

    #2-商铺列表
    def shop_list(self,inData):
        url = f'{HOST}/shopping/myShop'
        payload = inData
        resp = requests.get(url,headers = self.header,params=payload)
        return resp.json()
    #3-文件上传接口
    def file_upload(self,fileName,fileDir): #fileName 文件名  fileDir 文件路径
        userfile = {'file':(fileName,open(fileDir,'rb'),'image/png')}
        resp = requests.post(f'{HOST}/file',files = userfile,headers = self.header)
        return resp.json()['data']['realFileName'] #获取到图片信息


    #4- 编辑商铺   商铺的id，图形信息--实时数据
    def shop_updata(self,inData,shopId,imageInfo):
        url = f'{HOST}/shopping/updatemyshop'
        inData['id'] = shopId #更新店铺ID
        inData['image_path'] = imageInfo #更新图片信息
        inData['image'] = f"{HOST}/file/getImgStream?fileName={imageInfo}"
        payload = inData
        resp = requests.post(url,headers = self.header,data=payload)
        return resp.json()




if __name__ == '__main__':
    #1- 需要登录
    token = Login().login({"username":"ma0367","password":"17359"})
    #2- 列出商铺--id
    res = MyShop(token).shop_list({'page':1,'limit':10})
    id = res['data']['records'][0]['id']
    #3- 文件上传
    res = MyShop(token).file_upload('123.png','../../data/123.png')
    #4-编辑商铺
    pprint.pprint(res)
