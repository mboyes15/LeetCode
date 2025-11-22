class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # VERSION 1:
        # p1 = 0
        # p2 = len(str(x))-1
        # # due to the - sign
        # if x < 0:
        #     return False
        
        # while p1 < p2:
        #     if str(x)[p1] != str(x)[p2]:
        #         return False
        #     p1 +=1
        #     p2 -= 1
        # return True 

        # VERSION 2 (using maths):
        if x < 0:
            return False   

        x1 = x
        reverse = 0
        while x1>0:
            digit = x1 % 10
            reverse = reverse * 10 + digit
            x1 //=10

        if reverse == x:
            return True

        return False