from json import *
storage = "gHealthmetric.json"
# write to file
def record(data):
    with open(storage,"w") as fwrite:
        dump(data,fwrite,indent=4)
# read from file
def retrieve():
    try:
        with open(storage,"r") as fread:
            return load(fread)
    except FileNotFoundError: return {}