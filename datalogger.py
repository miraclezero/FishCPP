#!/usr/bin/env python3
import time
from config import DATA_DIR, DATA_PREFIX


def helper(x):
    s = x.split('\t')
    return s[0], s[2], s[4]

class LickLogger:
    def __init__(self, devID, sesID):
        self.devID = devID
        self.sessID= sesID
        self.startTime=time.strftime("%Y-%m-%d\t%H:%M:%S", time.localtime())

    def createDataFile(self, schedule, ratIDs, sessLen):
        date=time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
        self.datafile = DATA_DIR + DATA_PREFIX + date + "_" + str(self.devID) + '_S' + str(self.sessID) +  "_" + schedule + "_" + str(ratIDs) + '_' + str(sessLen) +  '.csv'
        print ("\nData file location:\n", self.datafile)

    def logEvent(self, rat, eventSec, eventType, timeLapsed, ratio=0):
        # Create output string
        outputstr = rat + "\t" + str(eventSec) + "\t"+ time.strftime("%Y-%m-%d\t%H:%M:%S", time.localtime()) + "\t" + self.devID + "_S" + str(self.sessID) + "\t" + eventType + "\t" + str(ratio) + "\t"+ str(timeLapsed) + "\n"
        print (outputstr)
        with open (self.datafile, "a") as datafile:
            datafile.write(outputstr)

    @staticmethod
    def finalLog(fname,data_dict,rfid_file):
        ratids = [data_dict["ratID1"][0], data_dict["ratID2"][0]]
        poke_counts = {ratids[0]:{"act":0, "inact": 0}, ratids[1]:{"act":0, "inact":0}}

        # read the poke counts from rfid files
        with open(rfid_file, "r") as f:
            lines = f.readlines()[1:]
            filtered = list(map(helper, lines))
            for rid , act_str, poke_count in filtered:
                if act_str == "active":
                    poke_counts[rid]["act"] = int(poke_count.strip())
                else:
                    poke_counts[rid]["inact"] = int(poke_count.strip())

        # summary .tab file
        with open(DATA_DIR+ "/" + fname, "a+") as f:
            print(DATA_DIR + "/" + fname)
            ID1_str = (("{}\t"*13).format(*data_dict["ratID1"], poke_counts[ratids[0]]["act"], poke_counts[ratids[0]]["inact"])) + "\n"
            ID2_str = (("{}\t"*13).format(*data_dict["ratID2"], poke_counts[ratids[1]]["act"], poke_counts[ratids[1]]["inact"])) + "\n"
            ID0_str = (("{}\t"*13).format(*data_dict["ratID0"], 0, 0)) + "\n"
            f.write(ID1_str + ID2_str + ID0_str)
        
                

