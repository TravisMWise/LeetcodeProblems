class Solution:
    """
    Given two binary strings a and b, return their sum as a binary string.
    Example 1:
        Input: a = "11", b = "1"
        Output: "100"
    """
    def addBinary(self, a: str, b: str) -> str:
        a = int(a)
        b = int(b)
        carry = 0
        final = 0; count = 0
        while a > 0 or b > 0:
            d1 = a % 10 # First digit
            a = a // 10 # A minus the first digit
            d2 = b % 10
            b = b // 10

            res = d1 + d2 + carry
            if res == 3:
                carry = 1
                res = 1
            elif res == 2:
                carry = 1
                res = 0
            elif res == 1:
                carry = 0
                res = 1
            else:
                res = 0
                carry = 0
            final += res * 10 ** count
            count += 1
        if carry == 1:
            final += 1 * 10 ** count
        final = str(final)
        return final