from Software_Engineering import OriginRequest as QR


def answer(quantity: int, list: list, if_fraction=0):
    i = 0
    correct = 0
    while i < list.__len__():
        if i % 2 == 0:
            print(list[i], '=')
        else:
            if if_fraction:
                st = input('answer:')
                if st == list[i]:
                    correct += 1
                else:
                    print('uncorrect')
            else:
                st = input('answer:')
                st = float(st)
                if st == float(list[i]):
                    correct = correct + 1
                else:
                    print('uncorrect')
        i = i + 1
    print('correct num', correct)
    print('wrong num', quantity - correct)


if __name__ == '__main__':
    quantity = input('quantity:')
    operators = input('operator nums:')
    if_false = input('negative operands:')
    if_pow = input('pow operators:')
    if_fraction = input('fraction present:')
    Pow_Operand = input('Pow_Operator:')
    Max = input('Max nums:')
    g = QR.QuestGenerator()
    g.generate(quantity=int(quantity), operators=int(operators), if_false=int(if_false), if_pow=int(if_pow),
               if_fraction=int(if_fraction), Pow_Operator=int(Pow_Operand), Max=int(Max))
    answer(int(quantity),g.output_list,int(if_fraction))
    with open('out.txt', 'w', encoding='utf-8') as f:
        for out in g.output_list:
            f.write(out + '\n')
