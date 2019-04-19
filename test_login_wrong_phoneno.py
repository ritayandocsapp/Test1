import json
import requests


api_url = 'https://test.docsapp.in/patientsapp/patient/login/otp'

post_headers = {'Content-Type': 'application/x-www-form-urlencoded'}

post_data = {'phonenumber': '',
             #'otp': '2029',
             'platform': 'abcdef',
             'ime': 'abcdefghiasdasdasd',
             'deviceId': '2312313123123',
             'advertiserId': 'asdasdasdasdasdadasjhdvasjhdhasdba',
             'email': 'deepak.mallah@docsapp.i',
             'gcm': 'askjdnaknkdjnd',
             'version': '3.10.123s',
             'imei': 'asdasdasdasdasdadasjhdvasjhdhasdba'}

post_cookies = {'SESSID': 's%3AmIvl8BcY-okZ-X7xdL9qFEwXCCfDwUr9.0JRV4LDC%2BZuKd3sOZoJZAQ8ygp%2FWI8BhpUBIT%2FMWto8'}


request = requests.post(url=api_url, data=post_data, headers=post_headers, cookies=post_cookies)
results = request.json()
print(json.dumps(results, sort_keys=True, indent=4))
#print(request.status_code)

print('Api responded with Status_code = {}'.format(request.status_code))

if results['success'] == 0:
   print('TestCase Passed')

if results['error'] == 'Invalid phone number':
   print('Login failed as expected because of wrong phone number')

if results['error'] == 'Mobile number missing':
   print('Login failed as expected because of missing phone number')