import random
from copy import deepcopy


class BiTree:
    operators = ('+', '-', '*', '/')

    def __init__(self,node_type=0,val=0):
        self.node_type=node_type
        self.val=val
        self.lchild=None
        self.rchild=None

        if self.node_type==1:
            if self.val in (0,1):
                self.this_level=0
            elif self.val in (2,3):
                self.this_level=2

    def set_children(self,lchild,rchild=None):
        self.lchild=lchild
        if rchild:
            self.rchild=rchild

    def to_string(self,upper_level=0):
        if self.node_type==1:
            if upper_level>self.this_level:
                return '(' + self.lchild.to_string(self.this_level) + self.operators[self.val] + self.rchild.to_string(self.this_level + 1) + ')'
            else:
                return self.lchild.to_string(self.this_level) + self.operators[self.val] + self.rchild.to_string(self.this_level + 1)
        return str(self.val)


class QuestGenerator:
    def __init__(self):
        self.output_list = []
        self.deduplicate_set = set()

    def generate(self, quantity=1, operators=7):
        for loop in range(quantity):
            nums = [BiTree(0, random.randint(0, 9)) for _ in range(operators + 1)]
            ops = [BiTree(1, random.randint(0, len(BiTree.operators)-2)) for _ in range(operators)]
            unfilled_ops = ops
            filled_ops = nums

            while len(unfilled_ops):
                i = random.randint(0, len(filled_ops) - 1)
                unfilled_ops[0].set_children(filled_ops[i], filled_ops[i])
                filled_ops.pop(i)
                i = random.randint(0, len(filled_ops) - 1)
                unfilled_ops[0].set_children(filled_ops[i])
                filled_ops.pop(i)

                filled_ops.append(unfilled_ops[0])
                unfilled_ops.pop(0)

            if not self.deduplicate(filled_ops[-1]):
                continue
            self.output_list.append(filled_ops[-1])
            print(self.output_list[-1].to_string())

    def deduplicate(self, root: BiTree):
        # 深拷贝 - 避免破坏原有的随机顺序
        inspect = deepcopy(root)
        QuestGenerator.format_expression(inspect)
        if inspect.to_string() in self.deduplicate_set:
            return False
        else:
            self.deduplicate_set.add(inspect.to_string())
            return True

    def format_expression(node: BiTree):
        if not node.lchild:
            return
        QuestGenerator.format_expression(node.lchild)
        QuestGenerator.format_expression(node.rchild)
        # 仅有+×可交换
        if node.val in (0, 2) and node.lchild.to_string() > node.rchild.to_string():
            tmp = node.lchild
            node.lchild = node.rchild
            node.rchild = tmp

if __name__=='__main__':
    g=QuestGenerator()
    g.generate(quantity=5,operators=5)
