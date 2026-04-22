# from json import *
from pickle import *
# storage = "gHealthmetric.json"
storage = "gHealthmetric.pkl"
# write to file
def record(data):
    with open(storage,"wb") as fwrite:
        dump(data,fwrite)
# read from file
def retrieve():
    try:
        with open(storage,"rb") as fread:
            return load(fread)
    except (FileNotFoundError,EOFError): return {}