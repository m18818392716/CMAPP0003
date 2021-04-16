__author__ = '小翟'

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver


    #等待元素可见
    def wait_eleVisisble(self, locator, by=By.ID, wait_time=30):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located((by, locator)))


    #等待元素存在
    def wait_elePresence(self, locator, by=MobileBy.ID, wait_time=30):
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((by, locator)))


    #查找并返回一个元素
    def get_element(self, locator):
        # if by not in By.__dict__.values() and by not in MobileBy.__dict__.values():
        #     print("你要找的元素定位不存在！")
        #     raise Exception
        # self.wait_eleVisisble(locator, by, wait_time)
        ele = self.driver.find_element(*locator)
        return ele


    #查找并返回多个元素
    def get_elements(self, locator, by=MobileBy.ID, wait_time=30):
        if by not in By.__dict__.values() and by not in MobileBy.__dict__.values():
            print("你要找的元素定位不存在！")
        eles = self.driver.find_elements(by, locator)
        return eles


    #滑屏
    def swipe(self, size):
        self.driver.swipe(size["width"]*0.9, size["height"]*0.5, size["width"]*0.1, size["height"]*0.5)
        time.sleep(2)


    #获取toast弹出框的文本内容
    def get_toast_content(self, locator, by=MobileBy.XPATH, wait_time=10):
        #等待弹出框存在
        WebDriverWait(self.driver, wait_time, 0.1).until(EC.presence_of_element_located((by, locator)))
        #获取弹出框内容
        toast_content = self.driver.find_element(by, locator)
        return toast_content