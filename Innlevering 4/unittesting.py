from BinaryTree import BinaryTree
from collections import namedtuple
import unittest

person = namedtuple('Person', ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])


class UnitTesting(unittest.TestCase):
    if __name__ == "__main__":
        unittest.main()

    def setUp(self):
        self.tree = BinaryTree()
        self.person1 = person('KRISTIANSEN', 'MORTEN KRISTIAN', 'LEINAHYTTA 36', '7224', 'MELHUS')
        self.person2 = person('OLDERVIK', 'SHARI LILL', 'KR�KA 84', '5948', 'FEDJE')
        self.person3 = person('GJERSTAD', 'TORKJELL', 'HOSTELAND 2 83', '1361', '�STER�S')
        self.person4 = person('VESTLY SKIVIK', 'JAHN FREDRIK', 'LINNG�RD 22', '1451', 'NESODDTANGEN')
        self.person5 = person('NYMANN', 'ROY-�YSTEIN', 'H�NESET 77', '7033', 'TRONDHEIM')
        self.person6 = person('�STBY', 'FRANK', 'W�RSETH 57', '7414', 'TRONDHEIM')
        self.person7 = person('LINNERUD', 'JOHNNY', 'L�RUM MELLEM 50', '6507', 'KRISTIANSUND N')
        self.person8 = person('REMLO', 'KIM ANDRE', 'SANDFLATA 71', '5648', 'HOLMEFJORD')
        self.person9 = person('SKARSHAUG', 'ASBJ�RN HARALD', 'ALAPMO 72', '7290', 'ST�REN')

    def test_find(self):
        self.tree.insert(value=self.person1)
        self.tree.insert(value=self.person2)
        self.tree.insert(value=self.person3)
        self.tree.insert(value=self.person4)
        self.assertEqual(self.tree.find(self.person1).value, self.person1)
        self.assertEqual(self.tree.find(self.person2).value, self.person2)
        self.assertEqual(self.tree.find(self.person3).value, self.person3)
        self.assertEqual(self.tree.find(self.person4).value, self.person4)

    def test_findmin(self):
        self.tree.insert(value=self.person1)
        self.tree.insert(value=self.person2)

        self.assertEqual(self.tree.findMin().value, self.person1)

    def test_findmax(self):
        self.tree.insert(value=self.person1)
        self.tree.insert(value=self.person2)

        self.assertEqual(self.tree.findMax().value, self.person2)

    def test_findLeftMost(self):
        self.tree.insert(value=self.person1)
        self.tree.insert(value=self.person2)
        self.tree.insert(value=self.person3)
        self.tree.insert(value=self.person4)
        self.tree.insert(value=self.person5)
        self.tree.insert(value=self.person6)
        self.tree.insert(value=self.person7)
        self.tree.insert(value=self.person8)
        self.tree.insert(value=self.person9)

        self.assertEqual(self.tree.findLeftMost(self.tree._root).value, self.person3)

    def test_findRightMost(self):
        self.tree.insert(value=self.person1)
        self.tree.insert(value=self.person2)
        self.tree.insert(value=self.person3)
        self.tree.insert(value=self.person4)
        self.tree.insert(value=self.person5)
        self.tree.insert(value=self.person6)
        self.tree.insert(value=self.person7)
        self.tree.insert(value=self.person8)
        self.tree.insert(value=self.person9)

        self.assertEqual(self.tree.findRightMost(self.tree._root).value, self.person6)

    def test_getnodes(self):
        #Because the insert method works as intended, we can conclude that the _getnode method is working as intended.
        #The method also returns and error if there is an attempt mate to insert a empty soace in to the tree.
        self.assertEqual(self.tree.insert(value=self.person1).value, self.person1)
        with self.assertRaises(Exception) as error:
            self.tree._getnodes()
        self.assertTrue('Attempt to insert an empty space into Binary Tree' in str(error.exception))

    def test_insert(self):
        self.assertEqual(self.tree.insert(value=self.person1).value, self.person1)
        self.assertEqual(self.tree.insert(value=self.person2).value, self.person2)
        self.assertEqual(self.tree.insert(value=self.person3).value, self.person3)

    def test_deletemin(self):
        self.tree.insert(value=self.person1)
        self.tree.insert(value=self.person2)
        self.tree.insert(value=self.person3)
        self.tree.insert(value=self.person4)
        self.tree.insert(value=self.person5)
        self.tree.insert(value=self.person6)
        self.tree.insert(value=self.person7)
        self.tree.insert(value=self.person8)
        self.tree.insert(value=self.person9)

        self.tree.deleteMin()
        self.assertEqual(self.tree.findMax().value, self.person6)

    def test_deletemax(self):
        self.tree.insert(value=self.person1)
        self.tree.insert(value=self.person2)
        self.tree.insert(value=self.person3)
        self.tree.insert(value=self.person4)
        self.tree.insert(value=self.person5)
        self.tree.insert(value=self.person6)
        self.tree.insert(value=self.person7)
        self.tree.insert(value=self.person8)
        self.tree.insert(value=self.person9)

        self.tree.deleteMax()
        self.assertEqual(self.tree.findMax().value, self.person4)

    def test_delete(self):
        self.tree.insert(value=self.person2)
        self.tree.insert(value=self.person1)
        self.tree.delete(self.person1)

        self.assertFalse(self.tree.find(self.person1))
        self.assertTrue(self.tree.find(self.person2))
