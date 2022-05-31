from mathparse import mathparse


class Plugin:
    def __init__(self):
        self.name = "Math"
        # Context is not used in this plugin as it is not a context-based plugin but rather a process-based plugin
        # self.contexts = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "plus", "add", "subtract", "minus", "times", "multiply", "divide", "equation", "math", "question"]

    def analyze(self, query):
        processing = self.process(query)

        if processing == False:
            return False
        
        return True

    def process(self, query):
        expression = mathparse.extract_expression(query, language="ENG")
        
        try:
            result = mathparse.parse(expression, language="ENG")
            return "The result is " + result
            
        except mathparse.PostfixTokenEvaluationException:
            return False
