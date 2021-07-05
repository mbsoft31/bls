import requests
import os
import time
from os import listdir
from os.path import isfile, join

def getCaptcha( waitfor ):
    os.system('rm ./captchas/*')

    time.sleep(waitfor)

    files = [ f for f in listdir('./captchas') if isfile(join('./captchas', f)) ]

    filename = files[0]

    f = open('./captchas/' + filename, "r")
    captcha = f.read()

    return captcha


def getData(captcha):
    f = open('./apptype', 'r')
    line = f.read()
    items = line.split('&')
    data = []
    for item in items:
        [key, value] = item.split('=')
        if key == 'g-recaptcha-response':
            data.append([key, captcha])
        else:
            data.append([key, value])
        
    return data

def main():
    DICT = {
        'app_type': 'Individual', 
        'member': '2',          
        'centre': '38%2338',
        'category': 'Normal',
        'phone_code': '216',
        'phone': '555555555',
        'email': 'bekhouche.mouadh@gmail.com',
        'verification_code': 'demander+le+code+de+v%C3%A9rification',
        'otp': '',
        'g-recaptcha-response': '03AGdBq24966H1EDGMjkcfmPNZFtXZycqqUodBYis9iJ1coNaS775ft9NCWBShcNGFH5b-1PSiX2hBho58BPY52hnUaqheNu59KWe9FAeoZEeVyaUYqqRN1l-Ln1zqAyDePrHxuiT_u4icv4X-YLfPHRqZhvDMS0O1goL3c0lmkwt2EwHJbWkMFjDDvcKkNcA5TQLMaJ89jmKr_ril9Nwgtz5gjTrM374aHAAm1XGhKQASxuETXA5bun9Q094gova6nw1pB6yUX9AvDq5NRDuTtvUSL0OpJNX_BSt0FENgEUqu4OEI75X9rW2vWpK2Oa2q7PedTXxPicx2TznUeib-g4wVkRsYSMYFVGCHHk9DB8CsoLTyToWktKFEcgNJ6l8codnTx2tghHmdZFxTBS5XR3JMZaDg7UnKgY9fWJzU5NrLo7Y0h3fsmEL5XlWnxK136nSNuQyb_UyeXzEv-kJeDfgNGuSPRvPvqw',
        'countryID': '',
    }
    for k in DICT:
        print(f"{k}={DICT[k]}")

    URL = "https://tunisia.blsspainvisa.com/book_appointment.php"

    captcha = getCaptcha(5)

    while captcha == None:
        captcha = getCaptcha(5)

    data = getData(captcha)

    text = ""
    for item in data:
        text += f"{item[0]}={item[1]}&"
    text = text[0:len(text)-1]

    curl_command = f"curl -X POST --data '{text}' {URL}"

    print(curl_command)

    r = requests.post(url=URL, data=text)

    f = open("index.html", "a", encoding="UTF-8")
    f.write(r.text)
    f.close()

    #res = os.system(curl_command)



# print(res)