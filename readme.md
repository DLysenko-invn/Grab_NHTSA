# Grab data from the nhtsa.gov site

The data placed in the "db" folder


## Venv
```
python3 -m venv .venv
```
```
source .venv/bin/activate
```
```
pip install -r requirements.txt
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
