#Modules Importer
from unos_plugin_google import UNOS

#Initilisation
unos = UNOS()
unos.UNOSinitialize()
verification = unos.Verify()

#Main Loop
def main():
    while True:
        activated = unos.RecognizeUNOS()

        if activated == True:
            print("UNOS: Activated ( Reason: " + activated + " )")
            unos.runningCommand()

        else:
            print("UNOS: Not Activated ( Reason: " + activated + " )")

#Check before launching
if verification == "True":
    unos.StartupText()
    main()
    #unos.MainWindow()

else:
    exit()