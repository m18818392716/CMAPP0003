# from Common.base_driver import DriverConfig
# import pytest
# import time
#
# base_driver = None
#
# def pytest_addoption(parser):
#     parser.addoption("--cmdopt", action="store", default="device_info", help=None)
#
# @pytest.fixture()
# def cmdopt(request):
#     return request.config.getoption("--cmdopt")
#
# @pytest.fixture()
# def common_driver(cmdopt):
#     global base_driver
#     base_driver = DriverConfig(eval(cmdopt))
#     time.sleep(2)
#     driver = base_driver.get_base_driver()
#     driver.close_app()
#     driver.quite()