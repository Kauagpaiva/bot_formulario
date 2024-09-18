## Bot para preencher o formulário da Redbull

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

# dados fixos
URL_DO_FORM = "https://www.redbull.com/br-pt/events/red-bull-basement-brazil"
FORMULARIO_UNIVERSIDADE = "ufrj"
FORMULARIO_CIDADE = "Rio"

#Atualizar com os dados que você preencheria no formulario
formulario_nome = 'nome'
formulario_sobrenome = "sobrenome"
formulario_email = "email@email.com"
formulario_telefone = "5521999999999"




#loop de teste dps só trocar por um while True
while True:
    try:
        # Cria uma instancia do navegador chrome
        chrome = webdriver.Chrome()
        
        #Acessa uma url no chrome
        chrome.get(URL_DO_FORM)

        # Encontrando botão na página
        botao_coockie = chrome.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        sleep(1)
        #clica no botão
        botao_coockie.click()
        sleep(1)


        # Repete o processo
        botao_participe = chrome.find_element(By.XPATH,'//*[@id="page-main"]/div/div[6]/div/cosmos-mode-8-3-8/div/div[3]/div/div/cosmos-button-8-3-8')
        botao_participe.click()
        sleep(1)

        #pagina 1
        botao_inscrevasse = chrome.find_element(By.XPATH, '//*[@id="page-main"]/div/div[10]/div/div/cosmos-mode-7-14-0/div[2]/div/div[2]/div/div[2]/cosmos-button-7-14-0[1]')
        sleep(1)
        botao_inscrevasse.click()
        sleep(5)

        # pagina 2
        botao_quer_ajuda = chrome.find_element(By.XPATH, '//*[@id="page-main"]/div/div[10]/div/div/cosmos-mode-7-14-0/div[2]/div/div[2]/div/div[2]/div/cosmos-button-7-14-0[2]')
        sleep(1)
        botao_quer_ajuda.click()
        sleep(1)

        # pagina 3
        botao_casas_inteligentes = chrome.find_element(By.XPATH, '//*[@id="page-main"]/div/div[10]/div/div/cosmos-mode-7-14-0/div[2]/div/div[2]/div/div[1]/div/div/div[4]')
        sleep(1)
        botao_casas_inteligentes.click()
        sleep(1)
        botao_proximo = chrome.find_element(By.XPATH, '//*[@id="page-main"]/div/div[10]/div/div/cosmos-mode-7-14-0/div[2]/div/div[2]/div/div[2]/div/cosmos-button-7-14-0')
        sleep(1)
        botao_proximo.click()
        sleep(1)

        # pagina 4
        botao_esportes_e_lazer = chrome.find_element(By.XPATH, '//*[@id="page-main"]/div/div[10]/div/div/cosmos-mode-7-14-0/div[2]/div/div[2]/div/div[1]/div/div/div[5]')
        sleep(1)
        botao_esportes_e_lazer.click()
        sleep(1)
        botao_proximo = chrome.find_element(By.XPATH, '//*[@id="page-main"]/div/div[10]/div/div/cosmos-mode-7-14-0/div[2]/div/div[2]/div/div[2]/div/cosmos-button-7-14-0[2]')
        sleep(1)
        botao_proximo.click()
        sleep(1)


        # pagina 5
        botao_inovar_com_tecnologia = chrome.find_element(By.XPATH, '//*[@id="page-main"]/div/div[10]/div/div/cosmos-mode-7-14-0/div[2]/div/div[2]/div/div[1]/div/div/div[2]')
        sleep(1)
        botao_inovar_com_tecnologia.click()
        sleep(2)
        botao_proximo = chrome.find_element(By.XPATH, '//*[@id="page-main"]/div/div[10]/div/div/cosmos-mode-7-14-0/div[2]/div/div[2]/div/div[2]/div/cosmos-button-7-14-0[2]')
        sleep(1)
        botao_proximo.click()
        sleep(10)

        # pagina 6
        ultima_resposta = chrome.find_element(By.XPATH, '//*[@id="page-main"]/div/div[10]/div/div/cosmos-mode-7-14-0/div[2]/div/div[2]/div/div[1]/div/div/div[3]/cosmos-text-7-14-0')
        sleep(1)
        ultima_resposta.click()
        sleep(1)
        botao_proximo = chrome.find_element(By.XPATH, '//*[@id="page-main"]/div/div[10]/div/div/cosmos-mode-7-14-0/div[2]/div/div[2]/div/div[2]/div/cosmos-button-7-14-0[2]')
        sleep(1)
        botao_proximo.click()
        sleep(10)

        # pagina 7
        penultima_resposta = chrome.find_element(By.XPATH, '//*[@id="page-main"]/div/div[10]/div/div/cosmos-mode-7-14-0/div[2]/div/div[2]/div/div[1]/div/div/div[2]/cosmos-text-7-14-0')
        sleep(1)
        penultima_resposta.click()
        sleep(1)
        botao_proximo = chrome.find_element(By.XPATH, '//*[@id="page-main"]/div/div[10]/div/div/cosmos-mode-7-14-0/div[2]/div/div[2]/div/div[2]/div/cosmos-button-7-14-0[2]')
        sleep(1)
        botao_proximo.click()
        sleep(10)

        # pagina 8
        sem_imagem = chrome.find_element(By.XPATH, '//*[@id="page-main"]/div/div[10]/div/div/cosmos-mode-7-14-0/div[2]/div/div[2]/div/div[1]/div/div[7]/div[2]/div[2]/cosmos-button-7-14-0')
        sleep(1)
        sem_imagem.click()
        sleep(2)
        pre_view = chrome.find_element(By.XPATH, '//*[@id="page-main"]/div/div[10]/div/div/cosmos-mode-7-14-0/div[2]/div/div[2]/div/div[2]/cosmos-button-7-14-0')
        sleep(1)
        pre_view.click()
        sleep(10)

        # pagina 9
        enviar = chrome.find_element(By.XPATH, '//*[@id="preview-container"]/div[2]/div[3]/cosmos-button-7-14-0[1]')
        sleep(1)
        enviar.click()
        sleep(15)

        # pagina formulario

        # nome
        pyautogui.click(431,621,duration=0.5) #move o mouse ate as coordenadas do campo e clica nele
        pyautogui.write(formulario_nome) # escreve o nome no formulario

        # sobrenome
        pyautogui.click(839,619,duration=0.5)
        pyautogui.write(formulario_sobrenome)

        # email
        pyautogui.click(643,833,duration=0.5)
        pyautogui.write(formulario_email)

        # desce a página
        pyautogui.scroll(-200)

        #telefone
        pyautogui.click(640,794, duration=0.5)
        pyautogui.write(formulario_telefone)

        pyautogui.scroll(-200)

        #universidade 
        pyautogui.click(613,771,duration=1) #selecionar o campo
        pyautogui.write(FORMULARIO_UNIVERSIDADE)
        pyautogui.click(316,812,duration=1) #selecionar ufrj

        #cidade
        pyautogui.click(622,931,duration=1) #selecionar o campo
        pyautogui.write(FORMULARIO_UNIVERSIDADE)
        sleep(1)
        pyautogui.press('enter') #selecionar rio

        #pyautogui.scroll(-200)

        # #estado
        # pyautogui.click(0,0,duration=1) #selecionar o campo
        # pyautogui.write(FORMULARIO_CIDADE)
        # pyautogui.click(0,0,duration=1) #selecionar rio

        # #time
        # pyautogui.click(0,0,duration=1) #selecionar o campo
        # pyautogui.click(0,0,duration=1) #selecionar o tamanho do time

        # #checkbox
        # pyautogui.click(0,0,duration=1) #primeiro check
        # pyautogui.click(0,0,duration=1) #segundo check

        # #submeter
        # pyautogui.click(0,0,duration=1) #submeter
        
        sleep(3)
        # Fecha a janela do chrome
        chrome.quit()


    # caso a tela demore muito para carregar
    except:
        chrome.quit()
