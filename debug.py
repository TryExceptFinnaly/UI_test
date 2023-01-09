# import requests
#
# headers = {'Content-type': 'application/json',
#            'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMSwidXNlcm5hbWUiOiJkYXYiLCJleHAiOjE2Njk0MDgwMTAsImVtYWlsIjoiZ2xhZGtpeXZhQGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNjY5MzY0ODEwfQ.jfaPQGjvKN4sMkuAZaqMRPebgBISzYOyHXtdO76t-4M'}
# for i in range(900, 2000):
#     delete_study = requests.delete(f'https://158.160.38.74:8000/api-admin/study/{i}/', verify=False, headers=headers)
#     print(delete_study.text)
#
# from hl7.hl7 import send_hl7_message
#
# for i in range(500):
#     send_hl7_message('sc')

blabla = 'blabla'

print(blabla.split('\n')[0])