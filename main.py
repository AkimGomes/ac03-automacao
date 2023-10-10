from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()

navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

endereco = navegador.find_element(By.NAME, "endereco")
endereco.send_keys("02317100")

buscar = navegador.find_element(By.XPATH, "//button[text()='Buscar']")
buscar.click()

time.sleep(3)

tabela = navegador.find_element(By.ID, "resultado-DNEC")

endereco = tabela.find_element(By.XPATH, ".//tbody/tr[1]/td[1]").text
bairro = tabela.find_element(By.XPATH, ".//tbody/tr[1]/td[2]").text
cidade = tabela.find_element(By.XPATH, ".//tbody/tr[1]/td[3]").text

print("Endereço:", endereco)
print("Bairro:", bairro)
print("Cidade:", cidade)

navegador.quit()
