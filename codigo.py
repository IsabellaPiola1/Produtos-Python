# automatiza o teclado e mouse do equipamento utilizado
# são comandos que o computador reconhece, por isso não deve ser escrito de forma diferente 
import pyautogui
import time

pyautogui.PAUSE = 1 # (em segundos, o tempo que vai esperar entre os comandos)

# pyautogui.click -> clicar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever 
# pyautogui.hotkey -> atalho de teclado (ctrl, C) 

# abrir o Google Chrome 
# apertar a tecla win 
pyautogui.press("win")

# digitar o texto chrome
pyautogui.write("chrome")

# apertar enter
pyautogui.press("enter")

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# pedir pro computador esperar 3 segundos (já existia antes do pyautogui) 
time.sleep(3)

# fazer login
pyautogui.click(x=695, y=462)
pyautogui.write("isa.fernandess2@gmail.com")

pyautogui.press("tab") #pasa para o campo da senha 
pyautogui.write("senha123")

pyautogui.press("tab") #passa para o botão logar
pyautogui.press("enter")

# importar a base de dados dos produtos  
# pip install pandas openpyxl
import pandas 

# precisa fazer isso, para armazenar informação 
tabela = pandas.read_csv("produtos.csv")

print(tabela)

time.sleep(2)

# cadastrar um produto 
pyautogui.click(x=657, y=332)

# codigo
pyautogui.write("MOLO0000251")
pyautogui.press("tab")

# marca
pyautogui.write("Logitech")
pyautogui.press("tab")

# tipo
pyautogui.write("Mouse")
pyautogui.press("tab")

# categoria
pyautogui.write("1")
pyautogui.press("tab")

# preco_unitario
pyautogui.write("25.95")
pyautogui.press("tab")

# custo
pyautogui.write("")
pyautogui.press("tab")

# obs

pyautogui.press("enter") # apertar o botão de enviar 

# numero positivo = scroll para cima
# numero negativo = scroll para baixo
pyautogui.scroll() 

# repetir o passo 4 até acabar todos os produtos (fazer com que todos os produtos sejam feitos 
# diretamente sem precisar colocar um por um)

# para selecionar alguém da tabela, coloca []

# tabela com todas as LINHAS (por isso index, captura as linhas), 
# se fosse column capturaria as colunas
for linha in tabela.index: 
    # cadastrar um produto 
    pyautogui.click(x=657, y=332) # clica no primeiro campo

    # codigo
    codigo = tabela.loc[linha, "codigo"] #linha e coluna (tem que ser o valor igual da base de dados)
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"] #linha e coluna (tem que ser o valor igual da base de dados)
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "mouse"] #linha e coluna (tem que ser o valor igual da base de dados)
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"] #linha e coluna (tem que ser o valor igual da base de dados)
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"] #linha e coluna (tem que ser o valor igual da base de dados)
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"] #linha e coluna (tem que ser o valor igual da base de dados)
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"] #linha e coluna (tem que ser o valor igual da base de dados)

    if obs != "nan":
        pyautogui.write(str(obs))

    pyautogui.press("tab")

    pyautogui.press("enter") # apertar o botão de enviar 

    pyautogui.scroll(10000) 

# nan = valor vazio em uma base de dados (Not a number)
# != -> diferente 