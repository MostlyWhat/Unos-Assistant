#Modules Importer
from unos_plugin import UNOS
import google.cloud

#Initilisation
unos = UNOS()
unos.UNOSinitialize()
verification = unos.Verify()

#Main Loop
def main():
    while True:
        activated = unos.RecognizeUNOS()

        if activated == True:
            print("UNOS: Activated ( Reason: Triggered by a User )")
            unos.runningCommand()

        else:
            print("UNOS: Not Activated ( Reason: " + activated + " )")

#Check before launching
if verification == "True":
    unos.StartupText()
    while True:
        try:
            main()
        
        except google.api_core.exceptions.OutOfRange:
            main()

        finally:
            print("UNOS: System Ended Successfully")
            
    #unos.MainWindow()

else:
    exit()