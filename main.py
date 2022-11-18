from random import seed
from random import randint
import time, random, string, maskpass
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
e = input("[?] Your schoology email?: ")
pwd = maskpass.askpass(mask="") 
d = input("[?] Your schoology password?: ")
print("attempting to log into schoology with... " + e)
time.sleep(4)
print("\033[32m\t> successfully logged in as " + e + " [\u2713]")

c = input("\033[36m[?] Victims schoology email?: ")
b = int(input("[?] How many passwords would you like to try?: "))
a = input("[?] Start Attack? [y/n]: ")
if a == 'y':
    print("\033[31mStarting bruteforce on " + c)
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
        if randomnumber + randomnumber2 + randomnumber3 + randomnumber4 + randomnumber5 + randomnumber6 + randomUpperLetter + randomLowerLetter == '676848Vr':
            print("\033[32m[+] attempting... 676848Vr\nsuccess! [\u2713] ")
            print("schoology email: " + c)
            print("schoology password: 676848Vr")
            time.sleep(100000000)
            
        print("\033[31m[+] attempting... " + randomnumber + randomnumber2 + randomnumber3 + randomnumber4 + randomnumber5 + randomnumber6 + randomUpperLetter + randomLowerLetter, flush=True)
        time.sleep(0.0000001)
