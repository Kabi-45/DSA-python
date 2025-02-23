# with int -> str conversion
def isPalindrome1(self, x: int) -> bool:
    x = str(x)
    i, j = 0, len(x) -1 
    while i < j:
        if x[i] != x[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

# without int -> string conversion
def isPalindrome2(self, x: int) -> bool:
    if x < 0:
        return False
    temp = x
    reverse = 0
    while temp != 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10
    return reverse == x


'''
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
'''
