from cgitb import text
from email import message
from tkinter import messagebox
from turtle import width
from selenium import webdriver
from tkinter import *
from tkinter import filedialog
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import messagebox
import time



# Contatos/Grupos - Informar o nomes de Grupos ou Contatos
contatos = []


# Mensagem - Mensagem que sera enviada
mensagem = []


# Midia = imagem, pdf, documentos e videos
midia = []

def validarcontato():
    if len (inputcontato.get()) != 0 :
        selecionarcontato()
    else : 
        messagebox.showerror("Error","digite um contato")
        return ()
          

def selecionarcontato():
    contatos.append(inputcontato.get())
    print(contatos)
    inputcontato.delete(0,"end")
    listarcontatos["text"] = ', '.join(contatos)
    
def removercontato():
    contatos.clear()
    print(contatos) 
    listarcontatos ["text"] = ""
    
def validarmensagen():
    if len (inputmensagem.get("1.0","end-1c")) != 0 :
        selecionarmensagem()
    else : 
        messagebox.showerror("Error","digite um mensagem")
        return ()    

def selecionarmensagem():
    mensagem.append(inputmensagem.get("1.0","end-1c"))
    print(mensagem)
    
def removermensagem():
    mensagem.clear()
    print(mensagem)  
    
  
def selecionarimagem():
    imagem=filedialog.askopenfilename(initialdir="/",title="imagem",filetypes=(("imgfiles",["png","jpeg","jpg"]),("all files","*.*")))
    midia.append(imagem)    
    print(midia)
    
def removermidia():
    midia.clear()
    print(midia)    
    
def center(app):
    
    app.update_idletasks()
    width = app.winfo_width()
    frm_width = app.winfo_rootx() - app.winfo_x()
    win_width = width + 3 * frm_width
    height = app.winfo_height()
    titlebar_height = app.winfo_rooty() - app.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = app.winfo_screenwidth() // 3 - win_width // 3
    y = app.winfo_screenheight() // 3 - win_height // 3
    app.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    app.deiconify()
    
    
def validarenvio():
    if len (contatos) != 0 :
        if  len (inputmensagem.get("1.0","end-1c"))!=0 :
            executarbot()
        elif len (midia)!=0 :
            executarbot()
        else : 
            messagebox.showerror("Error","digite uma mensagem")
    else : 
         messagebox.showerror("Error","digite um contato")     



def executarbot():

    # Abre o Chrome
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://web.whatsapp.com/')  # abre o Whatsapp Web
    time.sleep(20)
    
    
    # Funcao que pesquisa o Contato/Grupo
    def buscar_contato(contato):
            campo_pesquisa = driver.find_element(
                By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
            time.sleep(2)
            campo_pesquisa.click()
            campo_pesquisa.send_keys(contato)
            campo_pesquisa.send_keys(Keys.ENTER)

    # Funcao que envia a mensagem
    def enviar_mensagem(mensagem):
        for variasmensagem in mensagem :
            mensagemformatada = variasmensagem.split("\n")
            campo_mensagem = driver.find_element(By.XPATH, '//p[contains(@class,"selectable-text copyable-text")]')
            campo_mensagem.click()
            time.sleep(3)
            for msg in mensagemformatada :                
                campo_mensagem.send_keys(msg)
                campo_mensagem.send_keys(Keys.SHIFT,Keys.ENTER)
            campo_mensagem.send_keys(Keys.ENTER)


    # envia midia como mensagem

    def enviar_midia(midia):
        driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
        attach = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        attach.send_keys(midia)
        time.sleep(3)
        send = driver.find_element(By.XPATH, "//div[contains(@class, '_165_h _2HL9j')]")
        send.click()

    # Percorre todos os contatos/Grupos
    for contato in contatos:
        buscar_contato(contato)
        enviar_mensagem(mensagem)
        enviar_midia(midia)
        time.sleep(2)

app = Tk()
app.title = "botwhats"
center(app)
app.geometry("520x470")


Label(app,text="ChatBot").place(x=10,y=20)
Label(app,text="Digite seu contato:").place(x=10,y=70)
inputcontato = Entry(app)
inputcontato.place(x=120,y=70)
Button(app,text="Adicionar contato", command=validarcontato).place(x=250,y=65)
Button(app,text="Remover contato", command=removercontato).place(x=360,y=65)
Label(app,text="Digite sua mensagem:").place(x=10,y=130)
inputmensagem = Text(app)
inputmensagem.place(x=10,y=160,width=500,height=250)
Button(app,text="Adicionar mensagem",command=validarmensagen).place(x=135,y=130)
Button(app,text="Remover mensagem", command=removermensagem).place(x=265,y=130)
Button(app,text="Adicione sua mídia", command=selecionarimagem).place(x=10,y=420)
Button(app,text="Remover mídia", command=removermidia).place(x=130,y=420)
Button(app,text="Enviar", command=validarenvio).place(x=465,y=420)
listarcontatos = Label (app,text="")
listarcontatos.place (x=10,y=90)
exitpagina = Button (app,text="Exit", command=app.destroy)
exitpagina.place (x=425, y=420)
app.mainloop()