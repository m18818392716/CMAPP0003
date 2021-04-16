__author__ = '小翟'

import os

cur_dir = os.path.split(os.path.abspath(__file__))[0]
print(cur_dir)
htmlreports_dir = cur_dir.replace("Common", "HtmlTestReports")
print(htmlreports_dir)