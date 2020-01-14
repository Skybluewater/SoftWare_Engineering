import OriginRequest as QR

if __name__ == '__main__':
    g = QR.QuestGenerator()
    g.generate(quantity=1000, operators=5, if_false=True, if_pow=True,
               if_fraction=True, Pow_Operator=True, Max=9)
    with open('out.txt', 'w', encoding='utf-8') as f:
        for out in g.output_list:
            f.write(out + '\n')
