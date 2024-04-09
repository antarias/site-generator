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

    def test_split_nodes_delimiter1(self):
        nodes1 = split_nodes_delimiter([ TextNode("Text with *italic fragment* of text", "text") ], "*", "italic")
        nodes2 = [ 
            TextNode("Text with ", "text"), 
            TextNode("italic fragment", "italic"), 
            TextNode(" of text", "text") 
        ]
        self.assertEqual(nodes1, nodes2)

    def test_split_nodes_delimiter2(self):
        nodes1 = split_nodes_delimiter([ TextNode("*Only italic fragment*", "text") ], "*", "italic")
        nodes2 = [ 
            TextNode("", "text"), 
            TextNode("Only italic fragment", "italic"), 
            TextNode("", "text") 
        ]
        self.assertEqual(nodes1, nodes2)

    def test_split_nodes_delimiter3(self):
        self.assertRaises(Exception, split_nodes_delimiter, ([ TextNode("*Not correct italic fragment", "text") ], "*", "italic"))

    def test_split_nodes_delimiter4(self):
        nodes1 = split_nodes_delimiter([ TextNode("Text with `code fragment` of text", "text") ], "`", "code")
        nodes2 = [ 
            TextNode("Text with ", "text"), 
            TextNode("code fragment", "code"), 
            TextNode(" of text", "text") 
        ]
        self.assertEqual(nodes1, nodes2)

    def test_split_nodes_delimiter5(self):
        nodes1 = split_nodes_delimiter([ TextNode("Text with **bold fragment** of text", "text") ], "**", "bold")
        nodes2 = [ 
            TextNode("Text with ", "text"), 
            TextNode("bold fragment", "bold"), 
            TextNode(" of text", "text") 
        ]
        self.assertEqual(nodes1, nodes2)

if __name__ == "__main__":
    unittest.main()
