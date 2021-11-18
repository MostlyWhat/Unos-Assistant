import re

transcript = "hey who knows"

WAKEUP_COMMANDS = ["uno's", "who knows", "nos", "nose", "hey Uno's", "hey who knows", "hey nos", "hey nose"]

for wakeup_commands in WAKEUP_COMMANDS:
    unos_check = bool(re.match(rf"\b{wakeup_commands}\b", transcript, re.I))

    if unos_check == True:
        print(unos_check)

    else:
        print("nothing")