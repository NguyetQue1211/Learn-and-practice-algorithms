"""
    Given two strings s and t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving 
    the order of characters. No two characters may map to the same character, but a character may map to itself.
    
    Example 1: 
        Input: s = "egg", t = "add"
        Output: true
    
    Example 2: 
        Input: s = "foo", t = "bar"
        Output: false
    
    Example 3: 
        Input: s = "paper", t = "title"
        Output: true
    
    Constraints:
        1 <= s.length <= 5 * 10^4
        t.length == s.length
        s and t consist of any valid ascii character.
    
    Credit: 
    This prompt is belong to leetcode study plan named: leetcode 75
    
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        result = True
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in s_dict:
                    if s_dict[s[i]] != t[i]:
                         result = False
                s_dict[s[i]] = t[i]
        else: 
            result = False
        return result