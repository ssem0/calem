import json #
import os
from datetime import date

FILE = "calories.json" # data file for cals

def load_data(): # load data function 
    try:
        with open (FILE, "r") as f: #opens file in read-only mode
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError): # handles missing file, empty file, and corrupt file
        return {}

def save_data(data): # save data function
    with open (FILE, "w") as f: # opens file in write-only mode
        json.dump(data, f, indent = 4)
