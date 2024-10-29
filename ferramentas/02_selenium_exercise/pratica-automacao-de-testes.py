from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pathlib

# Prepara o WebDriver
driver = webdriver.Chrome()
file_path = pathlib.Path(__file__).parent.resolve()
driver.get(f"file:///{file_path}/sample-exercise.html")

# Teste Simples pra verificar se a pagina foi aberta corretamente
title = driver.title
assert title == "Sample page"
time.sleep(1) 

try:
    # Clica no botão generate
    generate_button = driver.find_element(By.NAME, "generate")
    generate_button.click()

    # Aguarda o código ser gerado
    WebDriverWait(driver, 5).until(
        lambda d: d.find_element(By.ID, "my-value").text != ""
    )

    # Pega o Codigo gerado
    generated_code = driver.find_element(By.ID, "my-value").text
    
    time.sleep(1) 

    # Limpa o texto de texto e coloca o codigo gerado
    input_field = driver.find_element(By.ID, "input")
    input_field.clear()
    input_field.send_keys(generated_code)

    # Clica no botão Test
    test_button = driver.find_element(By.NAME, "button")
    test_button.click()

    time.sleep(1) 

    # Aguarda o alerta aparecer, verificar se está ok e fecha
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = Alert(driver)
    alert_text = alert.text
    assert alert_text == "Done!", f"Unexpected alert text: {alert_text}"
    time.sleep(1) 
    alert.accept()

    # Verifica se a mensagem está com o código gerado
    result_message = driver.find_element(By.ID, "result").text
    expected_message = f"It workls! {generated_code}!"
    time.sleep(1) 
    assert result_message == expected_message, f"Unexpected result message: {result_message}"

finally:
    # Fecha o Browser
    time.sleep(2)
    driver.quit()
