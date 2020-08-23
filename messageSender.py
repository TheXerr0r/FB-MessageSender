#!/usr/bin/env/python3

import sys

if not sys.version_info.major == 3 and sys.version_info.minor >= 6:
        print("\n\n\t\tThe FB Meesage Attacker Tool Is require The Python3 To Run.")
        print(u"\t\t\t\tYou are using \033[93mPython {}.{}.".format(sys.version_info.major, sys.version_info.minor) + "\n\n")
        sys.exit(1)


import fbchat
from fbchat import Client
from getpass import getpass
import os

def CLS():
    if os == "nt":
        os.system("cls")
    else:
        os.system("reset")


def banner():
    print("""
                                                 __                _           
          /\/\   ___  ___ ___  __ _  __ _  ___  / _\ ___ _ __   __| | ___ _ __ 
         /    \ / _ \/ __/ __|/ _` |/ _` |/ _ \ \ \ / _ \ '_ \ / _` |/ _ \ '__|
        / /\/\ \  __/\__ \__ \ (_| | (_| |  __/ _\ \  __/ | | | (_| |  __/ |   
        \/    \/\___||___/___/\__,_|\__, |\___| \__/\___|_| |_|\__,_|\___|_|   
                                    |___/                                      
                            
                             ℂ𝕣𝕖𝕒𝕥𝕖𝕕 𝔹𝕪 @𝕖𝕙𝕤𝟜𝕟𝕟𝕟
                     𝓓𝓮𝓿𝓮𝓵𝓸𝓹𝓮𝓻𝓼 𝓣𝓮𝓪𝓶: 𝓢𝓬𝓸𝓻𝓹𝓲𝓸𝓷 𝓢𝓱𝓲𝓮𝓵𝓭
                                              
                            """)

def Message_Sender():
    try:
        banner()
        username = input("\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# Type Your FB UserName/Email: ")
        client = fbchat.Client(username, getpass())
        number_of_friends = int(input("\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# You Want To Send This Massage For How many Friends: "))
        for person in range(number_of_friends):
	        name = str(input("\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# Type Your Friend Username: "))
	        msg = str(input("\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# Type Your Massage: "))
	        while True:
		        sent = client.send(fbchat.models.Message(msg),name.uid)
		        if sent:
			        print("Message Sent Successfully!")
    except KeyboardInterrupt:
        print("\n\n\t\tPlease Wait For 3 Seconds...")
        time.sleep(3)
        print("\n\n\t\t\tGood By :)")
        exit()
			    
if __name__ == "__main__":
    Message_Sender()
