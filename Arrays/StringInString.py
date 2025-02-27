def strStr(self, haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
        return -1
    l, r = 0, len(needle) - 1
    while r < len(haystack):
        if haystack[l : r + 1] == needle:
            return l
        else:
            l += 1
            r += 1
    return -1

strStr("hello", "ll") # 2

'''
## Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''
