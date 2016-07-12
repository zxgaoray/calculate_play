user_input = raw_input()

class MoneyType:
    def __init__(self, s):
        self.money = 10 * int(s)
        self.count = 0

    def calculate(self):
        count = 1

        for idx in range(self.money/5):
            count = count + (self.money - idx * 5)/2 + 1

        self.count = count

moneyType = MoneyType(user_input)
moneyType.calculate()
user_input = moneyType.count

print user_input