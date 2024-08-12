'''
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
 
Constraints:
1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
'''

# First Solution:
from collections import Counter


class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        words1 = s1.split()
        words2 = s2.split()

        arr = words1 + words2

        count = Counter(arr)

        uncommon_words = []
        for key, value in count.items():
            if value == 1:
                uncommon_words.append(key)

        return uncommon_words


s1 = "apple apple"
s2 = "banana"
solution = Solution()
print(solution.uncommonFromSentences(s1, s2))

# Second solution:


class Solution(object):
    def uncommonFromSentences1(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        words1 = s1.split()
        words2 = s2.split()

        arr = words1 + words2

        count = {}

        for word in arr:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

        uncommon_words = []
        for key, value in count.items():
            if value == 1:
                uncommon_words.append(key)

        return uncommon_words


s1 = "apple apple"
s2 = "banana"
solution = Solution()
print(solution.uncommonFromSentences1(s1, s2))
