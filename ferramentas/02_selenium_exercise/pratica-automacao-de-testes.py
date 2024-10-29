from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from time import sleep
import unittest
import pathlib

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Prepara o WebDriver
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        cls.driver = webdriver.Chrome(options=options)
        file_path = pathlib.Path(__file__).parent.resolve()
        cls.driver.get(f"file:///{file_path}/sample-exercise_.html")

    def test_page_load(self):
        # Teste Simples pra verificar se a pagina foi aberta corretamente
        title = self.driver.title
        self.assertEqual(title, "Sample page")

    def test_generate_and_check_alert(self):
        try:
            # Clica no botão generate
            generate_button = self.driver.find_element(By.NAME, "generate")
            generate_button.click()

            # Aguarda o código ser gerado
            WebDriverWait(self.driver, 5).until(
                lambda d: d.find_element(By.ID, "my-value").text != ""
            )

            # Pega o Codigo gerado
            generated_code = self.driver.find_element(By.ID, "my-value").text
            
            # Limpa o texto de texto e coloca o codigo gerado
            input_field = self.driver.find_element(By.ID, "input")
            input_field.clear()
            input_field.send_keys(generated_code)

            # Clica no botão Test
            test_button = self.driver.find_element(By.NAME, "button")
            test_button.click()

            # Aguarda o alerta aparecer, verificar se está ok e fecha
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = Alert(self.driver)
            alert_text = alert.text
            self.assertEqual(alert_text, "Done!")
            alert.accept()

            # Verifica se a mensagem está com o código gerado
            result_message = self.driver.find_element(By.ID, "result").text
            expected_message = f"It workls! {generated_code}!"
            self.assertEqual(result_message, expected_message)
        
        finally:
            sleep(2)

    @classmethod
    def tearDownClass(cls):
        # Fecha o Browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
