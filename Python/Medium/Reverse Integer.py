class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        result = 0
        
        if x < 0:
            sign = -1
            x *= -1
        else:
            sign = 1
        
        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x //= 10
        
        result *= sign
        
        if result < INT_MIN or result > INT_MAX:
            return 0
        
        return result
