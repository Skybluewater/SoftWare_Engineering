from fractions import Fraction


class solvable:

    prior = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2, '(': -1}

    def solve(self,num1,num2,operator,if_fraction):
        if operator=='+':
            return num1+num2
        elif operator=='-':
            return num2-num1
        elif operator=='/':
            if num1==0:
                return 'not solvable'
            if if_fraction:
                return Fraction(num2, num1)
            return num2/num1
        elif operator == '*':
            return num2*num1
        elif operator == '^' or operator == '**':
            return pow(num2, num1)

    def Calculator(self, line, if_fraction):
        opt = []
        data = []
        i = 0
        while i < len(line):
            start = i
            if line[i] == '(':
                if line[i + 1] == '-':
                    i += 1
                    while line[i + 1].isdigit() and i + 1 < len(line):
                        i += 1
                    data.append(int(line[start + 1:i + 1]))
                    i += 1
                else:
                    opt.append(line[i])
            elif line[i].isdigit():
                while i + 1 < len(line) and line[i + 1].isdigit():
                    i += 1
                data.append(int(line[start:i + 1]))
            elif line[i] == ')':
                while opt[-1] != '(':
                    k = self.solve(data.pop(), data.pop(), opt.pop(), if_fraction)
                    if k == 'not solvable':
                        return 'not solvable'
                    data.append(k)
                opt.pop()
            else:
                while opt and self.prior[line[i]] <= self.prior[opt[-1]]:
                    k = self.solve(data.pop(), data.pop(), opt.pop(), if_fraction)
                    if k == 'not solvable':
                        return 'not solvable'
                    data.append(k)
                opt.append(line[i])
            i += 1
        while opt:
            k = self.solve(data.pop(), data.pop(), opt.pop(), if_fraction)
            if k == 'not solvable':
                return 'not solvable'
            data.append(k)
        return data.pop()
