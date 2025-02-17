class Solution(object):
    def calPoints(self, operations):
        record = []
        for operation in operations:
            if(operation == "+"):
                if len(record) >= 2:
                    record.append(record[-1] + record[-2])
            elif(operation == "D"):
                record.append(2 * record[-1])
            elif(operation == "C"):
                record.pop()
            else:
                record.append(int(operation))
        return sum(record)
        