import OriginRequest as QR
import sys
from solve import solvable

if __name__ == '__main__':
    quantity=input('quantity:')
    operators=input('operator nums:')
    if_false=input('negative operands:')
    if_pow=input('pow operators:')
    Max=input('Max nums:')
    g = QR.QuestGenerator()
    g.generate(quantity=int(quantity), operators=int(operators), if_false=int(if_false), if_pow=int(if_pow), Max=int(Max))
    with open('out.txt', 'w', encoding='utf-8') as f:
        for out in g.output_list:
            f.write(out + '\n')
