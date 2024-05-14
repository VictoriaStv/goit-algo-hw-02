from collections import deque


def is_palindrome(s: str) -> bool:
    s = s.lower()
    filtered_chars = deque()
    for char in s:
        if char.isalnum():
            filtered_chars.append(char)
   
    while len(filtered_chars) > 1:
        if filtered_chars.popleft() != filtered_chars.pop():
            return False
    return True


# Приклади використання:
print(is_palindrome("Я несу гусеня"))  
print(is_palindrome("Радар"))          
print(is_palindrome("Слава Україні"))  
print(is_palindrome("Героям слава"))  
