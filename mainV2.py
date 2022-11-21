from random import seed
from random import randint
import time, random, string, maskpass, requests, itertools
print('''
\033[36m
.▄▄ · ▄▄· ▄ .▄         ▄▄▌       ▄▄ • ▄· ▄▌    ▄ •▄▪ ▄▄▌ ▄▄▌ ▄▄▄ ▄▄▄  
▐█ ▀.▐█ ▌██▪▐▪    ▪    ██• ▪    ▐█ ▀ ▐█▪██▌    █▌▄▌████• ██• ▀▄.▀▀▄ █·
▄▀▀▀███ ▄██▀▐█▄█▀▄ ▄█▀▄██▪  ▄█▀▄▄█ ▀█▐█▌▐█▪    ▐▀▀▄▐███▪ ██▪ ▐▀▀▪▐▀▀▄ 
▐█▄▪▐▐█████▌▐▐█▌.▐▐█▌.▐▐█▌▐▐█▌.▐▐█▄▪▐█▐█▀·.    ▐█.█▐█▐█▌▐▐█▌▐▐█▄▄▐█•█▌
 \033[37m▀▀▀▀·▀▀▀▀▀▀ ·▀█▄▀▪▀█▄▀.▀▀▀ ▀█▄▀·▀▀▀▀  ▀ •     ·▀  ▀▀.▀▀▀.▀▀▀ ▀▀▀.▀  ▀

               coded by wyatt g
               \033[36m
               
''')
randomnumber7 = chr(random.randint(ord('2'), ord('9')))
e = input("[?] Your schoology email: ")
pwd = maskpass.askpass("[?] Your schoology password: ", mask="") 
print("[+] Attempting to log into schoology with... " + e)
time.sleep(randomnumber7)
print("\033[32m\t> Successfully logged in as " + e + " [\u2713]")

c = input("\033[36m[?] Victims schoology email: ")
b = int(input("[?] Number of passwords to try: "))
a = input("[?] Start Attack? [y/n]: ")
if a == 'y':
    print("\033[31m[!] Starting bruteforce on " + c)
    time.sleep(2)
    for i in range(b):
        randomnumber = chr(random.randint(ord('0'), ord('9')))
        randomnumber2 = chr(random.randint(ord('0'), ord('9')))
        randomnumber3 = chr(random.randint(ord('0'), ord('9')))
        randomnumber4 = chr(random.randint(ord('0'), ord('9')))
        randomnumber5 = chr(random.randint(ord('0'), ord('9')))
        randomnumber6 = chr(random.randint(ord('0'), ord('9')))
        randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
        randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
        print("\033[31m[+] " + randomnumber + randomnumber2 + randomnumber3 + randomnumber4 + randomnumber5 + randomnumber6 + randomUpperLetter + randomLowerLetter, flush=True)
        time.sleep(0.0000001)
        
        time.sleep(randomnumber*10)
        for i in range(1):
         print(randomnumber + randomnumber2 + randomnumber3 + randomnumber4 + randomnumber5 + randomnumber6 + randomUpperLetter + randomLowerLetter)
