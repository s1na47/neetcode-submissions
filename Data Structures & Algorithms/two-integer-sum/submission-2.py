class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Create our blank "Notepad"
        # Format will be -> { number_value : index_position }
        seen = {}

        # 2. Walk down the aisle one box at a time
        for index, num in enumerate(nums):
            # 3. The Math: What box do I need to reach the target?
            difference = target - num
            # 4. Check the Notepad
            if difference in seen:
                # We found it! Return the position from the notepad, and our current position
                return [seen[difference], index]
                # 5. If we didn't find it, write our current box on the notepad and keep walking
            seen[num] = index
        return [] # (Just in case no answer exists, though LeetCode guarantees there is one)