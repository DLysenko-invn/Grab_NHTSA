import os
import time
import json
import requests
from configuration import *


for filename in os.listdir(DATABASE_DIR):
    print(filename,"- ",end='')

    rsp_fn = os.path.join(DATABASE_DIR,filename,METADATA_FILENAME)
    if not os.path.isfile(rsp_fn):
        print("Metadata not found")
        continue
    
    with open(rsp_fn,encoding='utf-8') as f:
      dat = json.load(f)
      
    assert dat['meta']['pagination']['count'] == dat['meta']['pagination']['total']
      
    if not dat['results']:
        print("No results")
        continue

    assert len(dat['results'])==1

    r =  dat['results'][0]

    if not r['INSTRUMENTATION']:
        print("No instrumentation")
        continue
        
    print("Loading")    
    
    for i in r['INSTRUMENTATION']:
        if i['SENTYPD'] == "ACCELEROMETER" or i['SENTYPD'] == "ANGULAR VELOCITY TRANSDUCER":
            print("    ",i['SENTYPD']," ", end='')
            url = i['URL_TSV']
            if not url:
                print("No data")
                continue
            fn = os.path.basename(url)
            path = os.path.join(DATABASE_DIR,filename,fn)
            print(fn," ",end='')
            if os.path.isfile(path):
                print('Skip')
                continue
            time.sleep(SLEEP_TIME_SEC)
            rsp = requests.get(url)
            with open(path, 'w') as f:
                f.write(rsp.text)
            print('OK')
        
    
    