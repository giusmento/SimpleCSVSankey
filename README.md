# Simple Sankey from CSV

This repository is a python code that generate a Sankey chart from a csv

Please follow the below step to generate your chart

### Step 1: install requirements

```
pip3 install -r ./requirements.txt

```

or,
If you need to create a new virtual env

MAC

```
python -m venv simple-snakey-venv
source simple-snakey-venv/bin/activate
pip3 install -r ./requirements.txt
```

WINDOWS

### Step 2: Prepare your CSV

The tool processes the csv file `data.csv` stored under the folder `./data`.
Please add your data in the file

### Step 3: Run the Sankey creation

From terminal starts the generation process

```
python ./sankey.py
```

Your browser will open with the sankey chart
