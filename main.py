#Modules Importer
from unos_plugin import UNOS

#Initilisation
unos = UNOS()
unos.UNOSinitialize()
verification = unos.Verify()

#Main Loop
def main():
    while True:
        activated = unos.RecognizeUNOS()

        if activated == "True":
            unos.runningCommand()
            print("UNOS: Activated ( Reason: " + activated + " )")

        else:
            print("UNOS: Not Activated ( Reason: " + activated + " )")

#Check before launching
if verification == "True":
    unos.StartupText()
    main()
    #unos.MainWindow()

else:
    exit()