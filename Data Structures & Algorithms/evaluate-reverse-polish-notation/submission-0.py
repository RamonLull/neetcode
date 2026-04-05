class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        intermediate_results = []
        OPERATORS = {
            '+': lambda y, x: x + y, '-': lambda y, x: x - y, 
            '*': lambda y, x: x * y, '/': lambda y, x: int(x / y)        
            }
        
        for token in tokens:
            if token in OPERATORS:
                intermediate_results.append(OPERATORS[token](
                    intermediate_results.pop(), intermediate_results.pop()
                ))
            else:   # token is a number
                intermediate_results.append(int(token))
        return intermediate_results[-1]