# 封装需要使用的定位方法
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class Base():

    def __init__(self, driver):

        self.driver = driver

    # 初始化定位方法
    def find_element(self, loc, timeout=100):

        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*loc))

    # 点击封装
    def click_element(self, loc):

        self.find_element(loc).click()

    # 输入功能封装
    def input_text(self, loc, text):

        self.find_element(loc).send_keys(text)

    # 封装屏幕位置点击
    def screen_click(self,place):

        # 获取手机分辨率
        el_x = self.driver.get_window_size()['width']
        el_y = self.driver.get_window_size()['height']
        # 坐标区域左上角
        xd_x = (place[0] / el_x) * el_x
        xd_y = (place[1] / el_y) * el_y
        # 坐标区域右下角
        ld_x = (place[2] / el_x) * el_x
        ld_y = (place[3] / el_y) * el_y
        self.driver.tap([(xd_x,xd_y),(ld_x,ld_y)],30)

    # 封装屏幕滑动方法
    def swipe_screen(self,swipe_place):

        # 获取手机分辨率
        el_x = self.driver.get_window_size()['width']
        el_y = self.driver.get_window_size()['height']
        #滑动位置
        self.driver.swipe(el_x*swipe_place[0], el_y*swipe_place[1], el_x*swipe_place[2], el_y*swipe_place[3])

    # 封装长按方法
    def handle_long_press(self,way):
        # 获取手机分辨率
        el_x = self.driver.get_window_size()['width']
        el_y = self.driver.get_window_size()['height']
        # 坐标区域
        xd_x = (way[0] / el_x) * el_x
        xd_y = (way[1] / el_y) * el_y
        TouchAction(self.driver).long_press(x = xd_x, y = xd_y, duration=7000).release().perform()