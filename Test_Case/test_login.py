# -*- coding:utf-8 -*-
# @author:Jhon
# @software: PyCharm
# @file:test_login.py
# @time:2022/1/10 14:46
from lib.apilib.loginTest import Login
import pytest
from Tools.get_Excel import get_excelData
import allure,os
@allure.epic('外卖系统')
#1- 封装测试类
@allure.feature('登录模块')
class TestLogin:
    #2-数据驱动--装饰器
    @pytest.mark.parametrize('inData,respData',get_excelData('登录模块','Login'))
    def test_login(self,inData,respData):
        #1-调用--封装的模块
        res = Login().login(inData,getToken=False)
        print(res)
        #2- 断言  验证实际结果与预期结果
        assert res['msg'] == respData['msg']


if __name__ == '__main__':
    # -s 输出打印信息  -q  简化输出
    # -- alluredir==../report/temp --生成allure报告需要的源数据
    pytest.main(['test_login.py','-s','--alluredir','../report/tmp'])
    # allure generate---生成报告
    #方案二:allure serve--起服务---自动打开浏览器---一般设置一下默认浏览器
    os.system('allure serve ../report/tmp')