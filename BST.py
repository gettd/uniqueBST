class BSTNode:
  def __init__(self, key, value=None):
      self.key = key
      self.left = None
      self.right = None
      self.value = value
  def getKey(self):
    return self.key

  def getValues(self):
    return self.value

  def getRight(self):
    return self.right

  def getLeft(self):
    return self.left

def inOrder(node):
  if node is not None:
    inOrder(node.left)
    print(node.key, node.value)
    inOrder(node.right)

def preOrder(node):
  if node is not None:
    print(node.key, node.value)
    preOrder(node.left)
    preOrder(node.right)

def postOrder(node):
  if node is not None:
    print(node.key, node.value)
    postOrder(node.right)
    postOrder(node.left)

'''def insert(self, value):
  if not self.value:
      self.value = value
      return
  
  if self.value == value:
      return
  
  if value < self.value:
      if self.left:
          self.left.insert(value)
          return
      self.left = BSTNode(value)
      return
  
  if self.right:
      self.right.insert(value)
      return
  self.right = BSTNode(value)
'''
A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
L = []
for key in A:
  L.append(BSTNode(key))
L[0].left = L[1]
L[0].right = L[2]

L[1].left = L[3]
L[1].right = L[4]

L[2].left = L[5]
L[2].right = L[6]

L[3].left = L[7]
L[3].right = L[8]

L[0]= root

print(L)
        