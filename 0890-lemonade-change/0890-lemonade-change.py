class Solution(object):
    def lemonadeChange(self, bills):
        five = 0
        ten = 0
        twenty = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10 and five > 0:
                ten += 1
                five -= 1
            elif i == 20:
                if (five >= 1 and ten >= 1):
                    twenty += 1
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    twenty += 1
                    five -= 3
                else:
                    return False
            else:
                return False
        return True

        