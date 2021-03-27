# 执行用例
import pytest
from test_case.my_web_auto import use_case2
import allure

class Test_Base():

    # 初始化配置
    def setup_class(self):
        print('开始测试')

    @allure.step('步骤1')
    def test_wangyiyuns(self):
        st =use_case2()
        st.excute_use()

    def teardown_class(self):
        print('测试结束')


if __name__ == "__main__":
    pytest.main(['-s', 'excute_test.py'])
