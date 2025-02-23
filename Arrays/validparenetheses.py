def isValid(self, s: str) -> bool:
    stack = []
    parentheses = {
        ')' : '(',
        ']' : '[',
        '}' : '{',
    }
    for char in s:
        if char in '([{': #push(append) opening bracket into stack(list)
            stack.append(char)
        else: # conditions for closing brackets
            if not stack or stack[-1] != parentheses[char]:
                #if stack is empty -> no opening parentheses
                #OR no matching parentheses found
                return False
            else:
                stack.pop() # remove last element from the stack as the condition meets
    return len(stack) == 0 #condition for checking if there is no closing brackets

print(isValid("()"))      # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))      # False
print(isValid("{[]}"))    # True
print(isValid("([)]"))    # False
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
