class Solution:
    def isValid(self, s: str) -> bool:
        correct_symb = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char in correct_symb.values():
                stack.append(char)
            elif char in correct_symb:
                if not stack or correct_symb[char] != stack.pop():
                    return False
            else:
                return False
        return len(stack) == 0


result = Solution()
print(result.isValid('()[]{}'))
print(result.isValid('(][){}'))
