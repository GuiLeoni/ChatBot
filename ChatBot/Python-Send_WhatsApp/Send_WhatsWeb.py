from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 
import time

#Abre o Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') #abre o site Whatsapp Web
time.sleep(20) #da um sleep de 15 segundos, tempo para scannear o QRCODE

#Contatos/Grupos - Informar o nome(s) de Grupos ou Contatos que serao enviadas as mensagens
contato1 = ['ChatBot 2'] 
contato2 = []
contato3 = []


#Mensagem - Mensagem que sera enviada
mensagem1 = ['']
mensagem2 = ['']
mensagem3 = ['']

#Midia = imagem, pdf, documento, video (caminho do arquivo, lembrando que mesmo no windows o caminho deve ser passado com barra invertida / ) 
midia1 = "C:/Users/Aluno/Documents/codeSenai.png"
midia2 = ""
midia3 = ""

#Funcao que pesquisa o Contato/Grupo
def buscar_contato(contato):
    campo_pesquisa = driver.find_element(By.XPATH,'//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#Funcao que envia a mensagem
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_element(By.XPATH,'//p[contains(@class,"selectable-text copyable-text")]')
    campo_mensagem.click()
    time.sleep(3)
    campo_mensagem.send_keys((mensagem[0]))
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys((mensagem[1]))
    campo_mensagem.send_keys(Keys.ENTER)


#Funcao que envia midia como mensagem
def enviar_midia(midia):
    driver.find_element(By.CSS_SELECTOR , "span[data-icon='clip']").click()
    attach = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
    attach.send_keys(midia)
    time.sleep(3)
    send = driver.find_element(By.XPATH,"//div[contains(@class, '_165_h _2HL9j')]")
    send.click()   

#Percorre todos os contatos/Grupos e envia as mensagens
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)       
    enviar_midia(midia) 
    time.sleep(2)
