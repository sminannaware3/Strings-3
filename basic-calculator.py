import math
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s = s.strip()
        n = len(s)
        currNum = 0
        lastOperand = '+'
        for i in range(n):
            if s[i].isdigit():
                currNum = currNum * 10 + int(s[i])
                if i == n-1: self.addNum(stack, lastOperand, currNum)
            elif s[i] == '(':
                self.addNum(stack, lastOperand, 1)
                stack.append(math.inf)
                lastOperand = '+'
            elif s[i] == ')':
                self.addNum(stack, lastOperand, currNum)
                currSum = 0
                while stack[-1] != math.inf:
                    currSum += stack.pop()
                stack.pop() # popping '('
                lastOperand = stack.pop() # popping operand before '('
                stack.append(lastOperand * currSum)
                currNum = 0
            elif (s[i] != ' '):
                self.addNum(stack, lastOperand, currNum)
                currNum = 0
                lastOperand = s[i]
        result = 0
        for num in stack:
            result += num
        return result
    
    def addNum(self, stack: [int], operand: str, num: int):
        if operand == '+':
            stack.append(num)
        else:
            stack.append(-num)