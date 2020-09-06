class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        min_sal = min(salary)
        max_sal = max(salary)
        total = sum(salary) - min_sal - max_sal
        average = total / (len(salary) - 2.0)
        return average
