def isValid(s: str) -> bool:
    # Initialize a stack to keep track of opening brackets
    stack = []
    # Mapping of closing to opening brackets
    mapping = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the string
    for char in s:
        if char in mapping.values():  # If it's an opening bracket
            stack.append(char)
        elif char in mapping:  # If it's a closing bracket
            # Check if stack is empty or top of stack does not match
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False  # Invalid character (not expected based on constraints)

    # Return True if stack is empty (all brackets matched)
    return not stack







    



  

