import os
import time
import json
import requests
from configuration import *




for filename in os.listdir(DATABASE_DIR):
    print(filename,"- ",end='')
    path = os.path.join(DATABASE_DIR,filename,TESTINFO_FILENAME)
    if not os.path.isfile(path):
        print("Manifest not found")
        continue
    rsp_fn = os.path.join(DATABASE_DIR,filename,METADATA_FILENAME)
    if os.path.isfile(rsp_fn):
        print("Skip")
        continue
    
    with open(path,encoding='utf-8') as f:
      dat = json.load(f)
      
    url = URL_TEMPLATE % dat['testNo']
    time.sleep(SLEEP_TIME_SEC)
    rsp = requests.get(url).json()
    rsp_fn = os.path.join(DATABASE_DIR,filename,METADATA_FILENAME)
    with open(rsp_fn, 'w', encoding='utf-8') as f:
        json.dump(rsp, f, ensure_ascii=False, indent=4)
    
    print("OK")