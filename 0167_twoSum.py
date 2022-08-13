class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
        return [i+1, j+1]

# Alternative solution
    
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, number in enumerate(numbers):
            if number not in hashmap:
                hashmap[target-number] = i + 1
            else:
                return [hashmap[number], i + 1]
