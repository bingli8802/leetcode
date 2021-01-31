from random import choice
class RandomizedSet():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.li = []

        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dic:
            return False
        self.dic[val] = len(self.li)
        self.li.append(val)
        print self.dic, self.li
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dic:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.li[-1], self.dic[val]
            self.li[idx], self.dic[last_element] = last_element, idx
            # delete the last element
            self.li.pop()
            del self.dic[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        """
        return choice(self.li)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
