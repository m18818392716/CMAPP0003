__author__ = '小翟'

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from PageObjects.BasePage import BasePage
import time


class WelcomePage(BasePage):

    #元素定位
    experience_now_id = "com.xxzb.fenwoo:id/btn_start"

    #滑屏
    def swipe_screen(self):
        #等待2s
        time.sleep(2)
        #获取屏幕尺寸
        size = self.driver.get_window_size()
        for i in range(3):
            #向左滑动
            #swipe还有一个参数duration，单位是ms，防止操作过快
            #等待2s
            self.swipe(size)
        #等待立即提现可见
        #定位并点击立即提现
        self.get_element(self.experience_now_id).click()



