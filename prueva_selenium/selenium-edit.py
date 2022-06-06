from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, json

driver =  webdriver.Firefox(executable_path="C:/Software_Empleados/prueva_selenium/driveBrowsers/geckodriver.exe")#line of code to access the browser

with open("edit.json") as json_file:
    data = json.load(json_file)

    for m in data["Employees"]:

        print(m["nombre"] + " is loading!")

        #the line following open the page or project
        driver.get("http://127.0.0.1:5000/") 

        time.sleep(4) 

        intoToedit = driver.find_element_by_name("update")
        intoToedit.click()
        time.sleep(5)

        # userId = driver.find_element_by_name("txtId")
        # userId.clear()
        # userId.send_keys(m["id"])
        # time.sleep(2)

        userName = driver.find_element_by_name("txtName")
        userName.clear()
        userName.send_keys(m["nombre"])
        time.sleep(3)

        userEmail = driver.find_element_by_name("txtEmail")
        userEmail.clear()
        userEmail.send_keys(m["correo"])
        time.sleep(3)


        nextbtnEdit = driver.find_element_by_class_name("lone")
        nextbtnEdit.click()
        time.sleep(2)


        
driver.close() #line of code to close the browser


