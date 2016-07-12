user_input = raw_input()

class Pocker:
    def __init__(self, s):
        arr = s.split(' ')
        self.n = int(arr[0])
        self.m = int(arr[1])
        self.target = True
    def calculate(self):
        n = self.n
        m = self.m

        if n % (m+1):
            self.target = True
        else:
            self.target = False


pocker = Pocker(user_input)
pocker.calculate()

if pocker.target:
    user_input = "i win"
else:
    user_input = "u win"

print user_input