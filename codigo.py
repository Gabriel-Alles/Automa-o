import pyautogui
import time
import pandas  # Importação movida para o topo

pyautogui.PAUSE = 0.5

# Função para abrir o Chrome
pyautogui.press("Win")
pyautogui.write("Chrome")
pyautogui.press("Enter")

# Função para digitar o site
pyautogui.write(
    "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
)
pyautogui.press("Enter")

# Função para esperar o site carregar
time.sleep(3)

# Fazer o login
pyautogui.click(x=717, y=409)
pyautogui.write("email.aleatorio@outlook.com")

# Preencher senha
pyautogui.press("Tab")
pyautogui.write("SenhaAleatoria")

# Botão logar
pyautogui.press("Tab")
pyautogui.press("Enter")

# Função para esperar 3 segundos para caso o site demore a carregar
time.sleep(3)

# Passo 3: Importar a base de dados
# Caminho corrigido para string literal
tabela = pandas.read_csv(r"C:\Projetos\Automacao\produtos.csv")

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:  # para cada linha da minha tabela repita o processo abaixo
    pyautogui.click(x=768, y=287)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("Tab")  # passar para o próximo campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("Tab")  # passar para o próximo campo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("Tab")  # passar para o próximo campo
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("Tab")  # passar para o próximo campo
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("Tab")  # passar para o próximo campo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("Tab")  # passar para o próximo campo
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("Tab")  # passar para o próximo campo
    pyautogui.press("Enter")

    pyautogui.scroll(10000)

# Passo 5: Repetir para todos os produtos colocando ele dentro do laço de repetição FOR
