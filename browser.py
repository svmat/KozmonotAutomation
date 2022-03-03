from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Browser:
    """
    This class is wrapper around Selenium driver
    """

    def __init__(self, url, browser_name=""):
        # decide which browser to open, can be extended
        if browser_name.lower() == "firefox":
            self.driver = webdriver.Firefox(executable_path='drivers/geckodriver')
        elif browser_name.lower() == "chrome":
            self.driver = webdriver.Chrome(
                executable_path=r"C:\Users\Aleksei ThinkPad\PycharmProjects\chromedriver.exe")
        elif browser_name.lower() == "remote":
            BROWSERSTACK_URL = 'https://alekseinevzorov_m3a2bh:DU45S7VxjPULprV82GPm@hub-cloud.browserstack.com/wd/hub'
            desired_cap = {
                'os_version': '10',
                'os': 'Windows',
                'browser': 'chrome',
                'browser_version': '93.0',
                'name': 'Kozmonot Test1',  # test name
                'build': 'browserstack-build-1'  # Your tests will be organized within this build
            }
            self.driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)

        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # by default 10, but we can add this like a parameter

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()
