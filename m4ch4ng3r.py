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
   print(f"[Your MAC Address Is]: {gmc()}")
   os.system(f"ifconfig {args.interface} down")
   os.system(f"ifconfig {args.interface} hw ether {args.mac}")
   os.system(f"ifconfig {args.interface} up")
   print(f"[Your MAC Was Successfully Changed To]: {args.mac}")
 Macchanger()
 option = ""
 while option != "yes" or option != "no" or option != "Yes" or option != "No":
   option = input("[Do You Want To Change Your MAC Again]: ")
   if option == "Yes" or option == "yes" or option == "YES":
    desired_mac = str(input("[Enter MAC Address]: "))
    os.system(f"ifconfig {args.interface} down")
    os.system(f"ifconfig {args.interface} hw ether {desired_mac}")
    os.system(f"ifconfig {args.interface} up")
    print(f"[Your MAC Address Was Sucessfully Changed To]: {desired_mac}")
   elif option == "No" or option == "no" or option == "NO":
    exit("\nThanks For Using M0dCh4ng3r")
   elif option == "exit" or option == "quit":
       exit("\nThanks For Using M0dCh4ng3r")
   elif option == "ifconfig" or option == "ipconfig" or option == "ip":
       os.system("ifconfig")
   else:
    print("Invalid Command!")
except KeyboardInterrupt:
   exit("\nThanks For Using M4Ch4ng3r")
