class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operators:
                b = stack.pop()  
                a = stack.pop()  

                match token:
                    case "+":
                        result = a + b
                    case "-":
                        result = a - b
                    case "*":
                        result = a * b
                    case "/":
                        result = int(a / b)

                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]