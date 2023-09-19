from selenium import webdriver
from selenium.webdriver.common.by import By  # Import the 'By' class
import time
for i in range(2):
  driver=webdriver.Chrome()
  driver.get("https://the-internet.herokuapp.com/login")
#search for RTX 3090
  driver.find_element(By.XPATH, "//input[@id='username'][1]").send_keys('tomsmith')
  driver.find_element(By.XPATH, "//input[@id='password']").send_keys('SuperSecretPassword!')
  driver.find_element(By.CSS_SELECTOR, ".fa.fa-2x.fa-sign-in").click()
  driver.find_element(By.CSS_SELECTOR, ".icon-2x.icon-signout").click()

  # driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]').send_keys('RTX 3090'+(Keys.RETURN))
#scienceisautomation
  time.sleep(3) # 2 seconds

  # Close the browser
  driver.close()
