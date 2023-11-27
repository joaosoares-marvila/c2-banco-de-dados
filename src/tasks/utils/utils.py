from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import os

TEMPO_ESPERA = 20

def busca_elemento_XPATH(driver: webdriver, xpath: str) -> WebElement:
    """
    Procura um elemento na página utilizando um seletor XPath.

    Args:
        driver (webdriver): O objeto do driver do Selenium.
        xpath (str): O seletor XPath do elemento a ser procurado.

    Returns:
        WebElement: O elemento encontrado.
    """
    return WebDriverWait(driver, TEMPO_ESPERA).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, xpath)
                    )
                )

def busca_elemento_ID(driver: webdriver, id: str) -> WebElement:
    """
    Procura um elemento na página utilizando um seletor XPath.

    Args:
        driver (webdriver): O objeto do driver do Selenium.
        id (str): O seletor id do elemento a ser procurado.

    Returns:
        WebElement: O elemento encontrado.
    """
    return WebDriverWait(driver, TEMPO_ESPERA).until(
                    EC.visibility_of_element_located(
                        (By.ID, id)
                    )
                )

def busca_elemento_CLASS(driver: webdriver, class_name: str) -> WebElement:
    """
    Procura um elemento na página utilizando um seletor XPath.

    Args:
        driver (webdriver): O objeto do driver do Selenium.
        class_name (str): O seletor XPath do elemento a ser procurado.

    Returns:
        WebElement: O elemento encontrado.
    """
    return WebDriverWait(driver, TEMPO_ESPERA).until(
                    EC.visibility_of_element_located(
                        (By.CLASS_NAME, class_name)
                    )
                )

def formata_preco(preco: str) -> float:
    """
    Formata uma string de preço em um número de ponto flutuante.

    Esta função recebe uma string de preço, remove caracteres indesejados (como 'R$', ',', espaço e nova linha)
    e retorna o preço formatado como um número de ponto flutuante.

    Args:
    - preco (str): Uma string que representa o preço a ser formatado.

    Returns:
    - float: O preço formatado como um número de ponto flutuante.

    Exemplo de uso:
    >>> preco_str = "R$ 10,99\n"
    >>> preco_formatado = formata_preco(preco_str)
    >>> print(preco_formatado)
    10.99
    """
    preco = preco.replace("R$", "").replace(",", ".").replace(" ", "").replace("\n", "")
    preco_formatado = ''
    for caractere in preco:
        if not caractere.isalpha():
            preco_formatado += caractere

    if preco_formatado[-1] == '.':
        preco_formatado = preco_formatado[:-1]

    preco_formatado = float(preco_formatado)

    return preco_formatado
