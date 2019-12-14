

class solvable:

    prior = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2, '(': -1}

    def solve(self,num1,num2,operator):
        if operator=='+':
            return num1+num2
        elif operator=='-':
            return num2-num1
        elif operator=='/':
            if num1==0:
                exit('not solvable')
            return num2/num1
        elif operator=='*':
            return num2*num1
        elif operator=='^':
            return pow(num2,num1)

    def Calculator(self):
        r = open("out.txt", "r", encoding='utf8')
        lines = r.readlines()
        for line in lines:
            opt=[]
            data=[]
            i=0
            while i < len(line)-1:
                start=i
                if line[i]=='(':
                    if line[i+1]=='-':
                        i+=1
                        while line[i+1].isdigit() and i+1<len(line):
                            i+=1
                        data.append(int(line[start+1:i+1]))
                        i+=1
                    else:
                        opt.append(line[i])
                elif line[i].isdigit():
                    while i+1<len(line) and line[i+1].isdigit():
                        i+=1
                    data.append(int(line[start:i+1]))
                elif line[i]==')':
                    while opt[-1]!='(':
                        data.append(self.solve(data.pop(),data.pop(),opt.pop()))
                    opt.pop()
                else:
                    while opt and self.prior[line[i]] <= self.prior[opt[-1]]:
                        data.append(self.solve(data.pop(),data.pop(),opt.pop()))
                    opt.append(line[i])
                i+=1
            while opt:
                data.append(self.solve(data.pop(), data.pop(), opt.pop()))
            print('{:g}'.format(data.pop()))

