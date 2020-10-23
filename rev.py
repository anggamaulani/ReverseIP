import requests
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print('')
print('\033[1;36;40m[\033[0;37;40m\033[1;33;40m',current_time,'\033[1;36;40m] ~ [\033[1;33;40m reverse ip \033[1;36;40m]\033[0;37;40m')
WebLuNjing = input('\033[1;36;40m[\033[1;33;40m website \033[1;36;40m]\033[0;37;40m > ')
print('')
url = 'https://hackertarget.com/reverse-ip-lookup/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
dataPayload = {
    'theinput': WebLuNjing,
    'thetest': 'reverseiplookup',
    'name_of_nonce_field': '096fb19351',
    '_wp_http_referer': '/reverse-ip-lookup/'
}
r = requests.post(url, headers=headers, data=dataPayload)
soup = BeautifulSoup(r.text, 'html.parser')
Result_KONTOL = soup.find('pre', id='formResponse').text
print('\033[1;36;40m[\033[0;37;40m\033[1;33;40m',current_time,'\033[1;36;40m] ~ [\033[1;33;40m Resultz \033[1;36;40m]\033[0;37;40m\n')
print(Result_KONTOL)
print('\n\033[1;36;40m[\033[0;37;40m\033[1;33;40m',current_time,'\033[1;36;40m] ~ [\033[1;33;40m End \033[1;36;40m]\033[0;37;40m')
print('')
print('\033[1;36;40m[\033[0;37;40m\033[1;33;40m',current_time,'\033[1;36;40m] ~ [\033[1;33;40m Result Saved On results.txt \033[1;36;40m]\033[0;37;40m\n')
Simpen_Filemek = open('results.txt', 'w')
Simpen_Filemek.write(Result_KONTOL)
