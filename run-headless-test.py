from selenium import webdriver
from selenium.webdriver.chrome.options import Options
op = Options()
op.add_argument("--headless")
driver = webdriver.Chrome(options=op)

#if it returns error like "....is not clickable at point", try use these:
op = Options()
op.add_argument("--window-size=1920,1080")
op.add_argument("--start-maximized")
op.add_argument("--headless")
driver = webdriver.Chrome(options=op)
