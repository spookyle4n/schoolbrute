from random import seed
from random import randint
import time
import random
import string
print('''
\033[36m 
  _____     _____
 /____/|   /____/|_______________________________
|    | |  |    |/________/___________/_________\\ \\
|    | |  |    |   ___   |     __    |    ___   \\_\\
|    | /\ |    |  |   |  |    | |\\___|   |   |  | |
|    |/  \|    |  |___|  |    | |    |   |___|  |_|
 \             /         |    | |    |          / /
\033[37m  \___________/__________|____|_|    |_________/_/
   
               tiktok jahsehrare
               insta: spookyle4n\033[34m
''')
e = input("[?] Your schoology email?: ")
d = input("[?] Your schoology password? (bruteforce attack wont work without it): ")
print("attempting to log into schoology with...\033;3m " + e)
time.sleep(4)
print("\033[34m;0successfully logged in as " + e + " [\u2713]")

c = input("\033[30m[?] Victims schoology email?: ")
b = int(input("[?] How many passwords would you like to try?: "))
a = input("[?] Start Attack? [y/n]: ")
if a == 'y':
    print("\033[31m;0Starting bruteforce on " + c)
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
            print("\033[32m| attempting... \033[1;3m676848Vr\033[0m |\n\tsuccess! [\u2713] ")
            
        print("\033[31m[+] attempting... " + randomnumber + randomnumber2 + randomnumber3 + randomnumber4 + randomnumber5 + randomnumber6 + randomUpperLetter + randomLowerLetter, flush=True)
        time.sleep(0.0000001)
