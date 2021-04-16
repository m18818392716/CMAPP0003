# 根据设备启动信息，通过pytest.main来收集并执行用例。
import os

import pytest

"""
参考连接地址：http://testingpai.com/article/1595507151237
appium+pytest+allure+jenkins 如何实现多台手机连接
本贴最后更新于 265 天前，其中的信息可能已经渤澥桑田
使用 appium 可以实现 app 自动化测试，我们之前是连接一台手机去运行，如何同时连接多台手机呢？很多人可能想到的是多线程(threading)。
今天分享一种比多线程更简单的方法，虽然不是多台手机同时运行，但可以连接多台手机依次运行，
大致的运行方式是：001 号测试用例：A 手机，B 手机...，002 号测试用例：A 手机，B 手机...

结语
pytest 中 fixture 的参数化虽然能够实现多台手机同时连接，但是运行并不是同时的，
因为 request.param 读取参数列表是遍历读取的，所以造成了一个测试用例，手机 A 先执行，手机 B 后执行(假设 params=["手机 A", "手机 B"])，
要想真正做到多台手机同时运行，就要用到多线程

"""

reports_dir = './allure-report'
def run_cases(device):
    """
    参数：device为设备启动参数。在pytest.main当中，传递给--cmdopt选项。
    """
    print(["-s", "-v", "--cmdopt={}".format(device)])
    reports_path = os.path.join(reports_dir,"test_result_{}_{}.html".format(device["caps"]["deviceName"], device["port"]))
    pytest.main(["-s", "-v",
                 "--cmdopt={}".format(device),
                 "--html={}".format(reports_path)])