# import os
#
# import yaml
# from appium import webdriver
# class DriverConfig:
#     """
#     公共的base_driver方法
#     参考地址：https://baijiahao.baidu.com/s?id=1643913923729638712&wfr=spider&for=pc
#     参考地址：https://www.cnblogs.com/Simple-Small/p/13856736.html
#
#     """
#     def __init__(self, device_info):
#         self.device_info = device_info
#
#         cmd = 'start appium -p {0} -bp {1} -U 127.0.0.1:{2}'.format(self.device_info["server_port"],
#                                                                     self.device_info["device_port"],
#                                                                     self.device_info["system_port"])
#         os.system(cmd)
#
#     def get_base_driver(self, automatioName="appium", noReset=False):
#         '''
#         返回公共的driver
#         :param automatioName: 引擎名字
#         :param noReset: 是否重置
#         :return: driver对象
#         '''
#         fs = open("../Caps/desire_caps.yaml", encoding="utf-8")
#         desired_caps = yaml.load(fs, Loader=yaml.FullLoader)
#         desired_caps['platformVersion'] = self.device_info['platformVersion']
#         desired_caps['deviceName'] = "127.0.0.1:{}".format(self.device_info['device_port'])
#         desired_caps['platformVersion'] = self.device_info['platformVersion']
#
#         if automatioName != "appium":
#             desired_caps["automationName"] = automatioName
#         if noReset == True:
#             desired_caps['noReset'] = noReset
#         driver = webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(self.device_info['server_port']), desired_caps)
