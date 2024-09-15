'''
Given an array arr of integers, check if there exist two indices i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 
Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 
Constraints:
2 <= arr.length <= 500
-103 <= arr[i] <= 103
'''


class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen_nums = set()
        for num in arr:
            # Check if double of the number or half of the number is already in the set.
            if 2 * num in seen_nums or (num % 2 == 0 and num // 2 in seen_nums):
                return True
            seen_nums.add(num)
        return False


arr = [7, 1, 14, 11]
solution = Solution()
print(solution.checkIfExist(arr))
