class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_values = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC" : 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        result = [] 
        # get items into descending order
        items = sorted(roman_values.items(), key=lambda kv: kv[1], reverse=True)
        for sym, val in items:
            if num > 0:
                big = 0
                # Understand how many of the symbol to insert if at all
                big = int(num / val)
                if big>=1:
                    for i in range(0,big):
                        result.append(sym)
                        num = num % val 
                else:
                    continue
        return "".join(result)
                    
          