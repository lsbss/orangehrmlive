from selenium import webdriver


class PageObject:

    def __init__(self, driver):
        self.driver = driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def close(self):
        self.driver.quit()

    def is_url(self, url):
        return self.driver.current_url == url


