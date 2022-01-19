# -*- coding:utf-8 -*-
# @author:Jhon
# @software: PyCharm
# @file:conftest.py
# @time:2022/1/11 14:13


#环境初始化操作

import pytest
from lib.apilib.loginTest import Login
from lib.apilib.myshop import MyShop
@pytest.fixture(scope='session',autouse=True)
def start_demo(request):    #这是一个运行该包下任何一个test文件，都会一开始执行的操作
    print('------开始执行自动化------')


    #数据清除操作
    def fin():
        print('------结束执行自动化------')
    request.addfinalizer(fin)


# 数据清楚要手动调用，不能自动调用
@pytest.fixture(scope='function')
def updata_shop_init():
    print('---正在执行数据初始化测试---')
    token = Login().login({"username":"ma0367","password":"17359"})
    #2- 列出商铺--id
    shopId = MyShop(token).shop_list({'page':1,'limit':10})['data']['records'][0]['id']
    #3- 文件上传
    imageInfo = MyShop(token).file_upload('123.png','../data/123.png')
    return shopId,imageInfo