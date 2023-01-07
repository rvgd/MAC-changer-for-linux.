#!/usr/bin/env python

import subprocess
import optparse
import re

print("MMMMM          MMMMM          AAAAAA         CCCCCCCCCC         ")
print("MMM  MM      MM  MMM         AAA  AAA        CCC                ")
print("MMM    MM  MM    MMM        AAA    AAA       CCC                ")
print("MMM      MM      MMM       AAAAAAAAAAAA      CCC    H A N G E R.")
print("MMM              MMM      AAA        AAA     CCC                ")
print("MMM              MMM     AAA          AAA    CCC                ")
print("MMM              MMM    AAA            AAA   CCCCCCCCCC         ")
print("                                                         -rvgd  ")
print("[+] MAC changer starts...\n")

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface" , help=" Interface to change MAC Address. \n Default: wlan0")
    parser.add_option("-m","--mac", dest="new_mac" , help=" New MAC Address. ")    
    (options, arguments) = parser.parse_args()    
    if not options.new_mac:
        parser.error("\n[-]    Please specify -m (MAC address), use --help for more info.")
    if not options.interface:
        options.interface = "wlan0"
    return options

def change_mac (interface, new_mac):
    print("\n[+] Changing MAC Address for " + interface + " to " + new_mac + "\n")
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

def get_current_mac( interface ):

    ifconfig_result = str(subprocess.check_output(["ifconfig",interface]))

    mac_search_result = re.search(r"..:..:..:..:..:..", ifconfig_result)
    if mac_search_result:
        return mac_search_result.group()
    else:
        print("[-] Could not read MAC address. Please try again, if repeats check interface..")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("    Current MAC = "+ str(current_mac))

if current_mac == options.new_mac:
    print("    Don't need to change.")
    quit()
change_mac (options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
    print("    MAC Address has been updated to "+ current_mac)
    print("\n[+] Done..") 
else:
    print("[-] MAC Address can't be update..")


