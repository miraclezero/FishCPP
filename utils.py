# RATID
def get_ratid_scantime(rats, fname, this_lick, act, maxILI, maxISI):
    try:
        with open(fname, "r") as f:
            rat, scantime, *dummies = f.read().strip().split("\t")
            scantime = float(scantime)
            
    except (OSError, ValueError) as e:
        rat = "ratUnknown"
        scantime = 0

    try:
        if rat is None:
            rat = "ratUnknown"
        else:
            rat_obj = rats[rat]
            if act:
                last_lick = rat_obj.last_act_licks["time"]
            else:
                last_lick = rat_obj.last_inact_licks["time"]
            
            if this_lick - last_lick > maxILI and this_lick - scantime > maxISI:
                rat = "ratUnknown"
            
    except KeyError:
        print("error from get_ratid_scantime")

    return rat, scantime


# SYRINGE
def reload_syringe():
    from pump_move import PumpMove
    from gpiozero import DigitalInputDevice

    BACKWARD_LIMIT = DigitalInputDevice("GPIO23")

    mover = PumpMove()
    while BACKWARD_LIMIT.value != 1:
        mover.move("backward")
    del(mover)


# Send Slack message
def send_message(payload):
    import requests
    # webhook url file
    webhook_url = ""
    # file storing the webhook url
    with open('/home/pi/webhook_url', 'r') as f:
        webhook_url = f.read().strip()
    requests.post(webhook_url, json=payload)