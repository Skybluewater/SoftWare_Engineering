import OriginRequest as QR

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
    with open('out.txt', 'w', encoding='utf-8') as f:
        for out in g.output_list:
            f.write(out + '\n')
