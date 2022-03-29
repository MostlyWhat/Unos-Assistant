# Fallback Plugin
class Plugin:
    def __init__(self):
        self.name = "System.Analysis.MCAS"
        self.contexts = []

    # Define static method, so no self parameter
    def analyze(self, query):
        # Some prints to identify which plugin is been used
        # True
        return True

    def process(self, query):
        # Compare and see how many of the 3 values are the same
        value1 = 0
        value2 = 1
        value3 = 1

        if value1 == value2 == value3:
            print("All values are the same")
        
        elif value1 != value2 != value3:
            print("All values are different")    
            
        else:
            if value1 == value2:
                print("Value 1 and Value 2 are the same")
            elif value1 == value3:
                print("Value 1 and Value 3 are the same")
            elif value2 == value3:
                print("Value 2 and Value 3 are the same")