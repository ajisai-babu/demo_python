import time,subprocess

timeLeft=60
while timeLeft>0:
    if timeLeft>=10:
        print(timeLeft,end='')
    else:
        print('\b',timeLeft,end='')
    time.sleep(1)
    print('\b'*len(str(timeLeft)),end='',flush=True)
    timeLeft-=1

print('done.\n')
