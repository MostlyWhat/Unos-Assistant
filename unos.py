import os
import time

from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis
from System.Modules.Interface import Interface
from System.Modules.PreChecks import PreChecks
from System.Modules.Precursor import Boot, Splash

# Initialising Modules
config = Config()
crisis = Crisis()
prechecks = PreChecks()
boot_text = Boot(configuration=config.launch_mode)
splash_text = Splash(configuration=config.launch_mode)
interface = Interface(configuration=config.launch_mode)

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
print(" ")
exit_text.show()
