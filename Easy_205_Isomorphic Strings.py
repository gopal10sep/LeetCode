# 205. Isomorphic Strings
# Easy

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true
 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.



class Solution(object):
    def isIsomorphic(self, s: str, t: str) -> bool:
        charmap_s = {}
        charmap_t = {}
        
        for i in range(0,len(s)):
            if s[i] in charmap_s and charmap_s[s[i]] != t[i]:
                return False
            if t[i] in charmap_t and charmap_t[t[i]] != s[i]:
                return False
            charmap_s[s[i]] = t[i]
            charmap_t[t[i]] = s[i]
        return True

	def isIsomorphic01(self, s, t):
		zipped_set = set(zip(s, t))
        return len(zipped_set) == len(set(s)) == len(set(t))






    
    def isIsomorphic1(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())
        
    def isIsomorphic2(self, s, t):
        d1, d2 = [[] for _ in xrange(256)], [[] for _ in xrange(256)]
        for i, val in enumerate(s):
            d1[ord(val)].append(i)
        for i, val in enumerate(t):
            d2[ord(val)].append(i)
        return sorted(d1) == sorted(d2)
    
    def isIsomorphic3(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
    
    def isIsomorphic4(self, s, t): 
        return [s.find(i) for i in s] == [t.find(j) for j in t]
    

    def isIsomorphic6(self, s, t):
        d1, d2 = [0 for _ in xrange(256)], [0 for _ in xrange(256)]
        for i in xrange(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i+1
            d2[ord(t[i])] = i+1
        return True