import pyautogui
import time
import pandas # módulo para manipular base de dados

pyautogui.PAUSE = 1.0

#`pyautogui.click()`→ clicar com o mouse
#`pyautogui.write()`→ escrever um texto
#`pyautogui.press()`→ apertar uma tecla
#`pyautogui.hotkey()`→ combinação de teclas (Ctrl C)
#`pyautogui.scroll()`→ rolar a tela
#`pyautogui.position()`→ indica em que ponto da tela o mouse está

# 1 - entrar no navegador
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

# 2 - entrar no URL desejado
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# intervalo de tempo para dar tempo de acessar o link
time.sleep(2)

# 3 - realizar login
pyautogui.click(x=627, y=490)
pyautogui.hotkey('Ctrl', 'a')
pyautogui.write('pythonimpressionador@gmail.com') # email fictício
pyautogui.press('tab')
pyautogui.write('minha senha') # senha fictícia

# logar no site
pyautogui.click(x=920, y=694) # clique no botao de login
time.sleep(3)

# importar base de dados
tabela = pandas.read_csv('produtos.csv')
print(tabela)

# 4 - cadastrar os produtos do arquivo
for line in tabela.index:
        # codigo
    pyautogui.click(x=714, y=343)
    codigo = str(tabela.loc[line, 'codigo'])
    pyautogui.write(codigo)
        # marca
    pyautogui.press('tab')
    marca = str(tabela.loc[line,'marca'])
    pyautogui.write(marca)
        # tipo
    pyautogui.press('tab')
    tipo = str(tabela.loc[line,'tipo'])
    pyautogui.write(tipo)
        # categoria
    pyautogui.press('tab')
    categoria = str(tabela.loc[line,'categoria'])
    pyautogui.write(categoria)
        # preco unitário
    pyautogui.press('tab')
    preco = str(tabela.loc[line, 'preco_unitario'])
    pyautogui.write(preco)
        # custo
    pyautogui.press('tab')
    custo = str(tabela.loc[line, 'custo'])
    pyautogui.write(custo)
        # observação
    pyautogui.press('tab')
    obs = str(tabela.loc[line, "obs"])
    if obs != 'nan':
        pyautogui.write(obs)

    # clicar em "enviar"
    pyautogui.press('tab')
    pyautogui.press('enter')

    # subir a tela
    pyautogui.scroll(5000)