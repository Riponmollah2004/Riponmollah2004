import requests,json,hashlib
from os import system
from platform import system as osname
def clear():
	if osname() == "Linux":
		system("clear")
	else:
		system("cls")
clear()
r = '\x1b[91m'
g = '\x1b[92m'
y = '\x1b[93m'
b = '\x1b[94m'
m = '\x1b[95m'
c = '\x1b[96m'
w = '\x1b[97m'
def rez(url,exploit,n):
	if n == "1":
		print(w+" ["+g+"+"+w+"] "+g+exploit+": "+w+url+g+" [YES]")
	else:
		print(w+" ["+r+"+"+w+"] "+r+exploit+": "+w+url+r+" [NO]")
logo = f"""{g}
 /$$      /$$                      /$$       /$$           /$$      
| $$  /$ | $$                     | $$      |__/          | $$      
| $$ /$$$| $$  /$$$$$$  /$$    /$$| $$       /$$ /$$$$$$$ | $$   /$$
| $$/$$ $$ $$ |____  $$|  $$  /$$/| $$      | $$| $$__  $$| $$  /$$/
| $$$$_  $$$$  /$$$$$$$ \  $$/$$/ | $$      | $$| $$  \ $$| $$$$$$/ 
| $$$/ \  $$$ /$$__  $$  \  $$$/  | $$      | $$| $$  | $$| $$_  $$ 
| $$/   \  $$|  $$$$$$$   \  $/   | $$$$$$$$| $$| $$  | $$| $$ \  $$
|__/     \__/ \_______/    \_/    |________/|__/|__/  |__/|__/  \__/

	{y}Name: {c}WavLink Router Controller
	{y}Author: {c}Mohammad Ripon
	{y}Github: {c}http://github.com/RiponMollah2004
	
 {w} 1. Turn On Touch Link
 {w} 2. Turn Off Touch Link 
 {w} 3. Rebot WavLink Router
 {w} 4. Show All Users
 {w} 5. Block User Internet
 {w} 6. Unblock User Internet
 """
def SETUP():
	clear()
	print(logo)
	try:
		passw = input(g+" - "+w+"Enter Router Password: ")
		userid = hashlib.md5(("admin"+passw).encode('utf-8')).hexdigest()
		open(".userid","w").write(userid)
		return userid
	except:
		exit()
try:
	userid = open(".userid","r").read()
except:
	userid = SETUP()
clear()
print(logo)
try:
	req = requests.get("http://192.168.10.1:80/protocol.csp?fname=system&opt=login&function=set&usrid="+userid)
	token = json.loads(req.text)["token"]
except:
	print(r+' - '+c+'Message: '+w+'Wavlink Router Login Failed!')
	exit()
cookies = {"token":token,"lstatus":"true"}
on = "http://192.168.10.1/protocol.csp?token="+token+"&fname=net&opt=touch_link&function=set&wifi_close=1&enable=1&math=0.5594288364625055"
off = "http://192.168.10.1/protocol.csp?token="+token+"&fname=net&opt=touch_link&function=set&wifi_close=1&enable=0&math=0.17723405908778012"
rebot = "http://192.168.10.1/protocol.csp?token="+token+"&fname=system&opt=setting&action=reboot&function=set"
users = "http://192.168.10.1:80/protocol.csp?token="+token+"&fname=system&opt=main&function=get&math=0.7973682950786567"
while True:
	cmd = input(g+" [{}root{}@{}salahdin{}:{}~{}]{}# {}".format(g,r,y,g,c,g,m,r))
	if cmd == "1":
		try:
			req = requests.post(on,cookies=cookies)
		except:
			req = ""
		if '"enable": 1' in req.text:
			print(g+' - '+c+'Message: '+w+'Wavlink Touch Link Turn On Successful!')
	if cmd == "2":
		try:
			req = requests.post(off,cookies=cookies)
		except:
			req = ""
		if '"enable": 0' in req.text:
			print(g+' - '+c+'Message: '+w+'Wavlink Touch Link Turn Off Successful!')
	if cmd == "3":
		try:
			req = requests.post(rebot,cookies=cookies)
		except:
			req = ""
		if '"error": 0' in req.text:
			print(g+' - '+c+'Message: '+w+'Wavlink Router Rebot Successfu. Please Wait!')
	if cmd == "4":
		try:
			req = json.loads(requests.post(users,cookies=cookies).text)
			for i in req['terminals']:
				ip = i["ip"]
				if ip == "":
					ip = "192.168.0.1"
				print(g+" - "+w+i['name']+c+" Ip: "+y+ip)
				print(g+" - "+w+i['name']+c+" Mac: "+y+i["mac"])
				print(g+" - "+w+i['name']+c+" Speed: "+y+str(i["speed"]))
				print(g+" - "+w+i['name']+c+" Up Speed: "+y+str(i["up_speed"]))
				print()
		except Exception as e:
			print(e)
	if cmd == "5":
		try:
			mac = input(g+" - "+w+"User Mac Address: ")
			req = requests.post("http://192.168.10.1/protocol.csp?token="+token+"&fname=net&opt=host_black&function=set&mac="+mac+"&act=on")
			if '"error": 0' in req.text:
				print(g+' - '+c+'Message: '+w+'Mac: '+m+mac+y+" Blocked!")
			else:
				print(g+' - '+c+'Message: '+w+'Sorry! Mac: '+mac+' Can Not Blocked')
		except:
			pass
	if cmd == "6":
		try:
			mac = input(g+" - "+w+"User Mac Address: ")
			req = requests.post("http://192.168.10.1:80/protocol.csp?token="+token+"&fname=net&opt=host_black&function=set&mac="+mac+"&act=off")
			if '"error": 0' in req.text:
				print(g+' - '+c+'Message: '+w+'Mac: '+m+mac+y+" Unblock Successful!")
			else:
				print(g+' - '+c+'Message: '+w+'Sorry! Mac: '+mac+' Can Not Unblock!')
		except:
			pass