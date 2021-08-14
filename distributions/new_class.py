class Methods:
    def __init__(self, result):
        self.result = result

    def add(self,a,b):
        self.result = a + b
        return self.result

    def Minus(self,a,b):
        self.result = a - b
        return self.result

    def Multiply(self,a,b):
        self.result = a * b
        return self.result

    def Divide(self,a,b):
        self.result = a / b
        return self.result
