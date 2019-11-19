from selenium import webdriver
from selenium.webdriver.chrome.options import Options
op = Options()
op.add_argument("--headless")
driver = webdriver.Chrome(options=op)
