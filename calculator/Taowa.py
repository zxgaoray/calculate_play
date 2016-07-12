user_input = raw_input()

class Taowa:
    def __init__(self):
        return
    def setSize(self, m1, m2):
        self.width = m1
        self.height = m2

        self.area = m1 * m2

class Sorter:
    def __init__(self):
        self.taowas = []
        self.lastWidth = 0
        self.lastHeight = 0
        return

    def setArray(self, str):
        self.arr = str.split(' ')
        for idx in range(len(self.arr)):
            self.arr[idx] = int(self.arr[idx])

    def makeTaowa(self):
        l = len(self.arr) / 2

        for idx in range(l):
            m1 = self.arr[idx*2]
            m2 = self.arr[idx*2+1]
            taowa = Taowa()
            taowa.setSize(m1, m2)
            self.taowas.append(taowa)

    def sortTaowa(self):
        self.taowas.sort(key=lambda taowa:taowa.width)

    def calculate(self):
        l = len(self.taowas)

        self.lastHeight = self.taowas[0].height
        self.lastWidth = self.taowas[0].width
        m = 1

        for idx in range(1, l, 1):
            taowa = self.taowas[idx]
            w = taowa.width
            h = taowa.height
            if w > self.lastWidth and h > self.lastHeight :
                m = m+1
                self.lastWidth = w
                self.lastHeight = h

        return m

sorter = Sorter()
sorter.setArray(user_input)
sorter.makeTaowa()
sorter.sortTaowa()
user_input = sorter.calculate()

print user_input