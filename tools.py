 
import json

with open('config.json') as fjson:
    config = json.load(fjson)

def get_path():
    path =  config['path']
    return path

def get_finalpath():
    finalpath =  config['finalPath']
    return finalpath