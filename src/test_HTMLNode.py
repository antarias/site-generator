import unittest

from HTMLNode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props1(self):
        props1 = HTMLNode(None,None,None,{"href": "https://www.google.com", "target": "_blank"}).props_to_html()
        props2 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(props1, props2)

    def test_props2(self):
        props1 = HTMLNode(None,None,None,None).props_to_html()
        props2 = ""
        self.assertEqual(props1, props2)
        
if __name__ == "__main__":
    unittest.main()
