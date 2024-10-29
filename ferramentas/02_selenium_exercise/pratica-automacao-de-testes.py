from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
import unittest
import pathlib
import os

class TestGenerateAndCheckAlert(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Prepara o WebDriver
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        cls.driver = webdriver.Chrome(options=options)
        cls.rootdir = pathlib.Path(__file__).parent.resolve()
        cls.driver.get(f"file:///{cls.rootdir}/sample-exercise_.html")
        print(f"File Path: {cls.rootdir}")
        print(f"Script Name: {os.path.basename(__file__)}")

    def test_generate_and_check_alert(self):
        self.click_generate_button()
        generated_code = self.wait_for_and_get_generated_code()
        self.enter_generated_code(generated_code)
        self.click_test_button()
        self.check_alert()
        self.verify_result_message(generated_code)

    def click_generate_button(self):
        # Clica no botão generate
        generate_button = self.driver.find_element(By.NAME, "generate")
        generate_button.click()

    def wait_for_and_get_generated_code(self):
        # Aguarda o código ser gerado
        WebDriverWait(self.driver, 5).until(
            lambda d: d.find_element(By.ID, "my-value").text != ""
        )
        # Pega o Codigo gerado
        return self.driver.find_element(By.ID, "my-value").text

    def enter_generated_code(self, code):
        # Limpa o texto de texto e coloca o codigo gerado
        input_field = self.driver.find_element(By.ID, "input")
        input_field.clear()
        input_field.send_keys(code)

    def click_test_button(self):
        # Clica no botão Test
        test_button = self.driver.find_element(By.NAME, "button")
        test_button.click()

    def check_alert(self):
        # Aguarda o alerta aparecer, verificar se está ok e fecha
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = Alert(self.driver)
        alert_text = alert.text
        self.assertEqual(alert_text, "Done!")
        alert.accept()

    def verify_result_message(self, code):
        # Verifica se a mensagem está com o código gerado
        result_message = self.driver.find_element(By.ID, "result").text
        expected_message = f"It workls! {code}!"
        self.assertEqual(result_message, expected_message)

    @classmethod
    def tearDownClass(cls):
        # Fecha o Browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
