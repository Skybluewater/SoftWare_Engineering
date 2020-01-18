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

    def test_ques7(self):
        ret = self.question.generate(100,1,0,0,15)
        print("generate questions")
        print(ret)

    def test_calculator1(self):
        k = self.solution.calculator("(6-3)/4")
        self.assertEqual(k, 0.75)

    def test_calculator2(self):
        k = self.solution.calculator("7")
        self.assertEqual(k, 7)

    def test_calculator3(self):
        k = self.solution.calculator("3-8")
        self.assertEqual(k, -5)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test_ques1'))
    suite.addTest(MyclassTest('test_ques2'))
    suite.addTest(MyclassTest('test_ques3'))
    suite.addTest(MyclassTest('test_ques4'))
    suite.addTest(MyclassTest('test_ques5'))
    suite.addTest(MyclassTest('test_ques6'))
    suite.addTest(MyclassTest('test_ques7'))
    suite.addTest(MyclassTest('test_calculator1'))
    suite.addTest(MyclassTest('test_calculator2'))
    suite.addTest(MyclassTest('test_calculator3'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
