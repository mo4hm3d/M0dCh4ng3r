import os
import time

if not 'SUDO_UID' in os.environ.keys():
  exit("RUN THE SCRIPT AS ROOT")

print("*************************I AM NOT RESPONSIBLE FOR ANY ILLEGAL USE*************************")

  
print("Setting Up.......")
os.system("sudo chown root:root m4cch4ng3r.py")
os.system("sudo apt install python3-pip")
os.system("pip3 install getmac")
time.sleep(2)
os.system("pip3 install argparse")
time.sleep(2)
os.system("pip3 install os")
time.sleep(2)
print("Finishing Up.......")
os.system("sudo chmod 700 m4cch4ng3r.py")
time.sleep(2)
print("Finished Setting Up!")
