from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys




PATH='D:\cromdrive\chromedriver.exe'

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument("--user-data-dir=/home/username/.config/google-chrome")

driver=webdriver.Chrome(options=chrome_options, executable_path=PATH)


driver.get('https://auth.emag.ro/user/login')
driver.implicitly_wait(5)
find_first_element = driver.find_element_by_id("searchboxTrigger")
find_first_element.send_keys("masca")
find_first_element.submit()

driver.implicitly_wait(10)
mask_finder=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/section[1]/div/div[2]/div/div[3]/div[2]/div[6]/div[3]/div/div/div[1]/div[1]/a/div/img").click()
driver.implicitly_wait(5)
mask_title= driver.find_element_by_class_name("page-title").text
print(mask_title)
pret_finder=driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/section[1]/div/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div/p").text
price = pret_finder
new_price=price.replace("Lei", "")
print(new_price)

driver.implicitly_wait(5)
counter = 0
if int(new_price)== 1799:

    add_to_cos=driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/section[1]/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button[1]")
    add_to_cos.submit()
else:
    add_to_cos = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/section[1]/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button[1]")
    add_to_cos.submit()

    d = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div/span[1]/span[1]/span").click()


    id_finder=driver.find_element_by_id("select2-uit5-container")
    print(id)


    """
    while int(new_price) < 2000 and counter<3  :
        add_to_cos = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/section[1]/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button[1]")
        add_to_cos.submit()
        d= driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div/span[1]/span[1]/span").click()
        print("Price is not equal") """












