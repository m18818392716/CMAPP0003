__author__ = '小翟'

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from PageObjects.BasePage import BasePage
import re
import time

class InvestPage(BasePage):

    #元素定位
    input_invest_money_id = "com.xxzb.fenwoo:id/et_investamount"
    invest_now_id = "com.xxzb.fenwoo:id/btn_investnow"
    invest_success_confirm_id = "com.xxzb.fenwoo:id/btn_confirm"
    back_button_id = "com.xxzb.fenwoo:id/btn_back"
    toast_1_content_xpath = "//*[contains(@text, '请输入')]"
    toast_2_content_xpath = "//*[contains(@text, '最小投资金额为')]"
    toast_3_content_xpath = "//*[contains(@text, '投资金额必须为')]"


    #获取用户可用余额
    def get_user_left_money(self):
        #等待投资输入框可见
        #获取用户可用余额
        user_left_money = re.sub("\D", "", self.get_element(self.input_invest_money_id).text)
        return user_left_money


    #点击投资
    def invest(self, money):
        #等待投资输入框可见
        #输入投资金额
        self.get_element(self.input_invest_money_id).send_keys(money)
        #点击立即投资
        self.get_element(self.invest_now_id).click()


    #点击确定
    def click_confirm(self):
        #等待确定可见
        #点击确定
        self.get_element(self.invest_success_confirm_id).click()


    #点击返回按钮
    def click_back(self):
        #等待返回可见
        #点击返回
        self.get_element(self.back_button_id).click()


    #获取请输入投资金额toast弹出框的内容
    def get_toast_1_content(self):
        #等待弹出框存在
        #获取弹出框内容
        toast_1_content = self.get_toast_content(self.toast_1_content_xpath).text
        return toast_1_content


    #获取最小投资金额toast弹出框的内容
    def get_toast_2_content(self):
        #等待弹出框存在
        #获取弹出框内容
        toast_2_content = self.get_toast_content(self.toast_2_content_xpath).text
        return toast_2_content


    #获取投资金额必须为100整数倍toast弹出框的内容
    def get_toast_3_content(self):
        #等待弹出框存在
        #获取弹出框内容
        toast_3_content = self.get_toast_content(self.toast_3_content_xpath).text
        return toast_3_content