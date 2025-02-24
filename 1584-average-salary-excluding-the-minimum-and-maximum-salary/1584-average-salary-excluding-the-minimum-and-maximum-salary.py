class Solution(object):
    def average(self, salary):
        salary = sorted(salary)
        return sum(salary[1:-1]) / float((len(salary) - 2))
        