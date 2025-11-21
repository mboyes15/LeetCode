class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # to make better follow steps rather than looping through entire string
        # first get rid of all the whitespace
        # then check for sign
        # then initiate digits and anything else stops the program

        result = 0
        counter = 0
        sign = 1


        for character in s:
            if character.isdigit() == False:
                if counter == 0:
                    if character == "-":
                        sign = -1
                    elif character == "+":
                        sign = 1
                    # skip leading whitespace
                    elif character == " ":
                        counter -= 1
                    else:
                        return sign * result
                else:
                    return sign * result
            else:
                result = result * 10 + int(character)

                # check for overflow 
                if 2**31 -1 < sign*result or sign*result < -2**31:
                    if sign==-1:
                        return -2**31
                    else:
                        return 2**31 - 1
            counter += 1

        return sign * result