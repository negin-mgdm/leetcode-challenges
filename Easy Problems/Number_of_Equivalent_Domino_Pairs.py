'''
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), 
or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.
Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Example 1:
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

Example 2:
Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
 
Constraints:
1 <= dominoes.length <= 4 * 104
dominoes[i].length == 2
1 <= dominoes[i][j] <= 9
'''


from collections import defaultdict


class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        counts = defaultdict(int)
        result = 0

        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            result += counts[key]
            counts[key] += 1

        return result


dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
solution = Solution()
print(solution.numEquivDominoPairs(dominoes))
