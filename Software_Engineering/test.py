import unittest
from Software_Engineering.solve import solvable
from Software_Engineering.OriginRequest import BiTree, QuestGenerator
from decimal import Decimal
from fractions import Fraction


class MyclassTest(unittest.TestCase):
    def setUp(self) -> None:
        self.question = QuestGenerator()
        self.solution = solvable()
        self.tree = BiTree()

    def tearDown(self) -> None:
        pass

    def test_ques1(self):
        ret = self.question.generate(10, 5, 0, 0, 0, 9)
        print("generate questions")
        print(ret)

    def test_ques2(self):
        ret = self.question.generate(10, 5, 1, 0, 0, 9)
        print("generate questions")
        print(ret)

    def test_ques3(self):
        ret = self.question.generate(10, 5, 0, 1, 0, 9)
        print("generate questions")
        print(ret)

    def test_ques4(self):
        ret = self.question.generate(10, 5, 0, 0, 1, 9)
        print("generate questions")
        print(ret)

    def test_ques5(self):
        ret = self.question.generate(5, 8, 0, 0, 0, 15)
        print("generate questions")
        print(ret)

    def test_ques6(self):
        ret = self.question.generate(1000, 5, 1, 1, 1, 9)
        print("generate questions")
        print(ret)

    def test_changePowOp(self):
        k = self.question.changePowOp('(5+5)^2', True)
        self.assertEqual(k, '(5+5)**2', '没有转换乘方符')
        print("The result of changing pow operator")
        print(k)

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

    def test_operadd(self):
        k = self.tree.getOperOrder('+')
        self.assertEqual(k, 0)
        print("+ prior:")
        print(k)

    def test_opersub(self):
        k = self.tree.getOperOrder('-')
        self.assertEqual(k, 0)
        print("- prior:")
        print(k)

    def test_opermul(self):
        k = self.tree.getOperOrder('*')
        self.assertEqual(k, 2)
        print("* prior:")
        print(k)

    def test_operdiv(self):
        k = self.tree.getOperOrder('/')
        self.assertEqual(k, 3)
        print("/ prior:")
        print(k)

    def test_operpow(self):
        k = self.tree.getOperOrder('^')
        self.assertEqual(k, 4)
        print("^ prior:")
        print(k)

    def test_add1(self):
        k = self.solution.solve(2, 3, '+')
        self.assertEqual(k, 5)
        print("result of 2 add 3:")
        print(k)

    def test_add2(self):
        k = self.solution.solve(3 / 5, 11 / 7, '+')
        self.assertEqual(k, 76 / 35)
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
        self.assertEqual(k, 7/6)
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
        self.assertEqual(k, -4/3)
        print("result of -4 div 3:")
        print(k)

    def test_pow(self):
        k = self.solution.solve(3, 2, '^')
        self.assertEqual(k, 8)
        print("result of 2 pow 3")
        print(k)



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test_ques1'))
    suite.addTest(MyclassTest('test_ques2'))
    suite.addTest(MyclassTest('test_ques3'))
    suite.addTest(MyclassTest('test_ques4'))
    suite.addTest(MyclassTest('test_ques5'))
    suite.addTest(MyclassTest('test_ques6'))
    suite.addTest(MyclassTest('test_ChangePowOp'))
    suite.addTest(MyclassTest('test_roundup1'))
    suite.addTest(MyclassTest('test_roundup2'))
    suite.addTest(MyclassTest('test_operadd'))
    suite.addTest(MyclassTest('test_opersub'))
    suite.addTest(MyclassTest('test_opermul'))
    suite.addTest(MyclassTest('test_operdiv'))
    suite.addTest(MyclassTest('test_operpow'))
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
    suite.addTest(MyclassTest('test_pow'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

