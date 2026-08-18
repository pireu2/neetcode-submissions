class Solution:
    def isValid(self, s: str) -> bool:
        open_par = "{[("
        stack = []
        for c in s:
            if c in open_par:
                stack.append(c)
            else:
                if not stack:
                    return False
                
                top_stack = stack.pop()
                if (c == ")" and top_stack != "(") or (c == "]" and top_stack != "[") or (c == "}" and top_stack != "{"):
                    return False

        return not stack