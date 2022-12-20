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

before_number = '+79187207439'
after_number = ''

after_number = f'{before_number[0:2]} {before_number[2:5]} {before_number[5:8]}-{before_number[8:10]}-{before_number[10:]}'

print(after_number)