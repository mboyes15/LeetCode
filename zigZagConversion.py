class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        i = 0
        display = [[] for _ in range(numRows)]
        n = len(s)
        
        # base case
        if numRows == 1:
            return s

        while i < n:
            for down in range(numRows):
                if i < n:
                    display[down].append(s[i])
                    i+=1
            for up in range(numRows - 2, 0, -1):
                if i < n:
                    display[up].append(s[i])
                    i+=1
    
        ans = ""
        for row in display:
            ans += ''.join(row)
        return ans
    
