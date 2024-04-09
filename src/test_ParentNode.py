import unittest

from ParentNode import ParentNode
from LeafNode import LeafNode

class TestLeafNode(unittest.TestCase):
        
    def test_tohtml1(self):
        render1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        ).to_html()                 
        render2 = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(render1, render2)

    def test_tohtml2(self):
        render1 = ParentNode(
            "p",
            [
                LeafNode("a","Esto es el texto",{"href": "https://www.google.com", "target": "_blank"}),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        ).to_html()
        render2 = '<p><a href="https://www.google.com" target="_blank">Esto es el texto</a>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(render1, render2)

    def test_tohtml3(self):
        render1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ], 
            {"href": "https://www.google.com", "target": "_blank"}
        ).to_html()                 
        render2 = '<p href="https://www.google.com" target="_blank"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(render1, render2)
        
        
if __name__ == "__main__":
    unittest.main()
