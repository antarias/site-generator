import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_tohtml1(self):
        render1 = LeafNode("a","Esto es el texto",{"href": "https://www.google.com", "target": "_blank"}).to_html()
        render2 = '<a href="https://www.google.com" target="_blank">Esto es el texto</a>'
        self.assertEqual(render1, render2)

    def test_tohtml2(self):
        render1 = LeafNode(None,"Esto es el texto",{"href": "https://www.google.com", "target": "_blank"}).to_html()
        render2 = 'Esto es el texto'
        self.assertEqual(render1, render2)

        
if __name__ == "__main__":
    unittest.main()
