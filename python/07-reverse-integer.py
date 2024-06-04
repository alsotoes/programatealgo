class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -1*pow(2,31) <= x < 0:
            reversed_int = int(str(abs(x))[::-1])*-1
        elif 0 <= x < pow(2,31)-1:
            reversed_int = int(str(x)[::-1])
        else:
            reversed_int = 0
        
        return 0 if reversed_int.bit_length() > (32-1) else reversed_int
