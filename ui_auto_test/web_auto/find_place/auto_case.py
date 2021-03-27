# 封装的定位方法
import time
from find_place.default_setting import default
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class encapsulation_positioning():

    def __init__(self):

        self.driver = default().driver()
        # 智能等待时间和重试频率
        self.wait_time = 5
        self.wait_time_frequency = 0.5

    def location(self, way, tag, do=None, value=None):

        print(way,tag)
        time.sleep(1)
        if way == 'id':
            WebDriverWait(self.driver,self.wait_time,self.wait_time_frequency).until(EC.presence_of_element_located((By.ID, tag)),message=('查找元素失败：'+ tag))
            element = self.driver.find_element_by_id(tag)
            if do == 'click':
                element.click()
            elif do == 'input':
                element.send_keys(value)
            elif do == 'move_to_element':
                ActionChains(self.driver).move_to_element(element).perform()
            else:
                return element

        elif way == 'class_name':
            WebDriverWait(self.driver,self.wait_time,self.wait_time_frequency).until(EC.presence_of_element_located((By.CLASS_NAME, tag)),message=('查找元素失败：'+ tag))
            element = self.driver.find_element_by_class_name(tag)
            if do == 'click':
                element.click()
            elif do == 'input':
                element.send_keys(value)
            elif do == 'move_to_element':
                ActionChains(self.driver).move_to_element(element).perform()
            else:
                return element

        elif way == 'name':
            WebDriverWait(self.driver,self.wait_time,self.wait_time_frequency).until(EC.presence_of_element_located((By.NAME, tag)),message=('查找元素失败：'+tag))
            element = self.driver.find_element_by_name(tag)
            if do == 'click':
                element.click()
            elif do == 'input':
                element.send_keys(value)
            elif do == 'move_to_element':
                ActionChains(self.driver).move_to_element(element).perform()
            else:
                return element

        elif way == 'link_text':
            WebDriverWait(self.driver,self.wait_time,self.wait_time_frequency).until(EC.presence_of_element_located((By.LINK_TEXT, tag)),message=('查找元素失败：'+tag))
            element = self.driver.find_element_by_link_text(tag)
            if do == 'click':
                element.click()
            elif do == 'input':
                element.send_keys(value)
            elif do == 'move_to_element':
                ActionChains(self.driver).move_to_element(element).perform()
            else:
                return element

        elif way == 'partial_link_text':
            WebDriverWait(self.driver,self.wait_time,self.wait_time_frequency).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, tag)),message=('查找元素失败：'+tag))
            element = self.driver.find_element_by_partial_link_text(tag)
            if do == 'click':
                element.click()
            elif do == 'input':
                element.send_keys(value)
            elif do == 'move_to_element':
                ActionChains(self.driver).move_to_element(element).perform()
            else:
                return element

        elif way == 'tag_name':
            WebDriverWait(self.driver,self.wait_time,self.wait_time_frequency).until(EC.presence_of_element_located((By.TAG_NAME, tag)),message=('查找元素失败：'+tag))
            element = self.driver.find_element_by_tag_name(tag)
            if do == 'click':
                element.click()
            elif do == 'input':
                element.send_keys(value)
            elif do == 'move_to_element':
                ActionChains(self.driver).move_to_element(element).perform()
            else:
                return element

        elif way == 'xpath':
            WebDriverWait(self.driver,self.wait_time,self.wait_time_frequency).until(EC.presence_of_element_located((By.XPATH, tag)),message=('查找元素失败：'+tag))
            element = self.driver.find_element_by_xpath(tag)
            if do == 'click':
                element.click()
            elif do == 'input':
                element.send_keys(value)
            elif do == 'move_to_element':
                ActionChains(self.driver).move_to_element(element).perform()
            else:
                return element

        elif way == 'css_selector':
            WebDriverWait(self.driver,self.wait_time,self.wait_time_frequency).until(EC.presence_of_element_located((By.CSS_SELECTOR, tag)),message=('查找元素失败：'+tag))
            element = self.driver.find_element_by_css_selector(tag)
            if do == 'click':
                element.click()
            elif do == 'input':
                element.send_keys(value)
            elif do == 'move_to_element':
                ActionChains(self.driver).move_to_element(element).perform()
            else:
                return element
    def drivers(self):
        return self.driver
