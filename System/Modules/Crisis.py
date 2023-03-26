import datetime
import logging

from System.Modules.BootLoader import Config

# Module Information
# Module Name: System.Module.Crisis
# Module Purpose: To Provide the Crisis Management for the UNOS Assistant Framework
# Note: Should have been named existential crisis!

# Setting Up Configurations
config = Config()
log_filename = datetime.now().strftime('unos-system_%H_%M_%d%m%Y.log')

# Logging Config
if config.dev_mode is True:
    logging.basicConfig(filename=log_filename,
                        filemode='a',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)

else:
    logging.basicConfig(filename=log_filename,
                        filemode='a',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO)

class Crisis():
    @staticmethod
    def log(process: str, log: str):
        if config.dev_mode is True:
            print(f"[ {process} ] {log}")

        logging.log(logging.INFO, f"[ {process} ] {log}")

    @staticmethod
    def warning(process: str, warning: str):
        if config.dev_mode is True:
            print(f"[ {process} ] {warning}")

        logging.warning(f"[ {process} ] {warning}")

    @staticmethod
    def error(process: str, error: str):
        if config.dev_mode is True:
            print(f"[ {process} ] {error}")

        logging.error(f"[ {process} ] {error}")
