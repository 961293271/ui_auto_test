# 设备启动初始化配置
from appium import webdriver

def init_driver():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'acba8c23（设备号）'
    desired_caps['appPackage'] = '包名'
    desired_caps['appActivity'] = '.activity.StartActivity'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['autoGrantPermissions'] = True
    desired_caps['automationName'] = "uiautomator2"
    # 是否初始化app，True为不初始化，False为初始化
    desired_caps['noReset'] = True
    #键盘功能点击搜索
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True


    driver = webdriver.Remote('http://127.0.1.1:4723/wd/hub', desired_caps)
    return driver