class Solution(object):
    def calPoints(self, operations):
        record = []
        for operation in operations:
            if(operation == "+" and len(record) >= 2):
                record.append(record[-1] + record[-2])
            elif(operation == "D" and len(record) >= 1):
                record.append(2 * record[-1])
            elif(operation == "C" and len(record) >= 1):
                record.pop()
            else:
                record.append(int(operation))
        return sum(record)
        