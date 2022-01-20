# -*- coding:utf-8 -*-
# @author:Jhon
# @software: PyCharm
# @file:test_myShop.py
# @time:2022/1/10 15:37
from lib.apilib.myshop import MyShop
from lib.apilib.loginTest import Login
import pytest,os,allure
from Tools.get_Excel import get_excelData
@allure.epic('外卖系统')
@allure.feature('列出商铺')
@pytest.mark.shop
class TestMyShop: #测试类 逻辑关系
    def setup_class(self): #每一个类只执行下面的方法一次
        self.token = Login().login({"username":"ma0367","password":"17359"},getToken=True)
        #定义测试方法
    @allure.story('列出商铺')
    @allure.title('列出商铺用例')

    @pytest.mark.shop_list
    @pytest.mark.parametrize('inData,respData',get_excelData('我的商铺','listshopping'))
    def test_shop_list(self,inData,respData): #列出商铺
        res = MyShop(self.token).shop_list(inData) #商铺列出方法
        print(res)
        if res.get('code') !=None:
            assert res['code'] == respData['code']
        else:
            assert res['error'] == respData['error']


    #2- 测试类--接口方法
    @allure.story('编辑商铺')
    @allure.title('编辑商铺用例')
    @pytest.mark.shop_updata
    @pytest.mark.parametrize('inData,respData', get_excelData('我的商铺','updateshopping'))
    def test_shop_updata(self,inData,respData,updata_shop_init):  # 编辑店铺
        res = MyShop(self.token).shop_updata(inData,updata_shop_init[0],updata_shop_init[1])  # 更新店铺信息
        print('updata_shop_init--->',updata_shop_init[0],updata_shop_init[1])
        assert res['code'] == respData['code']

if __name__ == '__main__':
    for i in os.listdir('../report/tmp'):
        if 'json' in i:
            os.remove(f'../report/tmp/{i}')
    pytest.main(['test_myShop.py','-s','--alluredir','../report/tmp'])
    os.system('allure serve ../report/tmp')
    print('.....')
