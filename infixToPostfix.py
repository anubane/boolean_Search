##########################################
##-----------Anurag Banerjee------------##
##---------------CS 7030----------------##
##-----------  Assignment 3  -----------##
##########################################

# Code based on infox to postfix conversion code available on geeksforgeeks
class Conversion:

    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used as a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'not': 3, 'and': 2, 'or': 1}     # larger number means higher priority

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def isOperand(self, ch):
        return True if ch not in ('(', ')', 'and', 'or', 'not') else False

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):

        # Iterate over the expression for conversion
        for i in exp:
            # If the character is an operand,
            # add it to output
            if self.isOperand(i):
                self.output.append(i)

            # If the character is an '(', push it to stack
            elif i == '(':
                self.push(i)

            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == ')':
                while (not self.isEmpty()) and self.peek() != '(':
                    a = self.pop()
                    self.output.append(a)
                if not self.isEmpty() and self.peek() != '(':
                    return -1
                else:
                    self.pop()

            # An operator is encountered
            else:
                while not self.isEmpty() and self.notGreater(i):
                    self.output.append(self.pop())
                self.push(i)

        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())

        return self.output


if __name__ == '__main__':
    # Driver program to test above function
    exp = "( this and that and bell or monday ) or not ( ( bill or murray ) and murphy )".split()
    obj = Conversion(len(exp))
    print obj.infixToPostfix(exp)

# EOF
