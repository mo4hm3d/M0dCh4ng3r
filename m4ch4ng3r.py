#!/usr/bin/python3

import os
from getmac import get_mac_address as gmc
import argparse

parser = argparse.ArgumentParser(description="M0h4mm4d's python3 script to change MAC address")
parser.add_argument('-i', '--interface', metavar='interface', type=str, default='wlan0', help="Which interface to change its MAC address")
parser.add_argument('-m', '--mac', metavar='mac', type=str, help="The MAC address you want to spoof")

args = parser.parse_args()

if os.geteuid() != 0:
    exit("RUN THE SCRIPT AS ROOT")


try:
 def Macchanger():
   print(f"[Your MAC address is]: {gmc()}")
   os.system(f"ifconfig {args.interface} down")
   os.system(f"ifconfig {args.interface} hw ether {args.mac}")
   os.system(f"ifconfig {args.interface} up")
   print(f"[Your MAC Was Successfully Changed To]: {args.mac}")
 Macchanger()
 option = ""
 while option != "yes" or option != "no" or option != "Yes" or option != "No":
   option = input("[Do you want to spoof your MAC address again]: ")
   if option == "Yes" or option == "yes" or option == "YES":
    desired_mac = str(input("[Enter MAC address]: "))
    os.system(f"ifconfig {args.interface} down")
    os.system(f"ifconfig {args.interface} hw ether {desired_mac}")
    os.system(f"ifconfig {args.interface} up")
    print(f"[Your MAC address was sucessfully changed to]: {desired_mac}")
   elif option == "No" or option == "no" or option == "NO":
    exit("\nThanks For using M4Ch4ng3r")
   elif option == "exit" or option == "quit":
       exit("\nThanks for using M4Ch4ng3r")
   elif option == "ifconfig" or option == "ipconfig" or option == "ip":
       os.system("ifconfig")
   else:
    print("Invalid command!")
except KeyboardInterrupt:
   exit("\nThanks for using M4Ch4ng3r")
