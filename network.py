from __future__ import print_function

import subprocess
import time


def check_internet(host="google.com"):
    print("Testing " + host + "... ", end="", flush=True)
    if subprocess.call(["ping", "-n", "1", host], shell=False, stdout=subprocess.PIPE) == 0:
        print("connected!")
        return True
    else:
        print("not connected!")
        return False


print("Starting... use CTRL-C to exit.")
while True:
    if not check_internet():
        print("Resetting... ", end="", flush=True)
        subprocess.call(["netsh", "wlan", "disconnect"])
        time.sleep(10)
    time.sleep(2)
