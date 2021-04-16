__author__ = '小翟'

import pytest
import allure
from appium import webdriver
from PageObjects.welcome_page import WelcomePage
from PageObjects.index_page import IndexPage
from PageObjects.login_page import LoginPage
from PageObjects.userInfo_page import UserInfoPage
from PageObjects.invest_page import InvestPage
from TestDatas.invest_testdatas import *
from TestDatas.CommonData import *


class TestInvest:


    #投资成功
    @allure.feature("投资模块")
    @allure.story("投资成功")
    @pytest.mark.usefixtures("invest_common_driver")
    def test_invest_success(self, invest_common_driver):
        with allure.step("投资正确的金额"):
            IndexPage(invest_common_driver).click_invest_loan()
            user_left_money_before_invest = InvestPage(invest_common_driver).get_user_left_money()
            InvestPage(invest_common_driver).invest(invest_success_data["money"])
            InvestPage(invest_common_driver).click_confirm()
            InvestPage(invest_common_driver).click_back()
            IndexPage(invest_common_driver).click_invest_loan()
        with allure.step("获取投资余额差"):
            user_left_money_after_invest = InvestPage(invest_common_driver).get_user_left_money()
            invest_money = int(float(user_left_money_before_invest) - float(user_left_money_after_invest))
        with allure.step("比对投资金额"):
            assert invest_success_data["money"] == invest_money


    #投资失败——不输入金额
    @allure.feature("投资模块")
    @allure.story("投资失败：不输入金额")
    @pytest.mark.usefixtures("invest_toast_driver")
    def test_invest_noMoney(self, invest_toast_driver):
        with allure.step("投资不输入金额"):
            IndexPage(invest_toast_driver).click_invest_loan()
            InvestPage(invest_toast_driver).invest(invest_noMoney_data["money"])
        with allure.step("获取提示信息"):
            toast_1_content = InvestPage(invest_toast_driver).get_toast_1_content()
        with allure.step("比对提示信息"):
            assert invest_noMoney_data["check"] == toast_1_content


    #投资失败——输入金额为0
    @allure.feature("投资模块")
    @allure.story("投资失败：输入金额为0")
    @pytest.mark.usefixtures("invest_toast_driver")
    def test_invest_zeroMoney(self, invest_toast_driver):
        with allure.step("投资金额为0"):
            IndexPage(invest_toast_driver).click_invest_loan()
            InvestPage(invest_toast_driver).invest(invest_zeroMoney_data["money"])
        with allure.step("获取提示信息"):
            toast_2_content = InvestPage(invest_toast_driver).get_toast_2_content()
        with allure.step("比对提示信息"):
            assert invest_zeroMoney_data["check"] == toast_2_content


    #投资失败——输入金额不是100的整数倍
    @allure.feature("投资模块")
    @allure.story("投资失败：输入金额非100的倍数")
    @pytest.mark.usefixtures("invest_toast_driver")
    def test_invest_noMulti_money(self, invest_toast_driver):
        with allure.step("投资金额非100的倍数"):
            IndexPage(invest_toast_driver).click_invest_loan()
            InvestPage(invest_toast_driver).invest(invest_noMulti_money_data["money"])
        with allure.step("获取提示信息"):
            toast_3_content = InvestPage(invest_toast_driver).get_toast_3_content()
        with allure.step("比对提示信息"):
            assert invest_noMulti_money_data["check"] == toast_3_content


