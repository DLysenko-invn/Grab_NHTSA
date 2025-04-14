# Grab data from the nhtsa.gov site




## Venv
```
python3 -m venv .venv
```
```
pip install -r requirements.txt
```
```
source .venv/bin/activate
```


## Stage 1

Creates test folders and "manifest.json" files 

```
python stage1_collect_tests.py
```

## Stage 2

Collects "metadata.json" files 

```
python stage2_collect_metadata.py
```

## Stage 3

Collects data files 

```
python stage3_collect_data.py
```
