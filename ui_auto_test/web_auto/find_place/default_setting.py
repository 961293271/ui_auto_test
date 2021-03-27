# 默认设置页面（请求信息和配置参数）
from selenium import webdriver
from time import sleep

class default():

    def __init__(self):
        self.url1 = 'https://music.163.com/'
        # 添加请求头
        self.op = [
            'Accept-Language=zh-CN,zh;q=0.9',
            'Connection=keep-alive',
            'User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"',
        ]

    def driver(self):

        self.options = webdriver.ChromeOptions()
        for ops in self.op:
            self.options.add_argument(ops)
            print(ops)

        # 屏蔽浏览器对selenium的检测，可以去掉chrome正受到自动化浏览器的控制
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option(
            'excludeSwitches', ['enable-automation'])
        self.options.add_argument(
            "--disable-blink-features=AutomationControlled")

        # 隐藏图形化界面（不显示浏览器）
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')

        # 添加请求参数
        self.driver = webdriver.Chrome(chrome_options=self.options)

        # 不让网站后台检测是否为自动化软件
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
		    Object.defineProperty(navigator, 'webdriver', {
		      get: () => undefined
		    })
		  """
        })

        self.driver.get(self.url1)
        self.driver.maximize_window()
        return self.driver

# a = default()
# a.driver()