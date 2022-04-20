import logging

from System.Modules.BootLoader import Config

# Module Information
# Module Name: System.Module.Crisis
# Module Purpose: To Provide the Crisis Management for the UNOS Assistant Framework

# Setting Up Configurations
config = Config()

# Logging Config
if config.dev_mode == True:
    logging.basicConfig(filename="unos-latest.log",
                        filemode='a',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)

else:
    logging.basicConfig(filename="unos-latest.log",
                        filemode='a',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO)


class Crisis():
    def log(self, process: str, log: str):
        if config.dev_mode == True:
            print(f"[ {process} ] {log}")

        logging.log(logging.INFO, f"[ {process} ] {log}")

    def warning(self, process: str, warning: str):
        if config.dev_mode == True:
            print(f"[ {process} ] {warning}")

        logging.warning(f"[ {process} ] {warning}")

    def error(self, process: str, error: str):
        if config.dev_mode == True:
            print(f"[ {process} ] {error}")

        logging.error(f"[ {process} ] {error}")
