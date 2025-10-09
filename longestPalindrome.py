class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def checkPalindrome(i,j):

            while i < j-1:
                if s[i]!=s[j-1]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True
    
        # As wanting max length then only check big palindromes before small ones
        length  = len(s)
        for length in range(len(s),0,-1):
            for start in range(len(s)-length+1):
                if checkPalindrome(start, start+length):
                    return s[start:start+length]

        return ""
