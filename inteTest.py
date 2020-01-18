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

    def test_ques6(self):
        ret = self.question.generate(10, 5, 0, 0, 0, 9)
        print("generate questions")
        print(ret)

    def test_ques7(self):
        ret = self.question.generate(100, 1, 0, 0, 15)
        print("generate questions")

    def test_ques8(self):
        ret = self.question.generate(10, 5, 1, 0, 0, 9)
        print("generate questions")
        print(ret)

    def test_ques9(self):
        ret = self.question.generate(10, 5, 0, 1, 0, 9)
        print("generate questions")
        print(ret)

    def test_ques10(self):
        ret = self.question.generate(10, 5, 0, 0, 1, 9)
        print("generate questions")
        print(ret)

    def test_ques11(self):
        ret = self.question.generate(5, 8, 0, 0, 0, 15)
        print("generate questions")
        print(ret)

    def test_ques12(self):
        ret = self.question.generate(1000, 5, 1, 1, 1, 9)
        print("generate questions")
        print(ret)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(uniontest('test_ques1'))
    suite.addTest(uniontest('test_ques2'))
    suite.addTest(uniontest('test_ques3'))
    suite.addTest(uniontest('test_ques4'))
    suite.addTest(uniontest('test_ques5'))
    suite.addTest(uniontest('test_ques6'))
    suite.addTest(uniontest('test_ques7'))
    suite.addTest(uniontest('test_ques8'))
    suite.addTest(uniontest('test_ques9'))
    suite.addTest(uniontest('test_ques10'))
    suite.addTest(uniontest('test_ques11'))
    suite.addTest(uniontest('test_ques12'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
