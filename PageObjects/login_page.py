from selenium.webdriver.common.by import By

__author__ = '小翟'

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from PageObjects.BasePage import BasePage
import time

class LoginPage(BasePage):

    #元素定位
    rlMine = ('id', 'com.tnaot.newspro:id/rlMine')
    ivMineSetting = ('id', 'com.tnaot.newspro:id/ivMineSetting')
    rlExit = (By.ID, 'com.tnaot.newspro:id/rlExit')
    button1 = (By.ID, 'android:id/button1')  # 确认 退出
    button2 = (By.ID, 'android:id/button2')  # 取消 退出
    tv_login_btn = (By.ID, 'com.tnaot.newspro:id/tv_login_btn')  # 登录/注册按钮

    tv_main_password_login = (By.ID, 'com.tnaot.newspro:id/tv_main_password_login')  # 密码登录
    tv_main_phone_login = (By.ID, 'com.tnaot.newspro:id/tv_main_phone_login')  # 验证码登录
    tv_main_facebook_login = (By.ID, 'com.tnaot.newspro:id/tv_main_facebook_login')  # 第三方Facebook登录

    ll_password_area_code = (By.ID, 'com.tnaot.newspro:id/ll_password_area_code')  # 区号选择
    china_area = (By.XPATH, "//*[@text='中国']")  # 选择中国
    user = (By.ID, 'com.tnaot.newspro:id/et_password_phone_num')
    pwd = (By.ID, 'com.tnaot.newspro:id/et_phone_password')
    button = (By.ID, 'com.tnaot.newspro:id/ibtn_password_login')

    rlHome = (By.ID, 'com.tnaot.newspro:id/rlHome')  # 点击首页Tab
    iv_top_search = (By.ID, 'com.tnaot.newspro:id/iv_top_search')  # 点击搜索按钮
    et_search_keywords = (By.ID, 'com.tnaot.newspro:id/et_search_keywords')  # 输入搜索内容


    #输入手机号
    def input_phoneNumber(self, phoneNumber):
        #等待手机号输入框可见
        time.sleep(10)
        # 点击我的
        self.get_element(self.rlMine).click()
        time.sleep(5)
        # 点击登录注册入口
        self.get_element(self.tv_login_btn).click()
        # 选择手机号密码登录
        self.get_element(self.tv_main_password_login).click()
        # 选择区号
        self.get_element(self.ll_password_area_code).click()
        # 选择中国
        self.get_element(self.china_area).click()
        time.sleep(1)
        #输入手机号
        self.get_element(self.user).send_keys(phoneNumber)


    #输入密码
    def input_passwd(self, passwd):
        #等待密码输入框可见
        #输入密码
        self.get_element(self.pwd).send_keys(passwd)
        #点击登录
        self.get_element(self.button).click()
        time.sleep(2)


    # #获取无效的手机号提示信息
    # def get_invalid_phoneNumber_content(self):
    #     #等待提示信息可见
    #     #获取提示信息
    #     invalid_phoneNumber_content = self.get_element(self.button).text
    #     return invalid_phoneNumber_content
    #
    #
    # #获取手机号或密码错误的提示信息
    # def get_phoneNumber_or_passwd_error_content(self):
    #     #等待提示信息可见
    #     #获取提示内容
    #     phoneNumber_or_passwd_error_content = self.get_element(self.button).get_attribute("text")
    #     return phoneNumber_or_passwd_error_content
    #
    #
    # #获取验证码的提示信息
    # def get_verify_shortMessage_toast_content(self):
    #     #等待提示信息存在
    #     #获取提示内容
    #     verify_shortMessage_toast_content = self.get_toast_content(self.button).text
    #     return verify_shortMessage_toast_content



