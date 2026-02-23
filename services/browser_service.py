from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import config


def iniciar_driver():
    options = Options()

    if config.HEADLESS:
        options.add_argument("--headless=new")

    driver = webdriver.Edge(options=options)
    return driver