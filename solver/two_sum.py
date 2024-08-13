"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

 
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109

Only one valid answer exists.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
            
# Exemplo de uso
if __name__ == "__main__":
    # Instancia a classe Solution
    solution = Solution()
    
    # Define uma lista de números e o alvo
    nums = [2, 7, 11, 15]
    target = 9
    
    # Chama o método twoSum e imprime o resultado
    resultado = solution.twoSum(nums, target)
    
    # Exibe os índices dos números que somam ao alvo
    print(f"Índices dos números que somam {target}: {resultado}")