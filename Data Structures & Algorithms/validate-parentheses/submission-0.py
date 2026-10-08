class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary for characters in s
        pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stack = []

        for char in s:
            if char in pairs:
                # Store opening brackets
                stack.append(char)
            
            else:
                # Closing bracket needs an opening bracket
                if not stack:
                    return False

                opening = stack[-1]

                if pairs[opening] != char:
                    return False

                # remove the matched opening
                stack.pop()
        
        return not stack
            








        