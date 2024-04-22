import unittest

from TextNode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)
        
    def test_eq2(self):  
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node1, node2)
    
    def test_to_html1(self):
        render1 = text_node_to_html_node(TextNode("This is a text node", "bold")).to_html()
        render2 = "<b>This is a text node</b>"
        self.assertEqual(render1, render2)

    def test_to_html2(self):
        render1 = text_node_to_html_node(TextNode("This is a image", "image", "/images/img1.jpg")).to_html()
        render2 = '<img src="/images/img1.jpg" alt="This is a image"></img>'
        self.assertEqual(render1, render2)



if __name__ == "__main__":
    unittest.main()
