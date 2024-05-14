def check_delimiters(s: str) -> str:
    stack = []
    matching_pairs = {')': '(', ']': '[', '}': '{'}
   
    for char in s:
        if char in matching_pairs.values():
            stack.append(char)
        elif char in matching_pairs.keys():
            if stack and stack[-1] == matching_pairs[char]:
                stack.pop()
            else:
                return "Несиметрично"
   
    return "Симетрично" if not stack else "Несиметрично"


# Приклади використання:
print(check_delimiters("( ){[ 1 ]( 1 + 3 )( ){ }}"))
print(check_delimiters("( 23 ( 2 - 3);"))            
print(check_delimiters("( 11 }"))               