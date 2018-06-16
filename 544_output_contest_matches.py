class Solution:
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        team = [str(i) for i in range(1, n+1)]
        
        while len(team) > 1:
            n = len(team)
            for i in range(n//2):
                team[i] = "(" + team[i] + "," + team.pop() + ")"
        return team[0]