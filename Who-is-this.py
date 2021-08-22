try:
	import requests,threading,phonenumbers
	from phonenumbers import carrier
	from time import sleep
except Exception as e:
	exit(e)
PRNT = threading.Lock()
r=requests.session()
def telegram_vv1ck(*a, **b):
	with PRNT:
		print(*a, **b)
def searched():
	global SNP,TIK,TWR,EML,INS,SCLD,NON,ACP,VIM,NEapi,DARK,eml
	telegram_vv1ck(f"[*] Email : {eml} \n\n{EML}\n{SNP}\n{TWR}\n{TIK}\n{INS}\n{SCLD}\n{NON}\n{ACP}\n{VIM}\n{NEapi}\n{DARK}")
def EMdark():
	global SNP,TIK,TWR,EML,INS,SCLD,NON,ACP,VIM,NEapi,DARK,eml
	try:
		send = r.post('https://secure.darkwebid.com/user/login',headers={'Host': 'secure.darkwebid.com','Cookie': 'has_js=1; _ga=GA1.2.404847453.1629450192; _gid=GA1.2.317407483.1629450192; _gat=1','User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0','Content-Length': '118','Origin': 'https://secure.darkwebid.com','Referer': 'https://secure.darkwebid.com/user/login','Upgrade-Insecure-Requests': '1','Sec-Fetch-User': '?1','Te': 'trailers'},data={
			'name':eml,
			'form_build_id':'form-T8F0Un2cVoe_nvYrXQHIOO176-yBIpuiG46EIOTmhQE',
			'form_id':'user_login','op':'Continue'}).text
		if 'is not recognized as a user name or an e-mail address.'in send:
			DARK = '-[11] Not linked on darkwebid.com ✖️'
			searched()
		else:
			DARK = '-[11] linked on darkwebid.com ☑️'
			searched()
	except:
		DARK = '-[11] search error [darkwebid.com]'
		searched()
telegram_vv1ck("""
 _       ____             _         __  __    _    
| |     / / /_  ____     (_)____   / /_/ /_  (_)____ 
| | /| / / __ \/ __ \   / / ___/  / __/ __ \/ / ___/ ??
| |/ |/ / / / / /_/ /  / (__  )  / /_/ / / / (__  ) ??
|__/|__/_/ /_/\____/  /_/____/   \__/_/ /_/_/____/ ??
               By JOKER @vv1ck
?MODE :
	1) Search for email on websites
	2) Find phone number information
	3) Search for people by their name
	99) EXIT(<\>)
""")
def EMwapi():
	global SNP,TIK,TWR,EML,INS,SCLD,NON,ACP,VIM,NEapi,eml
	try:
		send = r.post('https://newsapi.org/reset-password',headers={
		'Host': 'newsapi.org','Cookie': '_ga=GA1.2.596557937.1629129476; _gid=GA1.2.1573072051.1629129476; _gat_gtag_UA_91285317_5=1','User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0','Origin': 'https://newsapi.org','Referer': 'https://newsapi.org/reset-password'},data={'email':eml})
		if "Please check your email for further instructions,"in send.text:
			NEapi = '-[10] linked on newsapi.com ☑️'
			EMdark()
		elif "We don&#39;t have a registered user with that email address."in send.text:
			NEapi = '-[10] Not linked on newsapi.com ✖️'
			EMdark()
		else:
			NEapi = '-[10] search error [newsapi.com]'
			EMdark()
	except:
		NEapi = '-[10] search error [newsapi.com]'
		EMdark()
def EMvim():
	global SNP,TIK,TWR,EML,INS,SCLD,NON,ACP,VIM,eml
	send = r.post('https://vimeo.com/forgot_password',headers={'Host': 'vimeo.com','Cookie': 'vuid=2139188521.1640766174; OptanonConsent=isIABGlobal=false&datestamp=Fri+Aug+20+2021+08%3A40%3A36+GMT%2B0000+(Coordinated+Universal+Time)&version=6.15.0&hosts=&consentId=bd63d91c-a872-40c0-80e7-39abe84d0f6a&interactionCount=1&landingPath=https%3A%2F%2Fvimeo.com%2Fforgot_password&groups=C0001%3A1%2CC0004%3A1%2CC0003%3A1%2CC0002%3A1; _gcl_au=1.1.1859821931.1628954558; _rdt_uuid=1628954558430.7535fc24-43f4-422d-93e9-6a0baa44e962; _ga=GA1.2.1509050282.1628954559; _pin_unauth=dWlkPU1EWTBabUUyWkdRdFltVmtZeTAwWVRkbExXRmxaVE10TWpsaFl6VTFOekJqWkRFNA; _fbp=fb.1.1628954558941.1830594440; afUserId=501e2ec1-a355-48e9-bcc6-c4dddfdea089-p; AF_SYNC=1628954559966; _uetsid=4a0d4e10019211ec9951b7d194b6c2d4; _uetvid=75945460fd1311eb9eb943defc105f6b; _gid=GA1.2.1070279053.1629448836; _gat_UA-76641-8=1','Origin':'https://vimeo.com','Referer': 'https://vimeo.com/forgot_password','User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.132 Safari/637.36','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Te': 'trailers','Connection': 'close'},data={'email':eml,'token': '5051bb6298fc6a43b44bf7632b89c4f4c8e33f9b.yp67ttqiem.1629448837'})
	if 'We’ve emailed you a link to reset your password.' in send.text:
		VIM = '-[9] linked on vimeo.com ☑️'
		EMwapi()
	elif 'This email was not found in our system'in send.text:
		VIM = '-[9] Not linked on vimeo.com ✖️'
		EMwapi()
	else:
		VIM = '-[9] search error [vimeo.com]'
		EMwapi()
def acaps():
	global SNP,TIK,TWR,EML,INS,SCLD,NON,ACP,eml
	try:
		send = r.post('https://www.acaps.org/user/password',headers={'Host': 'www.acaps.org','Cookie': 'has_js=1; acaps_mode=advanced; _ga=GA1.2.895538350.1628908856; _gid=GA1.2.1525444071.1628908856; _gat_UA-21240261-1=1; cookie-agreed=2','User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0','Referer': 'https://www.acaps.org/user/password'},data={'name': eml,'form_build_id':'form-GmhJBczE4v4RuumvVqBrs4AhCvdrGGNH64mmQDTotlw','form_id':'user_pass','op':'E-mail+new+password'}).text
		if 'is not recognized as a user name or an e-mail address.'in send:
			ACP = '-[8] Not linked on acaps.com ✖️'
			EMvim()
		else:
			ACP = '-[8] linked on acaps.com ☑️'
			EMvim()
	except:
		ACP = '-[8] search error [acaps.com]'
		EMvim()
def EMnon():
	global SNP,TIK,TWR,EML,INS,SCLD,NON,eml
	try:
		send = r.post('https://www.noon.com/_svc/customer-v1/auth/reset_password',headers={'cookie': 'next-i18next=ar-SA; AKA_A2=A; visitor_id=2d18be80-1958-4046-97a1-500742584616; _gcl_au=1.1.1522317105.1628906008; _ga=GA1.2.1536475616.1628906008; _gid=GA1.2.1694949827.1628906008; _gat_UA-84507530-14=1; _scid=f2b8cbdd-be9d-4edf-aed0-4b3fde0b4b9e; _fbp=fb.1.1628906007975.1440438626; nguest=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lJM05HUTRZVE0yTUdWa05XWTBOelV4WVRFNU4ySTNaRGc0TmpGbE9UaGtZeUlzSW1saGRDSTZNVFl5T0Rrd05qQXhNSDAuc0lQM1RDV0kzel9oZnFJY0hsTU5xTExvRGd3Yk1mNmowb1dGY0dmaUZEayIsImlhdCI6MTYyODkwNjAxMH0.68KVlD6GCJZxxPcenzuzfuc0nSkFksM4jFet3g3XMgY; _nsc=nsv1.public.eyJzdGlkIjoiNTFkMDVlZmMtMmYwZi00MmM4LWE3ZWEtMWZkNzY3NDhlNzYyIiwic2lkIjoiNzRkOGEzNjBlZDVmNDc1MWExOTdiN2Q4ODYxZTk4ZGMiLCJpYXQiOjE2Mjg5MDYwMTAsInZpZCI6IjJkMThiZTgwLTE5NTgtNDA0Ni05N2ExLTUwMDc0MjU4NDYxNiIsImhvbWVwYWdlIjp7fX01MW1EY3R5aXYxRlBxbGYzanRyOTZ2dWpjNmFQNVo0QUpDNTZOZWYwVTg0PQ.MQ; _sctr=1|1628899200000; __zlcmid=15ZkFmNm1eIjQ2X; _etc=STrytYJw5RtBDPau; RT="z=1&dm=noon.com&si=le66hf1mcuf&ss=ksb4kyp0&sl=1&tt=1yt&ld=1z4&nu=d41d8cd98f00b204e9800998ecf8427e&cl=4kl"','user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'},json={'email':eml}).text
		if '"message":"ok"'in send:
			NON = '-[7] linked on noon.com ☑️'
			acaps()
		elif '"error":"No user found with that email address"'in send:
			NON = '-[7] Not linked on noon.com ✖️'
			acaps()
		else:
			NON = '-[7] search error [noon.com]'
			acaps()
	except:
		NON = '-[7] search error [noon.com]'
		acaps()
def SCLDE():
	global SNP,TIK,TWR,EML,INS,SCLD,eml
	try:
		aBaDy1337 = requests.post("https://api-mobile.soundcloud.com/users/passwords/reset?client_id=Fiy8xlRI0xJNNGDLbPmGUjTpPRESPx8C",json={"email":eml}).text
		if '{}' in aBaDy1337:
			SCLD = '-[6] linked on soundcloud.com ☑️'
			EMnon()
		elif 'identifier_not_found' in aBaDy1337:
			SCLD = '-[6] Not linked on soundcloud.com ✖️'
			EMnon()
		else:
			SCLD = '-[6] search error [soundcloud.com]'
			EMnon()
	except:
		SCLD = '-[6] search error [soundcloud.com]'
		EMnon()
def EMnsta():
	global SNP,TIK,TWR,EML,INS,eml
	headers = {'cookie':'mid=YQvmcwAEAAFVrBezgjwUhwEQuv3c; ig_did=6C10D114-3B6D-4E5E-9E35-5E808661CBAD; ig_nrcb=1; shbid="13126\05446165248972\0541660151679:01f76272a193b960d6a59109693b94e7ceb63f379a095665f9e6588098e95e4d3c3a7ecc"; shbts="1628615679\05446165248972\0541660151679:01f7c823b2dd58ddaa1efa6ba7df2d6c9c6c69ef00c48655061d874c9143ef8902c6ebd4"; csrftoken=HtWab2HXNN9vlV8mNsL8v1BdVF2Yji5l',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36','x-csrftoken': 'HtWab2HXNN9vlV8mNsL8v1BdVF2Yji5l','x-ig-app-id': '936619743392459','x-ig-www-claim': '0','x-instagram-ajax': '6abd51c369a9','x-requested-with': 'XMLHttpRequest'}
	try:
		send = r.post('https://www.instagram.com/accounts/account_recovery_send_ajax/',headers=headers,data={'email_or_username':eml,'recaptcha_challenge_field': '','flow': '','app_id': '','source_account_id': '',}).text
		if '"status":"ok"' in send:
			INS = '-[5] linked on instagram.com ☑️'
			SCLDE()
		elif 'checkpoint_url"' in send:
			INS = '-[5] There is a captcha instagram.com ✖️'
			SCLDE()
		elif '"message":"No users found"' in send:
			INS = '-[5] Not linked on instagram.com ✖️'
			SCLDE()
		else:
			INS = '-[5] search error [instagram.com]'
			SCLDE()
	except:
		INS = '-[5] search error [instagram.com]'
		SCLDE()
def EMtk():
	global SNP,TIK,TWR,EML,eml
	try:
		send = r.post('https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/?residence=AE&device_id=9488371953858433865&os_version=7.2.0&app_id=1233&iid=6951746276598204161&app_name=musical_ly&pass-route=1&vendor_id=EF3C1478-2AFC-4B8E-8030-C608120AECF9&locale=ar&pass-region=1&ac=WIFI&sys_region=US&ssmix=a&version_code=17.2.0&vid=EF3C1478-2AFC-4B8E-8030-C608120AECF9&channel=App%20Store&op_region=AE&os_api=27&idfa=00000000-0000-0000-0000-000000000000&install_id=6951746276598204161&idfv=EF3C1478-2AFC-4B8E-8030-C608120AECF9&device_platform=iphone&device_type=Pixel&openudid=3ce553bec09070081e5a698d3a14a988f3642ac4&account_region=&tz_name=Asia&tz_offset=12936&app_language=ar&carrier_region=AE&current_region=AE&aid=1233&mcc_mnc=42402&screen_width=1242&uoo=1&content_language=&language=ar&cdid=FBF67CFE-39E1-4556-A3EB-624A20A434E1&build_number=172025&app_version=7.2.0&resolution=2883',headers={'Host': 'api16-normal-c-alisg.tiktokv.com','Connection': 'close','Content-Length': '76','x-Tt-Token': '9ABBszZbHK-ybQ4EmUNmO88d','Content-Type': 'application/x-www-form-urlencoded','x-tt-passport-csrf-token': 'f04fc476081a3d063b607f520e64780c','sdk-version': '2','passport-sdk-version': '7.2.0'},data={'email': eml,'account_sdk_source': 'app','mix_mode': '1','type': '31'})
		
		if '"message":"success"' in send.text:
			TIK = '-[4] linked on tiktok.com ☑️'
			EMnsta()
		elif 'description":"غير مسجل بعد"'in send.text:
			TIK = '-[4] Not linked on tiktok.com ✖️'
			EMnsta()
		else:
			TIK = '-[4] search error [tiktok.com]'
			EMnsta()
	except:
		TIK = '-[4] search error [tiktok.com]'
		EMnsta()
def EMTWR():
	global SNP,TWR,EML,eml
	urTW = "https://twitter.com/users/email_available?email="+eml
	try:
		go = r.get(urTW,headers={
		'Host': 'twitter.com','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36','Cookie': 'personalization_id="v1_6TNKT0FSMkPP7CfzL5Rkfg=="; guest_id=v1%3A159789135703778252; _ga=GA1.2.490437195.1597891367'}).text
		if '"taken":true'in go:
			TWR = '-[3] linked on twitter.com ☑️'
			EMtk()
		elif '"taken":false'in go:
			TWR = '-[3] Not linked on twitter.com ✖️'
			EMtk()
		else:
			TWR = '-[3] search error [twitter.com]'
			EMtk()
	except:
		TWR = '-[3] search error [twitter.com]'
		EMtk()
def EMsn():
	global SNP,EML,eml
	try:
		Send = r.post('https://accounts.snapchat.com/accounts/merlin/login',headers={'Host': 'accounts.snapchat.com','Cookie': 'xsrf_token=aDpeseUJS0ysikB9nhdNzA; _ga=GA1.2.113171992.1627308862; _scid=f8244bc8-117d-45aa-b1b0-f24ab31edabc; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; sc_at=v2|H4sIAAAAAAAAAE3GwRGAMAgEwIqY4cIJxG6MSBUp3m/2teq4YEOlrEuIWpIfSxbD36fB2bFBveEjTDM991H9AatYyihAAAAA; _sctr=1|1627257600000; web_client_id=e64bb4c8-1a1f-4de7-970d-d637c2e9a642','User-Agent': 'Mozilla/5.0 (@vv1ck) Gecko/20100101 Firefox/90.0','X-Xsrf-Token': 'aDpeseUJS0ysikB9nhdNzA','Origin': 'https://accounts.snapchat.com','Connection': 'close'},json={"email":eml,"app":"BITMOJI_APP"})
		if 'hasSnapchat' in Send.text:
			SNP = '-[2] linked on snapchat.com ☑️'
			EMTWR()
		elif Send.status_code == 204:
			SNP = '-[2] Not linked on snapchat.com ✖️'
			EMTWR()
		else:
			SNP = '-[2] search error [snapchat.com]'
			EMTWR()
	except:
		SNP = '-[2] search error [snapchat.com]'
		EMTWR()
def all_Email(domn):
	global EML,eml
	url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + eml + "&_=1604288577990"
	try:
		send = r.get(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36","Host": "odc.officeapps.live.com","Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0","canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c","uaid": "d06e1498e7ed4def9078bd46883f187b","Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"})
		if 'MSAccount' in send.text:
			EML = f'-[1] linked on {domn} ☑️'
			EMsn()
		elif 'Neither' in send.text:
			EML = f'-[1] Not linked on {domn} ✖️'
			EMsn()
		else:
			EML = f'-[1] search error [{domn}]'
			EMsn()
	except:
		EML = f'-[1] search error [{domn}]'
		EMsn()
def START_EML():
	global eml
	eml = input('[+] Enter Email : ')
	if "@"in eml:
		domn = eml.split('@')[1]
		telegram_vv1ck("\n ======= It's started, wait a bit =======\n")
		all_Email(domn)
	else:exit('[-] Please enter an email ..')
def number_search():
	phon=input("\n[+] Enter Phone Number: ")
	code = phon.split(' ')[0]
	try:phone = phon.split(' ')[1]
	except IndexError:exit('[-] You must type the country code, then a space, and then the phone number.. \nExample[ 974 52947429 ]')
	if code == '20':country="EG:Egypt"
	elif code =='98':country="IR:Iran"
	elif code =='212':country="MA:Morocco"
	elif code =='213':country="DZ:Algeria"
	elif code =='216':country="TN:Tunisia"
	elif code =='249':country="SD:Sudan"
	elif code =='252':country="SO:Somalia"
	elif code =='961':country="LB:Libya"
	elif code =='962':country="JO:Jordan"
	elif code =='963':country="SY:Syria"
	elif code =='964':country="IQ:Iraq"
	elif code =="965":country="KW:Kuwait"
	elif code =='966':country="SA:Saudi Arabia"
	elif code =='967':country="YE:Yemen"
	elif code =='968':country="OM:Oman"
	elif code =='970':country="PS:Palestine"
	elif code =='971':country="AE:Emirates"	
	elif code =='972':country="ISR:Israel"
	elif code =='973':country="BH:Bahrain"
	elif code =='974':country="QA:Qatar"
	else:exit("[¿] The country code is not added for this number, it will be added soon")
	countr = country.split(':')[0]
	countr2= country.split(':')[1]
	send =r.get(f"http://caller-id.saedhamdan.com/index.php/UserManagement/search_number?number={phone}&country_code={countr}",headers={"User-Agent":"8Y/69"})
	try:
		name = send.json()['result'][0]['name']
		if name=='':name='nothing'
		nump = send.json()['result'][0]['number']
		#Communication rights reserved @_agf
		pho=phonenumbers.parse('+'+phon)
		qtr = carrier.name_for_number(pho,'en')
		telegram_vv1ck(f'\n[+] phone : {nump}\n[+] country : {countr2}\n[+] ZIP code : {countr}\n[+] name : {name}\n[+] number type : {qtr}')
	except KeyError:
		telegram_vv1ck('[-] No leaked information found')
def All_users():
	username = input('[?] Enter username : ')
	try:file = open('Link_all.txt','r')
	except FileNotFoundError:exit('[-] Please make sure that the Link_all.txt file is in the same folder as the tool')
	telegram_vv1ck('\n      ========== started ==========\n')
	sleep(1)
	telegram_vv1ck(f'[+] Username : {username}')
	while True:
		urls = file.readline().split('\n')[0]
		if urls=='':exit('\n    ======= completed =======')
		url = urls.format(username)
		try:web = url.split('//')[1]
		except KeyError:exit('\n    ======= completed =======')
		web_name = web.split('/')[0]
		if 'https://t.me'in url:web_name='telegram.com'
		send = r.get(url,headers={'User-Agent': 'Mozilla/5.0 (@vv1ck) Gecko/20100101 Firefox/90.0'})
		if send.status_code == 200:telegram_vv1ck(f'[+] linked on {web_name}')
		elif send.status_code == 404:telegram_vv1ck(f'[-] Not linked on {web_name}')
		else:
			telegram_vv1ck(f'[!] search error [{web_name}]')
try:
	vv1ck=int(input('[?] Enter mode : '))
	if vv1ck==1:START_EML()
	elif vv1ck==2:number_search()
	elif vv1ck==3:All_users()
	else:exit('[<\>] see you soon ...')
except ValueError:exit('[<\>] Please enter one of the displayed numbers')
