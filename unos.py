import os
import sys
import time

from System.Modules.BootLoader import Config, PreChecks
from System.Modules.Crisis import Crisis
from System.Modules.Interface import Interface
from System.Modules.Preburner import Preburner
from System.Modules.Precursor import Boot, Exit, Splash

# Initialising Modules
config = Config()
crisis = Crisis()
prechecks = PreChecks()
preburner = Preburner()
boot_text = Boot(configuration=config.launch_mode)
splash_text = Splash(configuration=config.launch_mode)
exit_text = Exit(configuration=config.launch_mode)
interface = Interface(configuration=config.launch_mode,
                      username=config.username, unos_name=config.unos_name)

# Print Some Texts
crisis.log("UNOS Assistant Framework",
           "UNOS Assistant Framework has been started")
boot_text.show()
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
splash_text.show()
print(" ")
crisis.log("UNOS Assistant Framework",
           "Running Pre-Checks before starting the Interface")
prechecks.check()
preburner.start()

# Starting Interface
while True:
    try:
        interface.start()

    except Exception as e:
        crisis.error(
            "UNOS Assistant Framework", f"An Unknown Error has occurred: {e}")

    except KeyboardInterrupt:
        exit_text.show()
        break

print("\n")
crisis.log(
    "UNOS Assistant Framework",
    "Exiting UNOS Assistant Framework System")
print("\n")
sys.exit()
