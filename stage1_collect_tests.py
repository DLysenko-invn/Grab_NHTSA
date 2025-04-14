import os
import time
import json
import requests
from configuration import *




def process_tst(obj:dict)->bool:
    
    path = os.path.join(DATABASE_DIR,str(obj['testNo']))
    if os.path.isdir(path):
        return False

    os.mkdir(path)
    fn = os.path.join(path,TESTINFO_FILENAME)
    with open(fn, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)
    return True



def  process_url(url:str):
    if (url==None):
        return

    print(url)
    
    time.sleep(SLEEP_TIME_SEC)
    rsp = requests.get(url).json()

    if not rsp['results']:
        print('No results')
        return True
        
    for r in rsp['results']:
        print(r['testNo'],"- ",end='')
        if (r['testNo']<MIN_TESTID):
            print('Test id too small. Exit.')
            return False
        if r['modelYear'] and (r['modelYear']<MIN_YEAR):
            print('Car is too old. Exit.')
            return False 
        rc = process_tst(r)
        print("OK" if rc else "Skip" )
    
    process_url(rsp['meta']['pagination']['nextUrl'])
    
    return True






if not os.path.exists(DATABASE_DIR):
    os.makedirs(DATABASE_DIR)


N1 = MAX_TESTID


while (True):
    N2 = N1 - TESTID_STEP
    if (N2<0):
        N2=0
    
    print(">>>",N2,"-",N1)
    rc = process_url( URLSEARCH_TEMPL % (N2,N1) )
    if not rc:
        break
    
    N1 = N1 - 100
    if (N1<MIN_TESTID):
        break








