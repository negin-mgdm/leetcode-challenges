class Solution:
    def convertTemperature(self, celsius):
        temp = []
        temp.append(celsius + 273.15)
        temp.append(celsius * 1.80 + 32.00)

        return temp


celsius = Solution()
degree = celsius.convertTemperature(10.56)

degree_formatted = list(map(lambda x: '{:.5f}'.format(x), degree))

print(degree_formatted)
