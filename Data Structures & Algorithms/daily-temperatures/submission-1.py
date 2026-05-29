class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans = list()

        for i in range(len(temp)):
            found = False
            counter = 1
            add = 1
            while not found and add + i < len(temp):
                if temp[i] < temp[i+add]:
                    found = True
                    break
                else: add += 1

            if found: ans.append(add)
            else: ans.append(0)

        return ans