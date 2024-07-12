'''
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

Example 1:
Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.

Example 2:
Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 
Constraints:
1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
'''


class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        str_x = "ab"
        str_y = "ba"

        if x > y:
            larger_score_str = str_x
            larger_score = x
            smaller_score_str = str_y
            smaller_score = y
        else:
            larger_score_str = str_y
            larger_score = y
            smaller_score_str = str_x
            smaller_score = x

        i = 0
        count_larger_score = 0
        count_smaller_score = 0

        while i < len(s) - 1:
            if s[i:i+2] == larger_score_str:
                s = s[:i] + s[i+2:]
                count_larger_score += larger_score
                i = max(i - 2, 0)  # Move back to handle overlapping pairs

            else:
                i += 1

        i = 0

        while i < len(s) - 1:
            if s[i:i+2] == smaller_score_str:
                s = s[:i] + s[i+2:]
                count_smaller_score += smaller_score
                i = max(i - 2, 0)  # Move back to handle overlapping pairs
            else:
                i += 1

        return count_larger_score + count_smaller_score


s = "aabbaaxybbaabb"
x = 5
y = 4
solution = Solution()
print(solution.maximumGain(s, x, y))
