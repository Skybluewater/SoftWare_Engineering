import unittest
from solve import Solvable
from OriginRequest import BiTree, QuestGenerator
from decimal import Decimal
from fractions import Fraction

class MyclassTest(unittest.TestCase):
    def setUp(self) -> None:
        self.question = QuestGenerator()
        self.solution = Solvable()
        self.tree = BiTree()

    def tearDown(self) -> None:
        pass

    def test_operadd(self):
        k = self.tree.getoperorder('+')
        self.assertEqual(k, 0)
        print("+ prior:")
        print(k)

    def test_opersub(self):
        k = self.tree.getoperorder('-')
        self.assertEqual(k, 0)
        print("- prior:")
        print(k)

    def test_opermul(self):
        k = self.tree.getoperorder('*')
        self.assertEqual(k, 2)
        print("* prior:")
        print(k)

    def test_operdiv(self):
        k = self.tree.getoperorder('/')
        self.assertEqual(k, 3)
        print("/ prior:")
        print(k)

    def test_operpow(self):
        k = self.tree.getoperorder('^')
        self.assertEqual(k, 4)
        print("^ prior:")
        print(k)

    def test_formatExpression(self):
        node1 = BiTree(0, 1)
        node2 = BiTree(0, 2)
        node3 = BiTree(1, 45)
        node3.set_rchild(node2)
        node3.set_lchild(node1)
        self.question.format_expression(node3)

    def test_changepowop1(self):
        k = self.question.changepowop('(5+5)^2', True)
        self.assertEqual(k, '(5+5)**2', "didn't switch pow operator")
        print("The result of changing pow operator")
        print(k)

    def test_changepowop2(self):
        k = self.question.changepowop('5^2', False)
        self.assertEqual(k, '5^2')

    def test_roundup1(self):
        k = self.question.round_up(10.822)
        self.assertEqual(k, Decimal('10.820'))
        print("result of rounding up 10.822")
        print(k)

    def test_roundup2(self):
        k = self.question.round_up(7.565)
        self.assertEqual(k, Decimal('7.57'))
        print("result of rounding up 7.565")
        print(k)

    def test_add1(self):
        k = self.solution.solve(2, 3, '+')
        self.assertEqual(k, 5)
        print("result of 2 add 3:")
        print(k)

    def test_add2(self):
        k = self.solution.solve(3/5, 11/7, '+')
        self.assertEqual(k, 76/35)
        print("result of 3/5 add 11/7:")
        print(k)

    def test_add3(self):
        k = self.solution.solve(6.66, 99.458, '+')
        self.assertEqual(k, 106.118)
        print("result of 6.66 add 99.458:")
        print(k)

    def test_sub1(self):
        k = self.solution.solve(10.87, 6.56, '-')
        self.assertEqual(k, -4.31)
        print("result of 6.56 sub 10.87:")
        print(k)

    def test_sub2(self):
        k = self.solution.solve(15/7, 9/13, '-')
        self.assertEqual(k, -132/91)
        print("result of 9/13 - 15/7:")
        print(k)

    def test_mul1(self):
        k = self.solution.solve(3, 4, '*')
        self.assertEqual(k, 12)
        print("result of 4 mul 3:")
        print(k)

    def test_mul2(self):
        k = self.solution.solve(-3, 4, '*')
        self.assertEqual(k, -12)
        print("result of 4 mul -3:")
        print(k)

    def test_mul3(self):
        k = self.solution.solve(11/3, 21/10, '*')
        self.assertEqual(k, 231/30)
        print("result of 21/10 mul 11/3")
        print(k)

    def test_mul4(self):
        k = self.solution.solve(1.68, 99.135, '*')
        self.assertEqual(k, 166.5468)
        print("result of 99.135 mul 1.68")
        print(k)

    def test_div1(self):
        k = self.solution.solve(4, 5, '/')
        self.assertEqual(k, 1.25)
        print("result of 5 div 4:")
        print(k)

    def test_div2(self):
        k = self.solution.solve(6, 7, '/')
        self.assertEqual(k, 7 / 6)
        print("result of 7 div 6:")
        print(k)

    def test_div3(self):
        k = self.solution.solve(1.26, 3.775, '/')
        self.assertEqual(round(k, 3), 2.996)
        print("result of 3.775 div 1.26:")
        print(k)

    def test_div4(self):
        k = self.solution.solve(13/5, 7/9, '/')
        self.assertEqual(k, 35/117)
        print("result of 7/9 div 13/5:")
        print(k)

    def test_div5(self):
        k = self.solution.solve(3, -4, '/')
        self.assertEqual(k, -4 / 3)
        print("result of -4 div 3:")
        print(k)

    def test_pow1(self):
        k = self.solution.solve(0.5, 4, '^')
        self.assertEqual(k, 2)
        print("result of 4^(1/2):")
        print(k)

    def test_pow2(self):
        k = self.solution.solve(Fraction(1, 3), 4, '^')
        self.assertEqual(k, 'not solvable')
        print("result of 3^4:")
        print(k)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test_operadd'))
    suite.addTest(MyclassTest('test_opersub'))
    suite.addTest(MyclassTest('test_opermul'))
    suite.addTest(MyclassTest('test_operdiv'))
    suite.addTest(MyclassTest('test_operpow'))
    suite.addTest(MyclassTest('test_formatExpression'))
    suite.addTest(MyclassTest('test_changepowop1'))
    suite.addTest(MyclassTest('test_changepowop2'))
    suite.addTest(MyclassTest('test_roundup1'))
    suite.addTest(MyclassTest('test_roundup2'))
    suite.addTest(MyclassTest('test_add1'))
    suite.addTest(MyclassTest('test_add2'))
    suite.addTest(MyclassTest('test_add3'))
    suite.addTest(MyclassTest('test_sub1'))
    suite.addTest(MyclassTest('test_sub2'))
    suite.addTest(MyclassTest('test_mul1'))
    suite.addTest(MyclassTest('test_mul2'))
    suite.addTest(MyclassTest('test_mul3'))
    suite.addTest(MyclassTest('test_mul4'))
    suite.addTest(MyclassTest('test_div1'))
    suite.addTest(MyclassTest('test_div2'))
    suite.addTest(MyclassTest('test_div3'))
    suite.addTest(MyclassTest('test_div4'))
    suite.addTest(MyclassTest('test_div5'))
    suite.addTest(MyclassTest('test_pow1'))
    suite.addTest(MyclassTest('test_pow2'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
