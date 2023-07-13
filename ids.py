#!/usr/bin/python3 
from config import ROOT
import json
import sys

DEVID_FILE = ROOT+'/deviceid'
RATID_FILE = ROOT+'/ratids'
SESSIONID_FILE = ROOT+'/sessionid'

JSON_CONFIG_FILE = ROOT + '/peerpub_config.json'

class IDS:
    def __init__(self):
        try:
            with open(JSON_CONFIG_FILE ,'r') as f:
                json_data = json.load(f)
        except FileNotFoundError:
            sys.exit("peerpub_config.json file not found in /home/pi")
            
        self.devID = json_data['deviceid']
        self.sesID = json_data['sessionid']
        self.step = json_data['step']

    def change_step(self, step):
        self.step = int(step)
        self.save_data()

    def save_data(self):
        f = open(JSON_CONFIG_FILE, 'w')
        json.dump({
            "deviceid": self.devID,
            "step": self.step,
            "sessionid": self.sesID
        }, f)
        f.close()
        
    def sessionIncrement(self):
        self.sesID += 1
        self.save_data()
