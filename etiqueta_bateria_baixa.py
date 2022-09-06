from selenium import webdriver
import telebot
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

CHAVE_API = "5429364308:AAHMZ4qafLD-UKOSobfsHZ-35fFHeN2nT4k"

bot = telebot.TeleBot(CHAVE_API)

def verificar(message):
    return True

@bot.message_handler(func=verificar)
def responder(message):
    
     if message.text == "6":
        bot.send_message(message.chat.id, "Um minuto, estamos verificando!")

        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        
        
        navegador.get(f'http://192.168.7.206:3333/WebInstoreUI/control/login')

        navegador.find_element(By.NAME, "username").send_keys("config")
        navegador.find_element(By.NAME, "password").send_keys("config")

        navegador.find_element(By.NAME, "login").click()
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="alert0"]/a').click()
        time.sleep(1)
        navegador.find_element(By.ID,"gotoAlertDialogButton").click()
        time.sleep(2)
        contagem = navegador.find_element(By.XPATH,'//*[@id="workarea"]/div/div[2]/div/div[1]/div[1]').text
        quantidade_etiquetas = int(contagem[27:])
        
        bot.send_message(message.chat.id, f' Até o presente momento na Loja 06 há {quantidade_etiquetas} etiquetas com bateria baixa!\n')

     elif message.text == "14":
        bot.send_message(message.chat.id, "Um minuto, estamos verificando!")

        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        
        
        navegador.get(f'http://192.168.7.214:3333/WebInstoreUI/control/login')

        navegador.find_element(By.NAME, "username").send_keys("config")
        navegador.find_element(By.NAME, "password").send_keys("config")

        navegador.find_element(By.NAME, "login").click()
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="alert0"]/a').click()
        time.sleep(1)
        navegador.find_element(By.ID,"gotoAlertDialogButton").click()
        time.sleep(2)
        contagem = navegador.find_element(By.XPATH,'//*[@id="workarea"]/div/div[2]/div/div[1]/div[1]').text
        quantidade_etiquetas = int(contagem[27:])
        
        bot.send_message(message.chat.id, f'Até o presente momento na Loja 14 há {quantidade_etiquetas} etiquetas com bateria baixa!\n')

     elif message.text == "24":
        bot.send_message(message.chat.id, "Um minuto, estamos verificando!")

        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        
        
        navegador.get(f'http://192.168.7.224:3333/WebInstoreUI/control/login')

        navegador.find_element(By.NAME, "username").send_keys("config")
        navegador.find_element(By.NAME, "password").send_keys("config")

        navegador.find_element(By.NAME, "login").click()
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="alert0"]/a').click()
        time.sleep(1)
        navegador.find_element(By.ID,"gotoAlertDialogButton").click()
        time.sleep(2)
        contagem = navegador.find_element(By.XPATH,'//*[@id="workarea"]/div/div[2]/div/div[1]/div[1]').text
        quantidade_etiquetas = int(contagem[27:])
        
        bot.send_message(message.chat.id, f'Até o presente momento na Loja 24 há {quantidade_etiquetas} etiquetas com bateria baixa!\n')

     elif message.text == "26":
        bot.send_message(message.chat.id, "Um minuto, estamos verificando!")

        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        
        
        navegador.get(f'http://192.168.7.226:3333/WebInstoreUI/control/login')

        navegador.find_element(By.NAME, "username").send_keys("config")
        navegador.find_element(By.NAME, "password").send_keys("config")

        navegador.find_element(By.NAME, "login").click()
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="alert0"]/a').click()
        time.sleep(1)
        navegador.find_element(By.ID,"gotoAlertDialogButton").click()
        time.sleep(2)
        contagem = navegador.find_element(By.XPATH,'//*[@id="workarea"]/div/div[2]/div/div[1]/div[1]').text
        quantidade_etiquetas = int(contagem[27:])
        
        bot.send_message(message.chat.id, f' Até o presente momento na Loja 26 há {quantidade_etiquetas} etiquetas com bateria baixa\n')

     elif message.text == "27":
        bot.send_message(message.chat.id, "Um minuto, estamos verificando!")

        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        
        
        navegador.get(f'http://192.168.7.227:3333/WebInstoreUI/control/login')

        navegador.find_element(By.NAME, "username").send_keys("config")
        navegador.find_element(By.NAME, "password").send_keys("config")

        navegador.find_element(By.NAME, "login").click()
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="alert0"]/a').click()
        time.sleep(1)
        navegador.find_element(By.ID,"gotoAlertDialogButton").click()
        time.sleep(2)
        contagem = navegador.find_element(By.XPATH,'//*[@id="workarea"]/div/div[2]/div/div[1]/div[1]').text
        quantidade_etiquetas = int(contagem[27:])
        
        bot.send_message(message.chat.id, f'Até o presente momento na Loja 27 há {quantidade_etiquetas} etiquetas com bateria baixa!\n')

     elif message.text == "28":
        bot.send_message(message.chat.id, "Um minuto, estamos verificando!")

        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        
        
        navegador.get(f'http://192.168.7.228:3333/WebInstoreUI/control/login')

        navegador.find_element(By.NAME, "username").send_keys("config")
        navegador.find_element(By.NAME, "password").send_keys("config")

        navegador.find_element(By.NAME, "login").click()
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="alert0"]/a').click()
        time.sleep(1)
        navegador.find_element(By.ID,"gotoAlertDialogButton").click()
        time.sleep(2)
        contagem = navegador.find_element(By.XPATH,'//*[@id="workarea"]/div/div[2]/div/div[1]/div[1]').text
        quantidade_etiquetas = int(contagem[27:])
        
        bot.send_message(message.chat.id, f'Até o presente momento na Loja 28 há {quantidade_etiquetas} etiquetas com bateria baixa!\n')

     elif message.text == "29":
        bot.send_message(message.chat.id, "Um minuto, estamos verificando!")

        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        
        
        navegador.get(f'http://192.168.7.229:3333/WebInstoreUI/control/login')

        navegador.find_element(By.NAME, "username").send_keys("config")
        navegador.find_element(By.NAME, "password").send_keys("config")

        navegador.find_element(By.NAME, "login").click()
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="alert0"]/a').click()
        time.sleep(1)
        navegador.find_element(By.ID,"gotoAlertDialogButton").click()
        time.sleep(2)
        contagem = navegador.find_element(By.XPATH,'//*[@id="workarea"]/div/div[2]/div/div[1]/div[1]').text
        quantidade_etiquetas = int(contagem[27:])
        
        bot.send_message(message.chat.id, f'Até o presente momento na Loja 29 há {quantidade_etiquetas} etiquetas com bateria baixa!\n')
     
     elif message.text == "30":
        bot.send_message(message.chat.id, "Um minuto, estamos verificando!")

        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        
        
        navegador.get(f'http://192.168.7.230:3333/WebInstoreUI/control/login')

        navegador.find_element(By.NAME, "username").send_keys("config")
        navegador.find_element(By.NAME, "password").send_keys("config")

        navegador.find_element(By.NAME, "login").click()
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="alert0"]/a').click()
        time.sleep(1)
        navegador.find_element(By.ID,"gotoAlertDialogButton").click()
        time.sleep(2)
        contagem = navegador.find_element(By.XPATH,'//*[@id="workarea"]/div/div[2]/div/div[1]/div[1]').text
        quantidade_etiquetas = int(contagem[27:])
        
        bot.send_message(message.chat.id, f'Até o presente momento na Loja 30 há {quantidade_etiquetas} etiquetas com bateria baixa!\n')

     elif message.text == "32":
        bot.send_message(message.chat.id, "Um minuto, estamos verificando!")

        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        
        
        navegador.get(f'http://192.168.7.232:3333/WebInstoreUI/control/login')

        navegador.find_element(By.NAME, "username").send_keys("config")
        navegador.find_element(By.NAME, "password").send_keys("config")

        navegador.find_element(By.NAME, "login").click()
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="alert0"]/a').click()
        time.sleep(1)
        navegador.find_element(By.ID,"gotoAlertDialogButton").click()
        time.sleep(2)
        contagem = navegador.find_element(By.XPATH,'//*[@id="workarea"]/div/div[2]/div/div[1]/div[1]').text
        quantidade_etiquetas = int(contagem[27:])
        
        bot.send_message(message.chat.id, f'Até o presente momento na Loja 32 há {quantidade_etiquetas} etiquetas com bateria baixa!\n')

     elif message.text == "34":
        bot.send_message(message.chat.id, "Um minuto, estamos verificando!")

        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        
        
        navegador.get(f'http://192.168.7.234:3333/WebInstoreUI/control/login')

        navegador.find_element(By.NAME, "username").send_keys("config")
        navegador.find_element(By.NAME, "password").send_keys("config")

        navegador.find_element(By.NAME, "login").click()
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="alert0"]/a').click()
        time.sleep(1)
        navegador.find_element(By.ID,"gotoAlertDialogButton").click()
        time.sleep(2)
        contagem = navegador.find_element(By.XPATH,'//*[@id="workarea"]/div/div[2]/div/div[1]/div[1]').text
        quantidade_etiquetas = int(contagem[27:])
        
        bot.send_message(message.chat.id, f'Até o presente momento na Loja 34 há {quantidade_etiquetas} etiquetas com bateria baixa!\n')

     elif message.text == "35":
        bot.send_message(message.chat.id, "Um minuto, estamos verificando!")

        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        
        
        navegador.get(f'http://192.168.7.235:3333/WebInstoreUI/control/login')

        navegador.find_element(By.NAME, "username").send_keys("config")
        navegador.find_element(By.NAME, "password").send_keys("config")

        navegador.find_element(By.NAME, "login").click()
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="alert0"]/a').click()
        time.sleep(1)
        navegador.find_element(By.ID,"gotoAlertDialogButton").click()
        time.sleep(2)
        contagem = navegador.find_element(By.XPATH,'//*[@id="workarea"]/div/div[2]/div/div[1]/div[1]').text
        quantidade_etiquetas = int(contagem[27:])
        
        bot.send_message(message.chat.id, f'Até o presente momento na Loja 35 há {quantidade_etiquetas} etiquetas com bateria baixa!\n')

     elif message.text == "36":
        bot.send_message(message.chat.id, "Um minuto, estamos verificando!")

        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        
        
        navegador.get(f'http://192.168.7.236:3333/WebInstoreUI/control/login')

        navegador.find_element(By.NAME, "username").send_keys("config")
        navegador.find_element(By.NAME, "password").send_keys("config")

        navegador.find_element(By.NAME, "login").click()
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="alert0"]/a').click()
        time.sleep(1)
        navegador.find_element(By.ID,"gotoAlertDialogButton").click()
        time.sleep(2)
        contagem = navegador.find_element(By.XPATH,'//*[@id="workarea"]/div/div[2]/div/div[1]/div[1]').text
        quantidade_etiquetas = int(contagem[27:])
        
        bot.send_message(message.chat.id, f'Até o presente momento na Loja 36 há {quantidade_etiquetas} etiquetas com bateria baixa!\n')

     elif(message.text == "todas") or (message.text == "Todas"):
        bot.send_message(message.chat.id, "Um minuto, estamos verificando!")
        
        lista_ip = [206,212,214,224,226,227,228,229,230,232,234,235,236]

        lista_quantidades = []

        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        
        for ip in lista_ip:
            navegador.get(f'http://192.168.7.{ip}:3333/WebInstoreUI/control/login')

            navegador.find_element(By.NAME, "username").send_keys("config")
            navegador.find_element(By.NAME, "password").send_keys("config")

            navegador.find_element(By.NAME, "login").click()
            time.sleep(2)
            navegador.find_element(By.XPATH,'//*[@id="alert0"]/a').click()
            time.sleep(1)
            navegador.find_element(By.ID,"gotoAlertDialogButton").click()
            time.sleep(2)
            contagem = navegador.find_element(By.XPATH,'//*[@id="workarea"]/div/div[2]/div/div[1]/div[1]').text
            quantidade_etiquetas = int(contagem[27:])
            lista_quantidades.append(quantidade_etiquetas)

            soma = sum(lista_quantidades)

        bot.send_message(message.chat.id, f'Loja 06: {lista_quantidades[0]}\nLoja 12: {lista_quantidades[1]}\nLoja 14: {lista_quantidades[2]}\nLoja 24: {lista_quantidades[3]}\nLoja 26: {lista_quantidades[4]}\nLoja 27: {lista_quantidades[5]}\nLoja 28: {lista_quantidades[6]}\nLoja 29: {lista_quantidades[7]}\nLoja 30: {lista_quantidades[8]}\nLoja 32: {lista_quantidades[9]}\nLoja 34: {lista_quantidades[10]}\nLoja 35: {lista_quantidades[11]}\nLoja 36: {lista_quantidades[12]}\n\nTotal: {soma} com bateria baixa.')

     else:
        bot.send_message(message.chat.id, "Loja não encontrada!\nAs Lojas a serem pesquisadas são:\n 6,14,24,26,27,28,29,30,32,34,35,36!\n O comando Todos irá trazer todas as Lojas!")
        '''arquivo = open('etiquetas.txt','w')

        arquivo.write(f'Loja 06:{lista_quantidades[0]}\n')
        arquivo.write(f'Loja 12:{lista_quantidades[1]}\n')
        arquivo.write(f'Loja 14:{lista_quantidades[2]}\n')
        arquivo.write(f'Loja 24:{lista_quantidades[3]}\n')
        arquivo.write(f'Loja 26:{lista_quantidades[4]}\n')
        arquivo.write(f'Loja 27:{lista_quantidades[5]}\n')
        arquivo.write(f'Loja 28:{lista_quantidades[6]}\n')
        arquivo.write(f'Loja 29:{lista_quantidades[7]}\n')
        arquivo.write(f'Loja 30:{lista_quantidades[8]}\n')
        arquivo.write(f'Loja 32:{lista_quantidades[9]}\n')
        arquivo.write(f'Loja 34:{lista_quantidades[10]}\n')
        arquivo.write(f'Loja 35:{lista_quantidades[11]}\n')
        arquivo.write(f'Loja 36:{lista_quantidades[12]}')

        arquivo.close()'''
bot.polling()