class Solution(object):
    def judgeCircle(self, moves):
        horizontal_move = 0
        vertical_move = 0
        for move in moves:
            if move == "U":
                vertical_move += 1
            elif move == "D":
                vertical_move -= 1
            elif move == "R":
                horizontal_move += 1
            else:
                horizontal_move -= 1
        if horizontal_move == 0 and vertical_move == 0:
            return True
        else:
            return False