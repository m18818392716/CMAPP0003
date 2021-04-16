import subprocess

__author__ = '小翟'

import pytest
import time
from Common.conf_dir import htmlreports_dir

import time
def invoke(md):
    output, errors = subprocess.Popen(md, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8")
    return o


curTime = time.strftime("%Y-%m-%d_%H-%M-%S")
# pytest.main(["-m", "smoke",
#              "-s", "-q",
#              "--alluredir", htmlreports_dir + "/APP_AutoTest_Reports_{0}_xml".format(curTime)])

if __name__ == '__main__':

    # pytest.main(["-s", "-q", "./TestCases/test_login.py",
    #              "--alluredir", htmlreports_dir + "/APP_AutoTest_Reports_{0}_xml".format(curTime)])
    pytest.main(["-s", "-q", "./TestCases/test_login.py",
                 "--alluredir", htmlreports_dir + "/xml"])
    cmd = 'allure generate %s -o %s --clean' % ((htmlreports_dir + '/xml'), (htmlreports_dir + '/html'))
    invoke(cmd)