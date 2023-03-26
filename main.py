import os
import sys
import time

# Bootup Time
time_start = time.time()

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

# Bootup End
time_end = time.time()
time_elasped = round(time_end - time_start, 2)
crisis.log(framework, f"Startup took {time_elasped} seconds.")

def main():
    """
    It starts the interface, and if an error occurs, it will be logged
    """
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
crisis.log(
    framework,
    "Exiting UNOS Assistant Framework System")
sys.exit()
