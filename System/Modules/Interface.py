import concurrent.futures

import gradio as gr
from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis
from System.Modules.Management import Autofixer
from System.Modules.Speech import Listener, Speaker
from System.Modules.Splitter import Splitter

# Module Information
# Module Name: System.Modules.Interface
# Module Purpose: To Provide the Interface for the UNOS Assistant Framework

# Setting Up Modules
config = Config()
crisis = Crisis()
autofixer = Autofixer()

# Setup if the user enabled text to speech and if they did not, then disable it
if config.text_to_speech is True:
    speaker = Speaker()

# Setup if the user enabled voice recognition and if they did not, then disable it
if config.voice_recognition is True:
    listener = Listener()

modules = [f"{config.analyzers_location}.{modules}" for modules in config.analyzers_modules]
splitter = Splitter(plugins=modules, fallback_module=config.fallback_module)

# Quick Variables
unos_name = config.unos_name
username = config.username
launch_config = config.launch_mode

# Interface Modules
class Interface():
    @staticmethod
    def start():
        if launch_config == "cli" and config.voice_recognition is True:
            cli_interface = cli_speech()
            cli_interface.main()

        elif launch_config == "gui":
            gui_interface = gui()
            gui_interface.main()

        elif launch_config == "web":
            web_interface = web()
            web_interface.main()

        else:
            cli_interface = cli()
            cli_interface.main()

    @staticmethod
    def moreinfo():
        if launch_config == "cli" and config.voice_recognition is True:
            cli_interface = cli_speech()
            return cli_interface.extra_input()

        elif launch_config == "gui":
            gui_interface = gui()
            return gui_interface.extra_input()

        elif launch_config == "web":
            web_interface = web()
            return web_interface.extra_input()

        else:
            cli_interface = cli()
            return cli_interface.extra_input()

class cli():
    def main(self):
        while True:
            try:            
                # Gets Input from Splitter
                print(" ")
                query = str(input(f"{username}@{unos_name}: "))
                print(" ")
                splitter_output = splitter.analyze(query)

                # Outputting the Results
                self.outputting(splitter_output)

            except KeyboardInterrupt:
                break

            except Exception as e:
                # Reporting Error
                crisis.error(
                    "Interface", f"The Error: {e} has occurred")
                self.outputting("An error has occurred, please check logs")
                
                if config.autofixer is True:
                    # Attempt to Autofix it
                    crisis.error(
                        "Interface", "Attempting to use Autofixer")
                    self.outputting("Attempting to use Autofixer")
                    autofix = autofixer.fix(str(e))
                    
                    # Successfully Fixed the Issue
                    if autofix is True:
                        crisis.error(
                            "Interface", "Successfully fix the issue using Autofixer")
                        self.outputting("Successfully fix the issue using Autofixer")
                        
                    # Failed to Fix the Issue
                    else:
                        crisis.error(
                            "Interface", "Failed to fix the issue using Autofixer")
                        self.outputting("Failed to fix the issue using Autofixer")
            

    def extra_input(self):
        extrainput_request = "I'm sorry, can you provide me with a category?"

        if config.text_to_speech is True:
            speaker.speak(extrainput_request)

        self.outputting(extrainput_request)
        print(" ")
        response = str(input(f"{username}@{unos_name}: "))
        print(" ")

        return response

    @staticmethod
    def outputting(splitter_output: str):
        # Printing the Results
        print(f"[ {unos_name.upper()} ] {splitter_output}")

        # Run the Speaker Module in another thread, interruptable
        if config.text_to_speech is True:
            speaker.speak(splitter_output)

class cli_speech():
    def main(self):
        while True:
            try:
                # Listen for Wakeup Call
                print(f"\n[ {unos_name.upper()} ] Listening for Wakeup Command...")
                listen = listener.listenForUNOS()

                # If the wakeup call is detected, then ask for input
                if listen is True:
                    if config.text_to_speech is True:
                        speaker.speak("Yes?")

                    print(f"\n[ {unos_name.upper()} ] Listening for Command...")
                    user_response = listener.listenForCommand()

                    # Send the Input to Splitter for Analysis
                    print(f"\n[ {unos_name.upper()} ] {username} responded with: {user_response}")
                    splitter_output = splitter.analyze(user_response)

                    # Outputting the Results
                    self.outputting(splitter_output)

            except KeyboardInterrupt:
                break

            except Exception as e:
                # Reporting Error
                crisis.error(
                    "Interface", f"The Error: {e} has occurred")
                self.outputting("An error has occurred, please check logs")
                
                if config.autofixer is True:
                    # Attempt to Autofix it
                    crisis.error(
                        "Interface", "Attempting Autofixer")
                    self.outputting("Attempting Autofixer")
                    autofix = autofixer.fix(e)
                    
                    # Successfully Fixed the Issue
                    if autofix is True:
                        crisis.error(
                            "Interface", "Successfully fix the issue using Autofixer")
                        self.outputting("Successfully fix the issue using Autofixer")
                        
                    # Failed to Fix the Issue
                    else:
                        crisis.error(
                            "Interface", "Failed to fix the issue using Autofixer")
                        self.outputting("Failed to fix the issue using Autofixer")
                
    def extra_input(self):
        pass

    @staticmethod
    def outputting(splitter_output: str):
        # Printing the Results
        print(" ")
        print(f"[ {unos_name.upper()} ] {splitter_output}")

        # Run the Speaker Module in another thread, interruptable
        if config.text_to_speech is True:
            speaker.speak(splitter_output)

class gui():
    def main(self):
        pass

    def extra_input(self):
        pass

    def outputting(self):
        pass

class web():
    def main(self):
        interface = gr.Blocks()

        with interface:
            gr.Markdown(
                f"""
                # {config.unos_name} Assistant Web Interface
                
                ## UNOS Assistant Information
                Assistant Name: {config.unos_name}
                Assistant Codename: {config.unos_codename} 
                Assistant Version: {config.unos_version}
                Assistant Stability: {config.unos_stability}
                Assistant Predecessor: {config.unos_previous_interation}
                
                ## Warning the Interface is still in it's experimental stages. Voice Recognition and Text to Speech has been disabled.
                
                Welcome {config.username}, Start typing below and then click Submit to see the output.
                """)
            with gr.Column():
                input_box = gr.Textbox(label="Query", placeholder="Who are you?")
                context_box = gr.Textbox(label="Context (Not Required)", placeholder="About")
                output_box = gr.Textbox(label="Output")
                
            btn = gr.Button("Submit")
            btn.click(fn=self.process, inputs=[input_box, context_box], outputs=output_box)

        interface.launch(share = True)

    def process(self, query, context_text):
        try:
            # Global a Variable
            global context
            context = context_text
            
            # Process information using Splitter
            splitter_output = splitter.analyze(query)
            
            # Returns Information back to Output
            return splitter_output
        
        except Exception as e:
            # Reporting Error
            crisis.error(
                "Interface", f"The Error: {e} has occurred")
            
            if config.autofixer is True:
                # Attempt to Autofix it
                crisis.error(
                    "Interface", "Attempting Autofixer")
                autofix = autofixer.fix(e)
                
                # Successfully Fixed the Issue
                if autofix is True:
                    crisis.error(
                        "Interface", "Successfully fix the issue using Autofixer")
                    
                # Failed to Fix the Issue
                else:
                    crisis.error(
                        "Interface", "Failed to fix the issue using Autofixer")

    def extra_input(self):
        return context
