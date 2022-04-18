import os
import time
from pathlib import Path

from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis
from System.Modules.Interface import Interface
from System.Modules.Precursor import Boot, Exit, Splash

# Initialising Modules
config = Config()
crisis = Crisis()
boot_text = Boot(configuration=config.launch_mode, username=config.username,
                 unos_name=config.unos_name)
splash_text = Splash(configuration=config.launch_mode, username=config.username,
                     unos_name=config.unos_name)
exit_text = Exit(configuration=config.launch_mode)
interface = Interface(configuration=config.launch_mode, username=config.username,
                      unos_name=config.unos_name)

# Print Some Texts
boot_text.show()
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
splash_text.show()
print(" ")
# Insert Checking for Internet Etc
print("[ UNOS System Pre-Checks ] Network Connection is Successful (Placeholder)")
print(" ")
print("[ UNOS Assistant Framework ] System is Ready for Inquiry and Beyond")
print(" ")

# Starting Interface
try:
    while True:
        interface.start()

except Exception as e:
    crisis.error(
        f"[ {Path(__file__).stem} ] An Unknown Error has occurred: {e}")
    print(f"[ {Path(__file__).stem} ] {e}")

finally:
    crisis.log(
        f"[ {Path(__file__).stem} ]",
        "Exiting UNOS Assistant Framework System")
    exit_text.show()
