from selenium import webdriver
from selenium.webdriver.common.by import By

class ForgetPassword():

    def setup(self):
        driver_1 = webdriver.Chrome()
        driver_1.maximize_window()

    def Password_Link(self):
        self.driver_1.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver_1.implicitly_wait(20)
        self.driver_1.find_element(By.XPATH, "//*[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']").click()
        self.driver_1.implicitly_wait(20)
        self.driver_1.find_element(By.NAME, "username").send_keys("Admin")
        self.driver_1.implicitly_wait(20)
        self.driver_1.find_element(By.XPATH, "//*[@type='submit']").click()
        self.driver_1.implicitly_wait(20)
print("Reset password link sent Successfully")
def tearDown(self):
        self.driver_1.quit()

