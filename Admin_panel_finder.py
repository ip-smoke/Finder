#!/usr/bin/python
# Made by Smoke

import requests
import webbrowser
from colorama import Fore
import termcolor2
import termcolor
import os
# ==================================
os.system("pip install termcolor2")
os.system("pip install requests")
os.system("pip install colorama")
os.system('clear')
# ==================================
print(Fore.LIGHTBLUE_EX)
print("""
 +-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+
 |A|d|m|i|n| |p|a|n|e|l| |f|i|n|d|e|r|   |smoke|
 +-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+""")
print(Fore.CYAN)
print("""TELEGRAM >> not ID ---- RUBIKA >> @Spoilede
     	TELEGRAM CHANNEL >> t.me/Smoke_office
""")

print("\n\n\n")
# ==================================
print(Fore.LIGHTYELLOW_EX)
print("[#] Enter the your url > example (www.site.com , site.com)")
try:
	target = input(termcolor2.colored('[=>] ENTER THE URL >>  ' , color = "yellow"))

	patch = ["user.php","login.php","admin1.php","wp-login.php","admin.php"]

	for i in patch:

		link = "https://" + target + "/" + i 

		re = requests.get(link)

		check = re.status_code

		if check == 200:
			print(termcolor2.colored('[+] page login found >',color = "green"),link)
		else:
			print(termcolor2.colored('[-] not found ' , color = "red"),link)
except:
	print(termcolor2.colored('!! please check your url or internet !!' , color="red"))

print("\n\n\n\n")
print(Fore.LIGHTBLACK_EX)	
print("""
Made by Zucker
Please subscribe to my channel!
""")
