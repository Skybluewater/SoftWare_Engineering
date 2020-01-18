import unittest
from solve import Solvable
from OriginRequest import BiTree, QuestGenerator


class uniontest(unittest.TestCase):
    def setUp(self) -> None:
        self.question = QuestGenerator()
        self.solution = Solvable()
        self.tree = BiTree()

    def tearDown(self) -> None:
        pass

    def test_ques1(self):
        ret = self.question.generate(1, 7, 0, 0, 0, 0, 9)
        print("generate questions")

    def test_ques2(self):
        ret = self.question.generate(2, 7, 1, 1, 1, 1, 9)
        print("generate questions")

    def test_ques3(self):
        ret = self.question.generate(999, 7, 0, 0, 0, 0, 9)
        print("generate questions")

    def test_ques4(self):
        ret = self.question.generate(1000, 7, 0, 0, 0, 0, 9)
        print("generate questions")

    def test_ques5(self):
        ret = self.question.generate(1001, 7, 1, 1, 1, 1, 9)
        print("generate questions")

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
    suite.addTest(uniontest('test_ques1'))
    suite.addTest(uniontest('test_ques2'))
    suite.addTest(uniontest('test_ques3'))
    suite.addTest(uniontest('test_ques4'))
    suite.addTest(uniontest('test_ques5'))
    suite.addTest(uniontest('test_calculator1'))
    suite.addTest(uniontest('test_calculator2'))
    suite.addTest(uniontest('test_calculator3'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
