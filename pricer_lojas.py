from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

lista_ip = [206,212,214,224,226,227,228,229,230,232,234,235,236]

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

for ip in lista_ip:
    navegador.get(f'http://192.168.7.{ip}:3333/WebInstoreUI/control/login')

    navegador.find_element(By.NAME, "username").send_keys("config")
    navegador.find_element(By.NAME, "password").send_keys("config")

    navegador.find_element(By.NAME, "login").click()

    navegador.find_element(By.ID, "tabAdvanced").click()
    navegador.find_element(By.ID, "esl_stateRoamLink").click()
    time.sleep(2)
    contagem = navegador.find_element(By.XPATH, '//*[@id="workarea"]/div/div[2]/div/div[1]/div[1]').text
    quantidade_etiquetas = int(contagem[26:]) 

    while quantidade_etiquetas > 0:
        navegador.find_element(By.XPATH,'//*[@id="workarea"]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr/td[3]/a').click()
        time.sleep(1)
        navegador.find_element(By.XPATH,'//*[@id="unlinkButton"]').click()
        time.sleep(1)
        navegador.find_element(By.ID,'dialogConfirmButton').click()
        time.sleep(1)
        navegador.find_element(By.ID,'goBackButton').click()
        time.sleep(2)
        contagem = navegador.find_element(By.XPATH, '//*[@id="workarea"]/div/div[2]/div/div[1]/div[1]').text
        quantidade_etiquetas = int(contagem[26:])

    
