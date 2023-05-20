from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = "/Users/zuzu/Downloads/chromedriver_mac64/chromedriver"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(path,options=options)
driver.maximize_window()
driver.get("https://www.google.com/")
serach = driver.find.element(By.XPATH, '//*[@id="APjFqb"]')
serach.send.keys("Transformers", Keys.ENTER)
