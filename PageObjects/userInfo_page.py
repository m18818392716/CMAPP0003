from selenium.webdriver.common.by import By

__author__ = '小翟'

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from PageObjects.BasePage import BasePage
import time

class UserInfoPage(BasePage):

    #元素定位
    nickName_id = (By.ID, 'com.tnaot.newspro:id/tvUsername')  # 昵称


    #获取昵称
    def get_nickName(self):
        #等待昵称可见
        #获取用户昵称
        nickName = self.get_element(self.nickName_id).text
        return nickName