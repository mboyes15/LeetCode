class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # pS = 0
        # pP = 0
        # preceding = ''

        # Base Case
        # If the pattern is empty, then the string s must also be empty to match.
        if not p:
            return not s
        #  first_match is True if:
                # s is not empty
                # AND the first character of pattern p either:
                # equals the first character of s
                # OR is a dot .
        first_match = bool(s) and p[0] in {s[0],'.'}

        if len(p)>= 2 and p[1] == "*":
            return (
                self.isMatch(s, p[2:])
                or first_match
                and self.isMatch(s[1:], p)
           )
        else:
            return first_match and self.isMatch(s[1:],p[1:])
