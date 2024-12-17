'''
Given a string s, check if it can be constructed by taking a substring of it and 
appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 
Constraints:
1 <= s.length <= 104
s consists of lowercase English letters.
'''


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Creating a new string by doubling 's' and removing the first and last characters.
        doubled_s = (s + s)[1:-1]
        # If 's' exists in this new string, it means 's' can be formed by repeating a substring.
        if s in doubled_s:
            return True

        return False


s = "abcabcabcabc"
solution = Solution()
print(solution.repeatedSubstringPattern(s))
