class Solution(object):
    def isPowerOfTwo(self, n):
        
        if n == 1:
            return True
        elif n % 2 != 0 or n == 0:
            return False
        else:
            return self.isPowerOfTwo(n / 2)