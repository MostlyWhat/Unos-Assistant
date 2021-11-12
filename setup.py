import os
import time

print("This script will setup the system and install the packages")
time.sleep(5)
os.system('pip install -r requirements.txt' if os.name == 'nt' else 'pip3 install -r requirements.txt')
print("This script will now exit the program")
exit(0)