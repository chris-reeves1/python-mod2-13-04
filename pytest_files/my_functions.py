def add(a, b):
    return a + b

def divide(a, b):
    return a / b

class Area():
    def __init__(self, length, width):
        self.length, self.width = length, width

    def area(self):
        return self.length * self.width