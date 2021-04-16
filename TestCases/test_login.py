from selenium.webdriver.common.by import By

__author__ = '小翟'

import pytest
import allure
from appium import webdriver
from PageObjects.welcome_page import WelcomePage
from PageObjects.index_page import IndexPage
from PageObjects.login_page import LoginPage
from PageObjects.userInfo_page import UserInfoPage
from TestDatas.login_testdatas import *
import re
import time


class TestLogin:

    #登录成功——手机号、密码正确
    @allure.feature("登录模块")
    @allure.story("登录成功")
    @pytest.mark.usefixtures("login_common_driver")
    def test_login_success(self, login_common_driver):
        with allure.step("正常登录"):
            # IndexPage(login_common_driver).click_login()
            print('-------=========================={}'.format(login_common_driver))
            time.sleep(5)
            # rlMine = (By.ID, 'com.tnaot.newspro:id/rlMine')
            print('==================================')
            # login_common_driver.find_element_by_id('com.tnaot.newspro:id/rlMine').click()
            LoginPage(login_common_driver).input_phoneNumber(login_success_data["phoneNumber"])
            LoginPage(login_common_driver).input_passwd(login_success_data["passwd"])
            # IndexPage(login_common_driver).click_later()
        with allure.step("获取昵称"):
            # IndexPage(login_common_driver).click_me()
            nickName = UserInfoPage(login_common_driver).get_nickName()
        with allure.step("比对昵称"):
            assert login_success_data["check"] == nickName


    # #登录失败——手机号为空
    # @allure.feature("登录模块")
    # @allure.story("登录失败：手机号为空")
    # @pytest.mark.usefixtures("login_reset_driver")
    # def test_login_nophoneNumber(self, login_reset_driver):
    #     with allure.step("输入手机号为空"):
    #         IndexPage(login_reset_driver).click_login()
    #         LoginPage(login_reset_driver).input_phoneNumber(login_noPhoneNumber_data["phoneNumber"])
    #     with allure.step("获取提示信息"):
    #         invalid_phoneNumber_content = LoginPage(login_reset_driver).get_invalid_phoneNumber_content()
    #     with allure.step("比对提示信息"):
    #         assert login_noPhoneNumber_data["check"] == invalid_phoneNumber_content
    #
    #
    # #登录失败——密码错误
    # @allure.feature("登录模块")
    # @allure.story("登录失败：密码错误")
    # @pytest.mark.usefixtures("login_reset_driver")
    # def test_login_errorPasswd(self, login_reset_driver):
    #     with allure.step("输入错误密码"):
    #         IndexPage(login_reset_driver).click_login()
    #         LoginPage(login_reset_driver).input_phoneNumber(login_errorPasswd_data["phoneNumber"])
    #         LoginPage(login_reset_driver).input_passwd(login_errorPasswd_data["passwd"])
    #     with allure.step("获取提示信息"):
    #         phoneNumber_or_passwd_error_content = LoginPage(login_reset_driver).get_phoneNumber_or_passwd_error_content()
    #     with allure.step("比对提示信息"):
    #         assert login_errorPasswd_data["check"] == phoneNumber_or_passwd_error_content
    #
    #
    # #登录失败——手机号未注册
    # @allure.feature("登录模块")
    # @allure.story("登录失败：手机号未注册")
    # @pytest.mark.usefixtures("login_toast_reset_driver")
    # def test_login_phoneNumber_noRegister(self, login_toast_reset_driver):
    #     with allure.step("输入未注册的手机号"):
    #         IndexPage(login_toast_reset_driver).click_login()
    #         LoginPage(login_toast_reset_driver).input_phoneNumber(login_phoneNumber_noRegister_data["phoneNumber"])
    #     with allure.step("获取提示信息"):
    #         verify_shortMessage_toast_content = LoginPage(login_toast_reset_driver).get_verify_shortMessage_toast_content()
    #     with allure.step("比对提示信息"):
    #         assert re.search(login_phoneNumber_noRegister_data["check"], verify_shortMessage_toast_content) != None


