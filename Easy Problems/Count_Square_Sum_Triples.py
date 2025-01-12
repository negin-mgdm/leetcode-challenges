'''
A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

Example 1:
Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).

Example 2:
Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
 
Constraints:
1 <= n <= 250
'''

import math


class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                k = math.isqrt(i**2 + j**2)  # Calculating k.
                # OR k = math.floor(math.sqrt(i**2 + j**2)) in older Python versions.
                if k <= n and i**2 + j**2 == k**2:  # Checking if k is valid.
                    count += 1

        return count


number = 5
solution = Solution()
print(solution.countTriples(number))
