from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from time import sleep
import unittest
import pathlib
import os

class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        cls.driver = webdriver.Chrome(options=options)
        cls.rootdir = pathlib.Path(__file__).parent.resolve()
        cls.driver.get(f"file:///{cls.rootdir}/sample-exercise_.html")
        print(f"File Path: {cls.rootdir}")
        print(f"Script Name: {os.path.basename(__file__)}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

class TestPageLoad(BaseTest):

    def test_page_load(self):
        title = self.driver.title
        self.assertEqual(title, "Sample page")

class TestGenerateAlert(BaseTest):

    def test_generate_and_check_alert(self):
        try:
            generate_button = self.driver.find_element(By.NAME, "generate")
            generate_button.click()

            WebDriverWait(self.driver, 5).until(
                lambda d: d.find_element(By.ID, "my-value").text != ""
            )

            generated_code = self.driver.find_element(By.ID, "my-value").text
            
            input_field = self.driver.find_element(By.ID, "input")
            input_field.clear()
            input_field.send_keys(generated_code)

            test_button = self.driver.find_element(By.NAME, "button")
            test_button.click()

            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = Alert(self.driver)
            alert_text = alert.text
            self.assertEqual(alert_text, "Done!")
            alert.accept()

            result_message = self.driver.find_element(By.ID, "result").text
            expected_message = f"It workls! {generated_code}!"
            self.assertEqual(result_message, expected_message)
        
        finally:
            sleep(2)

if __name__ == "__main__":
    unittest.main()

