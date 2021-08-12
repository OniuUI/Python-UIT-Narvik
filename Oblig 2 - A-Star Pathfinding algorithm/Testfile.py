class treenode():

    def __init__(self, inputData):
        self.left = inputData
        self.right = None
        self.value = None


class binarytree():
    root = treenode(1)
    root.left = treenode(2)
    root.right = treenode(3)
    root.left.left = treenode(4)
    root.left.right = treenode(5)

    def find(value):
        current = value
        stack = []
        done = 0

        while True:
            if current is not None:
                stack.append(current)
                current = current.left

            elif stack:
                current = stack.pop()
                print(current.left, end=" ")
                current = current.right

            else:
                break

        print()


binarytree.find(treenode(1))
