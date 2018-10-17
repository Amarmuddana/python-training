class Solution(object):
    def numJewelsInStones(self, J, S):
        ":type J: str"
        ":type S: str"
        ":rtype: int"

        j_list = list(J)
        S_list = list(S)
        jewels = set(S_list) - set(j_list)
        return sum(s in J for s in S)