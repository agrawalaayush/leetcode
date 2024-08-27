class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        keys = s.strip().split(" ")
        return len(keys[-1])
        