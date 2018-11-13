#! usr/bin/env python
import argparse
import subprocess
import re

def  argument():
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--interface",dest="interface",help="Interface to change the macaddress")
    parser.add_argument("-m","--mac",dest="new_mac",help="New Mac address")
    options=parser.parse_args()
    if not options.interface:
        parser.error("Please specify the Interface")
    elif not options.new_mac:
        parser.error("Please specify the mac-address")
    return(options)
def run_command(interface,new_mac):
    subprocess.call(["ifconfig" , interface , "down"])
    subprocess.call(["ifconfig" , interface , "hw" , "ether", new_mac])
    subprocess.call(["ifconfig" , interface , "up"])
def check_result(interface):
    result=subprocess.check_output(["ifconfig", interface])
    check=re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result.decode("utf-8"))
    return(check.group(0))
options=argument()
run_command(options.interface,options.new_mac)
check_value=check_result(options.interface)
if check_value!=options.interface:
    print("[+] new mac address :" + check_value)
    print("task completed successfully")
else:
    print("Some error occured")



