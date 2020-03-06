from __future__ import print_function

import platform
import subprocess
import time
import os
from datetime import datetime as dt


def timestamp():
    now = dt.now()
    print("[" + str(now.hour).zfill(2) + ":" + str(now.minute).zfill(2) + ":" + str(now.second).zfill(2) + "]", end=" ")


def check_internet(host="google.com"):
    timestamp()
    print("Testing " + host + "... ", end="")
    if platform.system() == "Darwin":
        ping_result = subprocess.call(["ping", "-c", "1", host], shell=False, stdout=subprocess.PIPE)
    elif platform.system() == "Windows":
        ping_result = subprocess.call(["ping", "-n", "1", host], shell=False, stdout=subprocess.PIPE)
    else:
        raise OSError("Platform not supported.")
    if ping_result == 0:
        print("connected!")
        return True
    else:
        print("not connected!")
        return False


print("Starting... use CTRL-C to exit.")
while True:
    if not check_internet():
        timestamp()
        print("Resetting... ", end="")
        if platform.system() == "Darwin":
            subprocess.call(["networksetup", "-setairportpower", "Wi - Fi", "off"],
                            shell=False, stdout=subprocess.PIPE)
            subprocess.call(["networksetup", "-setairportpower", "Wi - Fi", "on"],
                            shell=False, stdout=subprocess.PIPE)
            # TODO: fix
        elif platform.system() == "Windows":
            subprocess.call(["netsh", "wlan", "disconnect"])
        else:
            raise OSError("Platform not supported.")
        time.sleep(10)
    time.sleep(2)
