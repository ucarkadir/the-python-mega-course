import time 
from datetime import datetime as dt

host_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "outlook.live.com"]

i = 0
while True:
    if dt(dt.now().year,dt.now().month, dt.now().day, 8 ) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print("Working hours...")
        with open(host_temp, 'r+') as file:
            content = file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:  
        i += 1 
        with open(host_temp, 'r+') as file:
            content = file.readlines()
            file.seek()
            for line in content:
                if not any(website in line for website in website_list ):
                    file.write(line)
            file.truncate()
        print("Fun hours..." + str(i)) 
    time.sleep(5)

