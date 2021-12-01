#Modules Importer
from unos_plugin_cmd import UNOS, BootLoader
import google.cloud

#Initilisation and Config
unos = UNOS()
boot = BootLoader()
unos.UNOSinitialize()

#Main Loop
def main():
    while True:
        activated = unos.RecognizeUNOS()

        if activated == True:
            print("UNOS: Activated ( Reason: Triggered by a User )")
            unos.runningCommand()

        else:
            print("UNOS: Not Activated ( Reason: " + activated + " )")

#Check before Launching
verification = boot.Verify()
if verification == True:

    #Internet Connection Check
    connected = boot.InternetCheck()

    if connected == True:
        #Boot Sequence
        boot.StartupText()

        #Main Loop
        while True:
            try:
                main()
            
            except google.api_core.exceptions.OutOfRange:
                main()

            finally:
                print("UNOS: System Ended Successfully")
                
        #unos.MainWindow()

    else:
        print("BootLoader: Program Closing ( Reason: Internet is Offline )")
        exit()

else:
    print("BootLoader: Program Closing ( Reason: Continue is False )")
    exit()