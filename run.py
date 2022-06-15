import requests
import random
import time


chars = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
        'S','T','U','V','W','X','Y','Z','_','-','A','B','C','D','E','F','G','H',
        'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
        ]

count = 0

def scan(count):
    test = ""
    for i in range(32):
        test = test + random.choice(chars)
    drive = "https://drive.google.com/drive/folders/1" + test + "?usp=sharing"
    r = requests.get(drive)
    print(drive)
    print(r.status_code)

    if r.status_code == 200:
        with open('200s.txt', 'a') as good:
            good.write(f'\n{drive}')

    count = count + 1
    print(count)

    time.sleep(random.randint(1,5))
    scan(count)


scan(count)
