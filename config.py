BASE_DIR = "./SocialDrink"
ROOT = "/home/pi"
# /home/pi/SocialDrinking directory
DATA_DIR = "{}/{}/".format(ROOT, "SocialDrinking")
# each data file starts with Soc_
DATA_PREFIX = "Soc_"
CONFIG_FILE = "/home/pi/openbehavior/PeerPub/python/session_configuration.csv"


def get_sessioninfo(sessionid):
    with open(CONFIG_FILE, "r") as f:
        csv_data = f.read().split("\n")
        
    sessioninfo = [info.split(",")[2:] for info in csv_data[1:] if sessionid in info.split(",")[:2]]

    return sessioninfo
