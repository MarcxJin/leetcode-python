class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        traceDict = {"L":0, "R":0, "U":0, "D":0}
        for move in moves:
            traceDict[move] += 1
        return True if traceDict["L"] == traceDict["R"] and traceDict["U"] == traceDict["D"] else False