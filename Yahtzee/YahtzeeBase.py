import random

class dice(object):

    def __init__(self,tag):
        self._value  = -1
        self._tag    = tag
            
    def _roll(self):
        self.value = random.randint(1,7)

    @property
    def value(self):
        return self._value

class roll(object):
        
    def __init__(self,*args):
        self._values = args

    def _top(self,n):
        return n*self._values.count(n)

    def _nOfAKind(self,n):
        for i in range(1,7):
            if self._values.count(i) == n: return i
        return -1

    def ones  (self):   return self._top(1)
    def twos  (self):   return self._top(2)
    def threes(self):   return self._top(3)
    def fours (self):   return self._top(4)
    def fives (self):   return self._top(5)
    def sixes (self):   return self._top(6)

    def threeOfAKind(self):
        if self._nOfAKind(3) > 0: return sum(self._values)
        else:                     return 0
            
        if any([self._values.count(i)>2 for i in range(1,7)]):
            return sum(self._values)
        else:
            return 0

    def fourOfAKind(self):
        if any([self._values.count(i)>3 for i in range(1,7)]):
            return sum(self._values)
        else:
            return 0

    def fullHouse(self):
        i5 = self._nOfAKind(5)
        i3 = self._nOfAKind(3)
        i2 = self._nOfAKind(2) 
        if (i5>0) or (i3>0) and (i2>0) and (i2!=i3):
            return 25
        else:
            return 0                          

    def shortStraight(self):
        if any([all([i in self._values for i in range(j,j+4)]) for j in range(1,4)]):
            return 30
        else:
            return 0
 
    def longStraight(self):
        if any([all([i in self._values for i in range(j,j+5)]) for j in range(1,3)]):
            return 40
        else:
            return 0

    def yahtzee(self):
        if self._nOfAKind(5) > 0:
            return 50
        else:
            return 0

    def chance(self):
        return sum(self._values)
