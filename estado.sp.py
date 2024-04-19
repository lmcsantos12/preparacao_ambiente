import json
import requests
import urllib.request
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def acessar_pagina_dinamica(link):
    #definir navegador simulado 
    navegador = webdriver.Chrome (service=ChromeService(ChromeDriverManager().install()))
    # abrir o link no navegador simulado
    navegador.get(link)

    sleep(3)

    caixa_aceiteCookies = navegador.find_element(By.XPATH, "//div[@id=aceiteCookies]").find_element(By.XPATH, "aceiteCookies.btn.btn-toast")
    #clicar na caixa content
    #find_element e find_elements
    caixa_diarios = navegador.find_element(By.XPATH, "//div[@class='content']").find_elements(By.XPATH, "//div[@class='card border-0']")
    print(len(caixa_diarios))
    #print(caixa_diarios)
    sleep(3)
    caixa_diarios[3].find_element(By.CSS_SELECTOR, ".btn-purple").click()
    
    #clicar em download pdf
    #find_element e find_elements
    #download_pdf = navegador.find_element(By.CSS_SELECTOR, "download pdf")
    #clicar no número nas caixas numeradas ao final da página
    #find_element e find_elements
    #caixa_numerada = navegador.find_element(By.CSS_SELECTOR,"número")

def main():
    link = https://www.imprensaoficial.com.br/DO/HomeDO_2_0.aspx#14/04/2024
    acessar_pagina_dinamica(link)
    
    
    
if __name__ == "__main__":
    main()