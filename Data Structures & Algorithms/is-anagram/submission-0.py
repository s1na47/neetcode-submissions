class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if different lengths, its impossible
        if len(s) != len(t):
            return False
        #create the two dictionaries(clipboards)
        count_s = {}
        count_t = {}

        #go through every letter and keep a tally
        for i in range(len(s)):
            #get() is a safe way to check a dictionary
            #it says "get the current count, but if the letter isnt there yet, use 0"
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        return count_s == count_t