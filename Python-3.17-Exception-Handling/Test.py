'''
class MyException(RuntimeError):
    def __init__(self, arg):
        self.args = arg
'''
try:
    value = int(input())
    if(value < 4):
        raise Exception("value is lesser than 4");
    else:
        print("value is greater than 4")
except Exception:
    print("value is lesser than 4");
else:
    print("This is else block");
finally:
    print("This is finally block")
