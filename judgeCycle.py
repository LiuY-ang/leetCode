class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        #分别统计向右，左，上，下走出现的次数
        rmoves=moves.count("R")
        lmoves=moves.count("L")
        umoves=moves.count("U")
        dmoves=moves.count("D")
        print rmoves,lmoves,umoves,dmoves
        if rmoves==lmoves and umoves==dmoves:#如果左，右出现的次数相等，并且上，下出现的次数相等
            return True#那么返回true
        return False
