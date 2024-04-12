'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
 
Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        sentence = s.lower()
        for i in range(len(sentence)):
            if sentence.count(sentence[i]) == 1:
                return i
        return -1


s = "LeetCode"
char_index = Solution().firstUniqChar(s)
print(char_index)
