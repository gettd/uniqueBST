import numpy as np


def factorial(n):
  result = 1
  for i in range(1, n):
    i = i + 1
    result = result * i
  return result


class BSTNode:

  def __init__(self, val=None):
    self.left = None
    self.right = None
    self.val = val

  def insert(self, val):
    if not self.val:
      self.val = val
      return

    if self.val == val:
      return

    if val < self.val:
      if self.left:
        self.left.insert(val)
        return
      self.left = BSTNode(val)
      return

    if self.right:
      self.right.insert(val)
      return
    self.right = BSTNode(val)

  def preorder(self, vals):
    if self.val is not None:
      vals.append(self.val)
    if self.left is not None:
      self.left.preorder(vals)
    if self.right is not None:
      self.right.preorder(vals)
    return vals


A = []
Result = []
n = int(input("Enter the number of elements in the array: "))
while len(A) < factorial(n):
  L = np.random.choice(range(1, n + 1), size=n, replace=False).tolist()
  if L not in A:
    A.append(L)
    bst = BSTNode()
    for num in L:
      bst.insert(num)
    bst.preorder([])
    if bst.preorder([]) not in Result:
      Result.append(bst.preorder([]))

print(Result)
