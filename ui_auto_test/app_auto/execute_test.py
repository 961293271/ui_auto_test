# 执行用例
from configuration_case.Phone_Init_Driver import init_driver
import pytest
from time import sleep
from ceshi_case.create_common_commodity import Create_common_commodity



class Test_Base():

    # 初始化配置
    def setup_class(self):
        print("start_test")
        self.driver = init_driver()
        # lg = Login(self.driver)
        # lg.chulitanchuang()
        # lg.start_login()

    # 添加测试用例
    def test_putong(self):
        tpt = Create_common_commodity(self.driver)
        tpt.execute_create()



    # 结束配置
    def teardown_class(self):
        sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    # Test_Base().test_search_page()
    pytest.main(['-s', 'execute_test.py'])
