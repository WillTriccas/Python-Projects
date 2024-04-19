# This code works but cloudflare detects it as hostile and blocks it after a while


from selenium import webdriver
from selenium.webdriver.common.by import By
from twilio.rest import Client
import time

twilio_authtoken = "493ed547f46061609ae87d9ffab9a6a5"
twilio_account = "ACcf96f8355bf5e630fe9230f292232fd8"

twilio_number = "+447862146314"
will_number = "+447717219474"

client = Client(twilio_account, twilio_authtoken)


profile = webdriver.FirefoxProfile('C:\\Users\\You\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\something.default-release')

driver = webdriver.Firefox(executable_path= "/Documents/Learning Python/Projects/Python GPU bot/geckodriver.exe")
driver.get('https://www.scan.co.uk/nvidia/products/3090/s69f85co7dmu3s')

#element = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/div[1]/div[3]/div/div/div[2]/div" )

content = driver.execute_script("return window.getComputedStyle(document.querySelector('.buyButtonNoPrice'),'::after').getPropertyValue('content')")
# the above line of code extracts the 'content' value of the after CSS element that is found in the .buyButtonNoPrice class

print(content)

instock = False

while not instock:

    time.sleep(3)

    if "OUT OF STOCK" in content.upper():
        print("it is still out of stock!")
        driver.refresh()

    else:
        message = client.messages.create(
        to= will_number,
        from_= twilio_number,
        body= "The Card is now in stock, go to https://www.scan.co.uk/nvidia/products/3090/s69f85co7dmu3s now! ")
        print("it is go time")
        driver.quit()



        


