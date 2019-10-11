class string_sol:
    def valid_parenthesis(self, str1):
        stack, pchar = [], {"(":")", "{":"}", "[":"]"}
        for a in str1:
            if a in pchar:
                stack.append(a)
            elif len(stack) == 0 or pchar[stack.pop()] != a:
                return False
        return len(stack) == 0
print(string_sol().valid_parenthesis("(){}[]"))
print(string_sol().valid_parenthesis("()[}}}"))
