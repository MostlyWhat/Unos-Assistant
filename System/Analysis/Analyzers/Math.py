import math

from mathparse import mathparse
from System.Modules.Crisis import Crisis

crisis = Crisis()

class Plugin:
    def __init__(self):
        self.name = "Math"
        # Context is not used in this plugin as it is not a context-based plugin but rather a process-based plugin
        # self.contexts = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "plus", "add", "subtract", "minus", "times", "multiply", "divide", "equation", "math", "question"]

    def analyze(self, query):
        processing = self.process(query)

        if processing is False:
            return False
        
        crisis.log("Math", "Passed the Math Expression Analysis")
        return True

    def process(self, query):
        expression = mathparse.extract_expression(query, language="ENG")
        
        try:
            result = str(mathparse.parse(expression, language="ENG"))
            return "The result is " + result
            
        except mathparse.PostfixTokenEvaluationException:
            return False
