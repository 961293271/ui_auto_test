#测试创建普通商品并添加库存

from configuration_case.Base import Base
from selenium.webdriver.common.by import By


class Create_common_commodity(Base):

        def __init__(self,driver):

            # 继承定位方法
            Base.__init__(self,driver)
            # 初始化数据
            self.product_name = '测试创建普通商品'
            self.detailed_description = '测试添加商品详细说明，测试9527-0001，凑齐30个字，9527-0001'
            self.price = '1'
            self.swipe_place = (0.5, 0.75, 0.5, 0.25)
            self.maidian_detail = '卖点输入测试，测试9527-0001'

            # 用例数据
            # 发布
            self.find_release = (By.ID, "com.mula.mall:id/main_tab_publish")


        #执行创建
        def execute_create(self):

            # 用例步骤
            self.click_element(self.find_release)




