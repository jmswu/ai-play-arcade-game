class Test:
    def __init__(self, num: int):
        self.val = num
    
    def printNum(self):
        print(f'value is: {self.val}')


test = Test(10)
test.printNum()