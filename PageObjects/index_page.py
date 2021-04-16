__author__ = '小翟'

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from PageObjects.BasePage import BasePage
import time

class IndexPage(BasePage):

    #元素定位
    register_login_id = "com.xxzb.fenwoo:id/btn_login"
    cancel_gesture_passwd_id = "com.xxzb.fenwoo:id/btn_cancel"
    me_id = "com.xxzb.fenwoo:id/iv_tab"
    invest_loan_id = "com.xxzb.fenwoo:id/pbar_process"


    #点击注册/登录
    def click_login(self):
        self.get_element(self.register_login_id).click()


    #点击以后再说
    def click_later(self):
        #等待以后再说可见
        #点击以后再说
        self.get_element(self.cancel_gesture_passwd_id).click()


    #点击我
    def click_me(self):
        #等待我可见
        #点击我
        self.get_elements(self.me_id)[3].click()


    #点击投标
    def click_invest_loan(self):
        #等待投标可见
        #点击投标
        self.get_element(self.invest_loan_id).click()


