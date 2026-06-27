class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #1. Put my left finger on the first number (index 0)
        L = 0

        #2. Put my right finger on the last number (length of list minus 1)
        R = len(numbers) - 1

        #3. Keep repeating as long as my fingers haven't crossed
        while L<R:

            #4. Add the numbers my fingers are currently pointing at
            current_sum = numbers[L] + numbers[R]

            #5. If it's a match, return the positions
            if current_sum == target:
                return [L + 1, R+1] # (+1 because the problem asks for 1-based indexing, not 0-based)

            #6. If the sum is TOO BIG, move the Right finger left
            elif current_sum > target:
                    R -= 1

            #7. If the sum is TOO SMALL, move the Left finger right
            else:
                    L+= 1