
#   __  __                _   _    _                _            _ 
#  |  \/  |              (_) | |  | |              | |          (_)
#  | \  / | ___ _ __ __ _ _  | |__| | ___ _   _  __| | __ _ _ __ _ 
#  | |\/| |/ _ \ '__/ _` | | |  __  |/ _ \ | | |/ _` |/ _` | '__| |
#  | |  | |  __/ | | (_| | | | |  | |  __/ |_| | (_| | (_| | |  | |
#  |_|  |_|\___|_|  \__,_| | |_|  |_|\___|\__, |\__,_|\__,_|_|  |_|
#                       _/ |               __/ |                   
#                      |__/               |___/                    
#
# This is for Peneteration test on Python Script
# Written By: Meraj Heydari
# 2015-2016
# Meraj.Heydarii@gmail.com


print '''
M .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.M
E| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |E
R| |  ___  ____   | || |  ____  ____  | || |      __      | || |  _________   | || |      __      | || | ____  _____  | |R
A| | |_  ||_  _|  | || | |_   ||   _| | || |     /  \     | || | |_   ___  |  | || |     /  \     | || ||_   \|_   _| | |A
J| |   | |_/ /    | || |   | |__| |   | || |    / /\ \    | || |   | |_  \_|  | || |    / /\ \    | || |  |   \ | |   | |J
H| |   |  __'.    | || |   |  __  |   | || |   / ____ \   | || |   |  _|      | || |   / ____ \   | || |  | |\ \| |   | |H
E| |  _| |  \ \_  | || |  _| |  | |_  | || | _/ /    \ \_ | || |  _| |_       | || | _/ /    \ \_ | || | _| |_\   |_  | |E
Y| | |____||____| | || | |____||____| | || ||____|  |____|| || | |_____|      | || ||____|  |____|| || ||_____|\____| | |Y
D| |              | || |              | || |              | || |              | || |              | || |              | |D
A| |              | || |              | || |              | || |              | || |              | || |              | |A
R| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |R
I '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' I
                                                  Meraj.Heydarii@gmail.com        
''' ,



import requests
import socket
import sys
import lxml.html
import time
import random
from bs4 import BeautifulSoup
import urllib2
import base64
import os
import platform
#=========================================
#Start find CMS of the Target!
#=========================================

    
def cms_detector(DIC): # This function try to find CMS of the target 

	
#=========================================
#Variables Of cms_detector function
#=========================================	

	condition=True # Define a condition variable and set "True"

#=========================================
#end of Variable of cms_detector function
#=========================================	
	print "\nCMS:\n====\n" # Print title of function
	
	
	readmefile=DIC['Z'] + "/" + "README.txt" #Create a url that include READE.txt file
	robotsfile=DIC['Z'] + "/" + "robots.txt" #Create a url that include robots.txt

	readmereq=requests.get(readmefile, headers=DIC['FIREFOXHEADER']) #Send a request to readmefile by get method
	robotsreq=requests.get(robotsfile, headers=DIC['FIREFOXHEADER']) #Send a request to robotsfile by get method	
	
#=========================================
#Start Search for Wordpress CMS!
#=========================================
	cmswkey=["content=\"wordpress\"","wp-content/uploads", "xmlrpc.php", "wp-content", "wordpress"] #Key words of Wordpress
	cmsjkey=["content=\"joomla\"", "/component", "joomlaworks", "joomla", "joom"] #Key words of joomla
	cmsdkey=["Drupal"] #key words of drupal
	
		
	
	wcmslist=open("wordpressversions.txt", "r") #Open wordpress version file that include versions of Wordpress
	


	if readmereq.status_code==200 or robotsreq.status_code==200: #Check for exist README and robots file
		wcmslist.seek(0) # Set pointer to first line of wcmslist
		for line in wcmslist.readlines(): # Read lines of wcmslist
			line=line[0:len(line)-1]  # Delete "Enter" from end of line
			wversion1=str("Wordpress " + line)  # Attach "Wordpress" at the first of versions
			wversion2=str("Wordpress! " + line) # Attach "Wordpress!" at the first of versions

			
			if readmereq.status_code==200 and readmereq.content.find(wversion1)!=-1 or readmereq.content.find(wversion2)!=-1: #Check wversion1 and wversion2 on README.txt if README.txt exist
				print wversion1 # Printing real version of the CMS
				condition=False # Set condition to False (that means find the version of Target)
				break	#Break From Loop (for)
			
			if line=="end": # Check if line was "end"
				condition=True # Set condition to True (that means can't find the version of Target yet)
				break #Break from Loop (for)
			
			if robotsreq.status_code==200 and robotsreq.content.find(wversion1)!=-1 or robotsreq.content.find(wversion2)!=-1: #Check wversion1 and wversion2 on robots.txt if robots.txt exist
				print wversion1 # Printing real version of the CMS
				condition=False # Set condition to False (that means find the version of Target)
				break	#Break From Loop (for)
		
			if line=="end": # Check if line was "end"
				condition=True # Set condition to True (that means can't find the version of Target yet)
				break #Break from Loop (for)

	if condition: #Check confition if was "True"

		wcmslist.seek(0) # Set pointer to first line of wcmslist
		for line in wcmslist.readlines(): # Read lines of wcmslist
			line=line[0:len(line)-1]  # Delete "Enter" from end of line
			wversion1=str("WordPress " + line)  # Attach "Wordpress" at the first of versions
			wversion2=str("Wordpress! " + line) # Attach "Wordpress!" at the first of versions
			
			if DIC['HEADER'].find(wversion1)!=-1 or DIC['BODY'].find(wversion1)!=-1 \
			   or DIC['HEADER'].find(wversion2)!=-1 or DIC['BODY'].find(wversion2)!=-1: # Check wversion1 and wversion2 on header and content of the target
				print wversion1 # Printing real version of the CMS
				condition=False # Set condition to False (that means find the version of Target)

				if line=="end": # Check if line was "end"
					condition=True # Set condition to True (that means can't find the version of Target yet)
					break # Break from Loop (for)



	if condition: # Check condition if was "True"
		fff="http://guess.scritch.org/%2Bguess/?url=" + str(DIC['Z']) # Create a url to get help from "guess.scritch.org" web site for finding the CMS
		jjjj=requests.get(fff, headers=DIC['FIREFOXHEADER']) # Send a request to online cms detector by get method

		if jjjj.content.find("Wordpress")!=-1: # Check content of the guess.scritch.org for check result and find "Wordpress" 
			wcmslist.seek(0) # Set pointer to first line of wcmslist
			for line in wcmslist.readlines(): # Read lines of wcmslist				
				line=line[0:len(line)-1] # Delete "Enter" from end of line
				wversion=str("Wordpress</a> " + line) # Attach "Wordpress</a>" at the first of versions
				if line=="end": # Check if line was "end"
					condition=True # Set condition to True (that means can't find the version of Target yet)
					break # Break from Loop (for)
				
				if jjjj.content.find(wversion)!=-1: # Check content of the guess.scritch.org for finding wversion
					print "Wordpress " + line # Print version of wordpress
					condition=False # Set condition to False (that means find the version of Target)
					break # Break from Loop (for)


	if condition: # Check condition i was "True"
		for wword in cmswkey: # Check keys on cmswkey
			if str(DIC['BODY']).find(wword)!=-1: 
				print "Wordpress!"
				condtion=False				
				break

	wcmslist.close()
								
#=========================================
#Finish Search for Wordpress CMS!
#=========================================

#=========================================
#Start Search for Joomla CMS!
#=========================================
	


	
        jcmslist=open("joomlaversions.txt", "r")
	
	if condition and (readmereq.status_code==200 or robotsreq.status_code==200):
		jcmslist.seek(0)
		for line in jcmslist.readlines():
			line=line[0:len(line)-1]
			jversion1=str("Joomla " + line)
			jversion2=str("Joomla! " + line)
			
			if line=="end":
				condition=True
				break
			
			if readmereq.content.find(jversion1)!=-1 or readmereq.content.find(jversion2)!=-1:
				print jversion1
				condition=False
				break

	if condition:
		jcmslist.seek(0)
		for line in jcmslist.readlines():
			line=line[0:len(line)-1]
			jversion1="Joomla " + line
			jversion2="Joomla! " + line
			
			if DIC['HEADER'].find(jversion1)!=-1 or DIC['BODY'].find(jversion1)!=-1 \
			   or DIC['HEADER'].find(jversion2)!=-1 or DIC['BODY'].find(jversion2)!=-1:
				print jversion1	
				condition=False

			if line=="end":
				condition=True
				break

		
	
	if condition:
		fff="http://guess.scritch.org/%2Bguess/?url=" + str(DIC['Z'])
		jjjj=requests.get(fff, headers=DIC['FIREFOXHEADER'])

		if jjjj.content.find("Joomla")!=-1:
			jcmslist.seek(0)
			for line in jcmslist.readlines():
				line=line[0:len(line)-1]
				jversion=str("Joomla</a> " + line)
				if line=="end":
					condition=True
					break
				if jjjj.content.find(jversion)!=-1:
					print "Joomla " + line
					condition=False
					break
	
	if condition:		
		for jword in cmsjkey:		
			jcms=str(DIC['BODY']).find(jword)
			if jcms!=-1:	
				print "Joomla!"
				condition=False
				break
	jcmslist.close()
					
#=========================================
#Finish Search for Joomla CMS!
#=========================================
					
#=========================================
#Start Search for Drupal CMS!
#=========================================
	
	dcmslist=open("drupalversions.txt", "r")	

	if condition and (readmereq.status_code==200 or robotsreq.status_code==200):
		dcmslist.seek(0)
		for line in dcmslist.readlines():
			line=line[0:len(line)-1]
			dversion1=str("Drupal " + line)
			dversion2=str("Drupal! " + line)

			if line=="end":
				condition=True
				break

			if readmereq.content.find(dversion1)!=-1 or readmereq.content.find(dversion2)!=-1:
				print dversion1
				condition=False


	if condition:
		dcmslist.seek(0)
		for line in dcmslist.readlines():
			line=line[0:len(line)-1]
			dversion1="Drupal " + line
			dversion2="Drupal! " + line

			if DIC['HEADER'].find(dversion1)!=-1 or DIC['BODY'].find(dversion1)!=-1 \
			   or DIC['HEADER'].find(dversion2)!=-1 or DIC['BODY'].find(dversion2)!=-1:
				print dversion1
				condition=False

			if line=="end":
				condition=True
				break





	if condition:
		fff="http://guess.scritch.org/%2Bguess/?url=" + str(DIC['Z'])
		jjjj=requests.get(fff, headers=DIC['FIREFOXHEADER'])

		if jjjj.content.find("Drupal")!=-1:
			dcmslist.seek(0)
			for line in dcmslist.readlines():
				line=line[0:len(line)-1]
				dversion=str("Drupal</a> " + line)
				if line=="end":
					condition=True
					break
				if jjjj.content.find(dversion)!=-1:
					print "Drupal " + line
					condition=False
					break




	if condition:
		for dword in cmsdkey:
			dcms=str(DIC['BODY']).find(dword)
			if dcms!=-1:
				print "Drupal!"
				condition=False
				break
	dcmslist.close()

	if condition:
		print "CMS Not Found!"
#=========================================
#Finish Search for Drupal CMS!
#=========================================

#=========================================
#finish find CMS of the Target!
#=========================================

#=========================================
#Start Port Scan from Target!
#=========================================

def port_scaner(DIC):
	
    
	print "\nOpen Ports:\n==========="

	l=(21,23,25,52,68,80,110,123,443,445,2576,3389,1433,1434,8080)

	for port in l:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result=s.connect_ex((DIC['IP'], port))
		if result == 0:
			print "Port {} \t Open".format(port)
			
		else:
			print "Port {} \t Closed".format(port)

	s.close()  
	
#=========================================
#Finish Port Scan from Target!
#=========================================	


#=========================================
#Start find Status code Of webpage!
#=========================================

def status_code(DIC):
	 
    
	y=DIC['X'].status_code
	print "\nstatus code:\n============\n" 
	print str(y)

	if y==200:
		print "Page is availabe!"
	
	if y==302:
		print "Redirection!"

	if y==404:
		print "Page is unavailable!"

	if y==403:
		print "Access is Denied!"

	if y==400:
		print "The request could not be understood by the server!"

	if y==401:
		print "The request requires user authentication!"

	if y==407:
		print "Proxy Authentication Required!"

	if y==408:
		print "Request Timeout!"

	if y==500:
		print "Internal server error!"

	if y==502:
		print "Bad Gateway!"

	if y==503:
		print "Service Unavailable!"

	if y==504:
		print "Gateway Timeout!"

	if y==505:
		print "HTTP Version Not Supported!"


#=========================================
#Finish find Status code Of webpage!
#=========================================

#=========================================
#Start find Admin Page!
#=========================================		
		
def find_admin_page(DIC):

	
	adminlist=open("adminlist.txt", "r")
	print "\nAdmin page: \n==========="
	for line in adminlist.readlines():
		
		u=DIC['Z'] + "/" + line
		n=requests.get(u, headers=DIC['FIREFOXHEADER'])
		print n
		print u
		print n.status_code
		if n.status_code=="200" or n.status_code=="401" or n.status_code=="302":
			print "The Login page is: "
			print u
			print "Status code is: " + n.status_code
			break
			#uu=u
			#return uu

		
		if n.status_code=="403":
			print "The Login page is: "
			print u
			print "Status code is 403!"
			
	else:
		print "\nLogin Page not found!"


#=========================================
#Finish find Admin Page!
#=========================================
		
def basic_information(DIC):
	
	global result

	print "\nBasics Information:\n===================\n"
	result.write("\nBasics Information:\n===================\n");
	print "Target: " + str(DIC['TARGET'])
	result.write("Target: " + str(DIC['TARGET']))
	print "IP Address: " + str(DIC['IP'])
	
	print "Server: ",
	if DIC['HEADER'].find("Server")!=-1:
		print DIC['X'].headers['server']
	else:
		print "Not found!"
		
	#print "OS: ",
	#print platform.system(),
	#print platform.release()
		
	print "Language: ",
	if DIC['HEADER'].find("X-Powered-By")!=-1:
		print DIC['X'].headers['x-powered-by']
	else:
		print "Not found!"
	
	print "content-type: ",		
	if DIC['HEADER'].find("content-Type")!=-1:
		print DIC['X'].headers['content-type']
	else:
		print "Not found!"
		
	print "X-Content-Encoded-By: ",		
	if DIC['HEADER'].find("'X-Content-Encoded-By'")!=-1:
		print ['X'].headers['X-Content-Encoded-By']
	else:
		print "Not found!"	

#=========================================
#Start find Links on webpage!
#=========================================

def get_links(DIC):
	
	#print "\nLinks Of Webpage:\n=================\n"
	#dom =  lxml.html.fromstring(DIC['BODY'])
	
	#for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
		#print link
	#return link



        ####encoding = resp.encoding if 'charset' in DIC['X'].headers['content-type'].lower() else None
        ####soup = BeautifulSoup(resp.content, from_encoding=encoding)
	soup = BeautifulSoup(DIC['BODY'])
        for link in soup.find_all('a', href=True):
		print(link['href'])

        #soup = BeautifulSoup(DIC['BODY'],'html.parser')
	#for link in soup.findAll('a'):
		#print link


#=========================================
#Finish find Links on webpage!
#=========================================


#=========================================
#Start Man Page!
#=========================================
def man_page():
	print '''
	Usage: Khafan.py TargetName [-all] [-a] [-b] [-c] [-s] [-p] [-g] [-h]\n
	Options:
	     -a           Get admin page of the Target.
	     -b           Get Basic Information of the Target.
	     -c           Get CMS Version of the Target.
	     -h           Show man page.
	     --help       Show man page.
	     -s           Get Status Code of the Target
	     -p           Scan port from Target.
	     --proxy      Use proxy.
	     -g           Get links of the Target.
	     -all         Do all things!
	'''
	
	
#=========================================
#Finish Man Page!
#=========================================





#=========================================
#Start find Subdomains!
#=========================================
def find_subdomains(DIC):
	
	print "\nSub Domains:\n============\n"
	subdomainlist1=open("sub1.txt", "r")
	dom =  lxml.html.fromstring(DIC['BODY'])

	for link in dom.xpath('//a/@href'):
		if link.find("." + DIC['T'])!=-1:
			print link
	for line in subdomainlist1.readlines():
		line=line[0:len(line)-1]
		sub1="http://" + line + "." + DIC['T']
		print sub1
		try:
			prr= requests.get(sub1, headers=DIC['FIREFOXHEADER'], timeout=2).status_code
		except:
			print "Connecton Error!"
			continue
		 
		if prr==200 or 403:
			print "OK"
		else:
			print "NO!"
		
#=========================================
#Finish find Subdomains!
#=========================================




def main(url):
	target= url
	if "http://" in target:
		z=target
	else:
		z="http://" + target
	
	k=target.find("/")
	if k!=-1:
		t=target[:k]
	else:
		t=target	

	socket.setdefaulttimeout(30)
	ip=socket.gethostbyname(t)
	
	#Create a proxy list if needed
	if proxyUse:
	
		webpage = urllib2.urlopen('https://proxy-list.org/english/index.php?p=1')
		soup = BeautifulSoup(webpage,'html.parser')
		proxylist=[]
	
		for anchor in soup.find_all('li', attrs={'class': 'proxy'}):
			tt=anchor.get_text()[6:]
			ttt=tt[:-1]
			proxylist.append(ttt)
		
	#print proxylist
	
	
	headerlist= [ 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10',\
	              'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',\
	              'BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0 3gpp-gba',\
	              'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',\
	              'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/1.1.0-80) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16 Silk-Accelerated=true',\
	              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Touch)',\
	              'Opera/9.25 (Windows NT 5.1; U; en)',\
	              'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',\
	              'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)']
	
	firefoxheader={'user-agent': random.choice(headerlist)}	
	
	
	print firefoxheader
	
	
	if proxyUse:
		tmOut = 3  # timeout is 4 second by default (first level we add 1 to 3 --> 4 )
		while proxylist:
			try:# if each proxy not working or is too slow we use another one 
				#myproxy="http://" + str(base64.b64decode(random.choice(proxylist)))
				myproxy="http://" + str(base64.b64decode(proxylist.pop()))
				proxy= {"http" : myproxy}
				print "proxy: " + myproxy
				tmOut = tmOut + 1 #Lets increase timeout for next proxy		
				print "timeOut for proxy : ",str(tmOut),"s"
				x=requests.get(z, proxies=proxy, headers=firefoxheader,timeout=tmOut)
				
				break
			except:
				print "The proxy isn't working or is slow ! wait for testing another"
		else:#when all of proxy not working !!!
			print "All of proxy not working!"
				
	else:
		x=requests.get(z, headers=firefoxheader)
	body=x.content
	header=str(x.headers)
	
	return {'TARGET':target,'Z':z, 'T':t, 'IP':ip, 'X':x, 'HEADER':header, 'BODY':body, 'FIREFOXHEADER':firefoxheader}

print "\n" + "=" * 123

try:
	
#=========================================
#Start Print Time to screen!
#=========================================
	global proxyUse
	proxyUse = False 
	toDoList = [] 
	localtime = time.asctime( time.localtime(time.time()) )
	ltime=localtime
	print ltime
	element= None
#=========================================
#Finish Print Time to screen!
#=========================================	
	


	if len(sys.argv)<=2 :
		
		man_page()
	else:
		#First we find all of switches and append works to toDoList and run them finally
		for counter in range(2 , len(sys.argv)): #we check --proxy swtich existance 
			if sys.argv[counter]=="--proxy":
				proxyUse = True	
				
		main=main(sys.argv[1])
		
		result=open("result.txt", 'w+')
		
		for counter in range(2 , len(sys.argv)): 
			if sys.argv[counter]=="-m":
				toDoList.append(man_page,[])
							
				
			if sys.argv[counter]=="-a":
				toDoList.append([find_admin_page,[main]])
				
	
			if sys.argv[counter]=="-b":
				toDoList.append([basic_information,[main]])
			
	
			if sys.argv[counter]=="-c":
				toDoList.append([cms_detector,[main]])
	
	
			if sys.argv[counter]=="-r":
				toDoList.append([status_code,[main]])
				
	
			if sys.argv[counter]=="-p":
				toDoList.append([port_scaner,[main]])


			if sys.argv[counter]=="-g":
				toDoList.append([get_links,[main]])
	
	
			if sys.argv[counter]=="-h" or sys.argv[counter]=="--help":
				toDoList.append([man_page,[]])
		
		
			if sys.argv[counter]=="-s":
				toDoList.append([find_subdomains,[main]])
				
				
			if sys.argv[counter]=="-all":
				toDoList.append([status_code,[main]])
				toDoList.append([basic_information,[main]])
				toDoList.append([cms_detector,[main]])
				toDoList.append([get_links,[main]])
				toDoList.append([find_subdomains,[main]])
				toDoList.append([port_scaner,[main]])
				toDoList.append([find_admin_page,[main]])
				
			#elif sys.argv[counter]!="-S":
			#	os.remove("Result.txt")
			if len(toDoList)==0 :
				man_page()
		for work in toDoList:
			func = work[0] 
			args = work[1]
			func(*args)
			#if sys.argv[counter]!="-h" or sys.argv[counter]!="--help":
				#print "\n" + "=" * 42
				#if raw_input("\nDo you want save result to a file?(y/n) ")=="y":
					#savefilename=raw_input("Choose name: ")
					#print savefilename
except Exception as e:
	print e
	print "An error occurred or your address dont exist!"

print "\n" + "=" * 123
	
#if __name__ == "__main__":
#	main()