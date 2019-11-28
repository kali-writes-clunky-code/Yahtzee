import random

class Roll(object):
        
    def __init__(self,*args):
        self._values = args

    def _top(self,n):
        return n*self._values.count(n)

    def _n_of_a_kind(self,n):
        for i in range(1,7):
            if self._values.count(i) == n: return i
        return -1

    def ones  (self):   return self._top(1)
    def twos  (self):   return self._top(2)
    def threes(self):   return self._top(3)
    def fours (self):   return self._top(4)
    def fives (self):   return self._top(5)
    def sixes (self):   return self._top(6)

    def three_of_a_kind(self):
        if any([self._values.count(i)>2 for i in range(1,7)]):
            return sum(self._values)
        else:
            return 0

    def four_of_a_kind(self):
        if any([self._values.count(i)>3 for i in range(1,7)]):
            return sum(self._values)
        else:
            return 0

    def full_house(self):
        i5 = self._n_of_a_kind(5)
        i3 = self._n_of_a_kind(3)
        i2 = self._n_of_a_kind(2) 
        if (i5>0) or (i3>0) and (i2>0) and (i2!=i3):
            return 25
        else:
            return 0                          

    def small_straight(self):
        if any([all([i in self._values for i in range(j,j+4)]) for j in range(1,4)]):
            return 30
        else:
            return 0
 
    def large_straight(self):
        if any([all([i in self._values for i in range(j,j+5)]) for j in range(1,3)]):
            return 40
        else:
            return 0

    def yahtzee(self):
        if self._n_of_a_kind(5) > 0:
            return 50
        else:
            return 0

    def chance(self):
        if all([value>0 for value in self._values]):
          return sum(self._values)
        else:
          return 0

    def __getitem__(self,key):
      if key=="Ones":   return self.ones()
      if key=="Twos":   return self.twos()
      if key=="Threes": return self.threes()
      if key=="Fours":  return self.fours()
      if key=="Fives":  return self.fives()
      if key=="Sixes":  return self.sixes()

      if key=="Three of a Kind": return self.three_of_a_kind()
      if key=="Four of a Kind":  return self.four_of_a_kind()
      if key=="Full House":      return self.full_house()
      if key=="Small Straight":  return self.small_straight()
      if key=="Large Straight":  return self.large_straight()
      if key=="Yahtzee":         return self.yahtzee()
      if key=="Chance":          return self.chance()
