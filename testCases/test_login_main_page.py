# -*- coding:utf-8 -*-

from common.login_page import login
import unittest


browserName = "Chrome"
url = "http://www.xagxyzdq.com/"

class loginMainPage(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        print('登录主页')
        self.driver = login(browserName, url)

    def test_login_main_page(self):
        '''登录主页测试'''
        try:
            # driver = login(browserName, url)
            # assert_string_in_pagesource
            assert u'西安高新第一中学初中校区东区初级中学' in self.driver.page_source, \
                u"%s not found in title!" % u'西安高新第一中学初中校区东区初级中学'

        except Exception as e:
            raise e

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()