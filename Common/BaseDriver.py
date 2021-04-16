from time import sleep

__author__ = '小翟'

import yaml
from appium import webdriver

class BaseDriver:


    # def base_driver(self, device, automationName="appium", noReset=True):
    #     # fs = open(r"D:\Program\Jenkins\workspace\APP_AutoTest\appium_AutoTest\Caps\Caps.yaml", encoding="utf-8")
    #     fs = open("./Caps/Caps.yaml", encoding="utf-8")
    #     datas = yaml.load(fs, yaml.FullLoader)
    #     for i in datas:
    #         if device == i["deviceDesc"]:
    #             if automationName != "appium":
    #                 i["desired_caps"]["automationName"] = automationName
    #             if noReset == False:
    #                 i["desired_caps"]["noReset"] = False
    #             desired_caps = i["desired_caps"]
    #             driver = webdriver.Remote("http://{0}:{1}/wd/hub".format(str(i["server_url"]), str(i["server_port"])), desired_caps)
    #             return driver

    def base_driver(self, device, automationName="appium", noReset=False):
        # fs = open(r"D:\Program\Jenkins\workspace\APP_AutoTest\appium_AutoTest\Caps\Caps.yaml", encoding="utf-8")
        fs = open("./Caps/Caps.yaml", encoding="utf-8")
        datas = yaml.load(fs, yaml.FullLoader)
        for i in datas:
            if device == i["deviceDesc"]:
                if automationName != "appium":
                    i["desired_caps"]["automationName"] = automationName
                if noReset == False:
                    i["desired_caps"]["noReset"] = False
                desired_caps = i["desired_caps"]
                driver = webdriver.Remote("http://{0}:{1}/wd/hub".format(str(i["server_url"]), str(i["server_port"])), desired_caps)
                return driver


if __name__ == '__main__':
    # device = ["Honor_5C", "YeShen"]
    device = ["Honor_5C"]
    bd = BaseDriver().base_driver(device[0], automationName="appium", noReset=True)
    print('1111111111')
    print(bd)
    sleep(5)
    # bd.find_element_by_id('com.tnaot.newspro:id/iv_top_search').click()
    bd.find_element_by_id('com.tnaot.newspro:id/rlMine').click()
    bd.quit()