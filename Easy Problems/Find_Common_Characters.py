'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''


class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common_chars = []

        for char in words[0]:
            is_common_char = True
            for i, word in enumerate(words):
                if char not in word:
                    is_common_char = False
                words[i] = words[i].replace(char, "", 1)
            if is_common_char:
                common_chars.append(char)

        return common_chars


words = ["cool", "lock", "cook"]
solution = Solution()
print(solution.commonChars(words))
