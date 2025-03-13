# Time O(n)
# Space O(n)
class Solution:
    def calculate(self, s: str) -> int:
        # using stack
        stack = []
        n = len(s)
        currNum = 0
        lastOperand = '+'
        for i in range(n):
            if s[i].isdigit():
                currNum = currNum * 10 + int(s[i])
                
            if (not s[i].isdigit() and s[i] != ' ') or i == n-1:
                if lastOperand == '+':
                    stack.append(currNum)
                if lastOperand == '-':
                    stack.append(-currNum)
                if lastOperand == '*':
                    stack.append(stack.pop() * currNum)
                if lastOperand == '/':
                    stack.append(int(stack.pop() / currNum))
                currNum = 0
                lastOperand = s[i]
        result = 0
        for num in stack:
            result += num
        return result

# without stack
# Time O(n)
# Space O(1)
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        currNum = 0
        lastOperand = '+'
        tail = 0
        calc = 0
        for i in range(n):
            if s[i].isdigit():
                currNum = currNum * 10 + int(s[i])
                
            if (not s[i].isdigit() and s[i] != ' ') or i == n-1:
                if lastOperand == '+':
                    calc += currNum
                    tail = currNum
                if lastOperand == '-':
                    calc += -currNum
                    tail = -currNum
                if lastOperand == '*':
                    calc = calc - tail + tail * currNum
                    tail = tail * currNum
                if lastOperand == '/':
                    calc = calc - tail + int(tail / currNum)
                    tail = int(tail / currNum)
                currNum = 0
                lastOperand = s[i]
        return calc

        
        