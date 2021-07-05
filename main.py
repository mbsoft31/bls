# importing the requests library
import requests
import json
import os

# api-endpoint
URL = "https://tunisia.blsspainvisa.com/book_appointment.php"

# defining a params dict for the parameters to be sent to the API
PARAMS = {}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

print("AWSALB", r.cookies.get('AWSALB'))
print("AWSALBCORS", r.cookies.get('AWSALBCORS'))

awsalb = r.cookies.get('AWSALB')
awsalbcors = r.cookies.get('AWSALBCORS')

# app_type=Individual&juridiction=14%23Algiers%239&visa_no=&visa_valid_from=&visa_valid_to=&rejected=No&refusal_date=&phone_code=213&phone=782335262&email=mosbahfamily%40gmail.com&verification_code=demander+le+code+de+v%EF%BF%BDrification&otp=&countryID=&tokenvalue=cf79ae6addba60ad018347359bd144d2&g-recaptcha-response=


PARAMS = {
    'app_type': 'Individual',
    'juridiction': '14#Algiers#9',
    'visa_no': '',
    'visa_valid_from': '',
    'visa_valid_to': '',
    'rejected': 'No',
    'refusal_date': '',
    'phone_code': '213',
    'phone': '782335262',
    'email': 'mbsoft31@gmail.com',
    'verification_code': '',
    'otp': '',
    'countryID': '',
    'tokenvalue': 'cf79ae6addba60ad018347359bd144d2',
    'g-recaptcha-response': '',
}

PARAMS=  {
    'center': "35#35",
    'visa_no': '',
    'visa_valid_from': '',
    'visa_valid_to': '',
    'rejected': 'No',
    'refusal_date': '',
    'verification_code': '',
    'otp': '',
    'countryID': '',
    'tokenvalue': 'cf79ae6addba60ad018347359bd144d2',
    'category': 'Normal',
    'app_type': 'Family', # Family, Individual
    'member': 4, # member goes from 2 to 8 range(2,8,1),
    'phone_code': '7',
    'phone': '512121212',
    'email': 'bekhouche.mouadh@gmail.com',
    'verification_code': 'Request+verification+code',
    'g-recaptcha-response':'03AGdBq26j2KAktybrUsCkV2EkbDI4W5Em79A0Bh1BxxQ0j42YsMNRuvG24HhUnvT2eTSw0Lkp8gJsxk5HSw_NDiSR9pG-7hHw-Vv3ZTZSW27xm0Wd3voxW_tBNEpU10wH_WrS5pLhzvPfjRZMblblnCUvDZpCDXxXEE0j4d9hNZcMfKI0eG6qGS7jsqX2yl7EGNuQ96x5XTS1t1fZzvaW9st0FQGca3OKYCpSxJ0jE9pSxEZxVmxx-BLVy0lP56aH0rAtvS2yJlaIHb9Q7hq4xoKqnAxr5_duikkcX_kPVh4FRx6hGTmv3QA_mS8tUtgkGZOvIcbdC_8eheY3FH8uM1NYt3GiaxUeQ08bmCqYemg47e88Qwpn36mFehkKDfl6BU9NW4G3QD_ZXJ7h9V6DfD2JLCl034DIs2Sa37C3idPIA7cWDUZKryFB-8kaFG_wRoy9xC4Us0Tf'
}

r = requests.post(url=URL, data= PARAMS, )

print(r.text)

f = open("index.html", "a", encoding='UTF-8')
f.write(r.text)
f.close()

a = os.system("help")

print(a)