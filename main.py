import os
import sys
import time

from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis
from System.Modules.Interface import Interface
from System.Modules.Precursor import Boot, Exit, Splash
from System.Modules.PreSystem import Preburner, PreChecks

# Initialising Modules
config = Config()
crisis = Crisis()
prechecks = PreChecks()
preburner = Preburner()
boot_text = Boot()
splash_text = Splash()
exit_text = Exit()
interface = Interface()

# Quick Variable
framework = "UNOS Assistant Framework"

# Print Some Texts
crisis.log(framework,
           "UNOS Assistant Framework has been started")
boot_text.show()
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
splash_text.show()
print(" ")
crisis.log(framework,
           "Running Pre-Checks before starting the Interface")
prechecks.check()
preburner.start()

def main():
    try:
        interface.start()

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        crisis.error(
            framework, f"The Error '{e}' has occurred in '{fname}' on line '{exc_tb.tb_lineno}'")

    except KeyboardInterrupt:
        exit_text.show()

# Starting Interface
main()

# Exit Program
print("\n")
crisis.log(
    framework,
    "Exiting UNOS Assistant Framework System")
print("\n")
sys.exit()
