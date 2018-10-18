class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        signed = [-1,1][x > 0]
        rvs = int(str(abs(x))[::-1])
        return [signed*rvs, 0][rvs > 2**31 - 1]