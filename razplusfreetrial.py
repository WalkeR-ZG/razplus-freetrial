#import libs
import threading
import requests, pyquery

#get Email address from 10 Minutes Mail https://10minutemail.com
mail_url = "https://10minutemail.com"
pq= pyquery.PyQuery(requests.get("https://10minutemail.com").text)
mail_address = pq('#mailAddress').attr("value")
print(mail_address)

#register in raz-plus