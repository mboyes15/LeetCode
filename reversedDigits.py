class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        reversedOutput = 0

        # Base case: a single digit
        if 0 <= x < 10 or -10 < x <= 0:
            return x

        # remove the 0 at the end if there is one
        if x % 10 == 0:
            x /= 10

        temp_num = abs(x)  # Handle negative numbers by taking absolute value
        while temp_num > 0:
            last_digit = temp_num % 10
            temp_num //= 10
            reversedOutput = reversedOutput * 10 + last_digit

            # check for overflow 
            if reversedOutput > 2**31 -1:
                return 0

        if negative:
            return -reversedOutput
        
        return reversedOutput
