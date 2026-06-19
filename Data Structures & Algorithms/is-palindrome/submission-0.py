class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Setup our two pointers
        L = 0                 # Left finger starts at index 0
        R = len(s) - 1        # Right finger starts at the very end

        # 2. Keep checking until the fingers cross in the middle
        while L < R:
            
            # 3. Skip non-letters on the Left
            while L < R and not s[L].isalnum():
                L += 1
                
            # 4. Skip non-letters on the Right
            while L < R and not s[R].isalnum():
                R -= 1
                
            # 5. Compare the letters (make them both lowercase to be safe)
            if s[L].lower() != s[R].lower():
                return False # We found a mismatch! It's not a palindrome.
            
            # 6. If they match, move both fingers inward
            L += 1
            R -= 1
            
        # 7. If the fingers crossed and we never returned False, it's a palindrome!
        return True