# -*- coding:utf-8 -*-
import unittest
import HTMLTestRunner

# 用例地址
test_dir = r"./testCases"

# discover方法加载多个用例集合
discover = unittest.defaultTestLoader.discover \
    (start_dir=test_dir, pattern="test*.py", top_level_dir=None)

# 测试报告地址
fileName = r"testReport/TestResult.html"
fp = open(fileName, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title=u"TestReport",
                                       description="用例执行情况")
runner.run(discover)
fp.close()