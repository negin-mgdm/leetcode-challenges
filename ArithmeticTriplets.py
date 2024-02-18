class Solution:
    def arithmeticTriplets(self, nums, diff):
        triplets = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if [i] < [j] < [k]:
                        if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                            triplets.append((i, j, k))
        return triplets


solution = Solution()

nums = [0, 1, 4, 6, 7, 10]
diff = 3

output = solution.arithmeticTriplets(nums, diff)

output_count = 0

for item in output:
    if isinstance(item, tuple):
        output_count += 1

print(output_count)
