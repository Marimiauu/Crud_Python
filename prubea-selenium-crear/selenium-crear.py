from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, json

driver =  webdriver.Firefox(executable_path="C:/Users/Sena/Desktop/proyecto-fin/Crud_Python/prubea-selenium-crear/driveBrowsers/geckodriver.exe")

with open("create-example.json") as json_file:
    data = json.load(json_file)

    for p in data["empleados"]:
        print(p["nombre"] + " cargando... ")
        

        driver.get("http://127.0.0.1:5000/")
        time.sleep(3)

        nextBtnCreate = driver.find_element_by_name("crear")
        nextBtnCreate.click()
        time.sleep(4)

        nameFrom = driver.find_element_by_name("txtName")
        nameFrom.send_keys(p["nombre"])

        emailFrom = driver.find_element_by_name("txtEmail")
        emailFrom.send_keys(p["correo"])

        nextBtnSubmit = driver.find_element_by_name("create")
        nextBtnSubmit.click()
        print(" se montaron los datos de  "+p["nombre"])
        time.sleep(4)

driver.close()