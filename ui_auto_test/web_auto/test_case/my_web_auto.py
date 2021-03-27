from find_place.auto_case import encapsulation_positioning
import time
import allure

class use_case2():

	def __init__(self):
		self.way = encapsulation_positioning()
		self.place1 ='[data-action="login"]'
		# self.place2 ="//*[text()='立即购买']"
		# self.place12 = "[placeholder='请输入手机号码']"

	@allure.step('测试步骤一')
	def excute_use(self):
		self.way.location('css_selector',self.place1).click()
		time.sleep(2)
		# self.way.location('xpath',self.place2).click()
		# self.way.location('css_selector',self.place12).send_keys('hehe')


