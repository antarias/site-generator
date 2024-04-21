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

    # extract_markdown_images
    def test_extract_markdown_images1(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        nodes1 = extract_markdown_images(text)
        nodes2 = [
            ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), 
            ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")
        ]
        self.assertEqual(nodes1, nodes2)

    # extract_markdown_links
    def test_extract_markdown_links1(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        nodes1 = extract_markdown_links(text)
        nodes2 = [("link", "https://www.example.com"), 
                  ("another", "https://www.example.com/another")
        ]
        self.assertEqual(nodes1, nodes2)

    #test_split_nodes_image
    def test_split_nodes_image1(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        nodes1 = split_nodes_image([node])
        nodes2 = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
        ]
        #print ("")        
        #print ("test_split_nodes_image")
        #print ("======================")
        #print (nodes1)
        #print ("")  
        #print (nodes2)
        self.assertEqual(nodes1, nodes2)

    def test_split_nodes_image2(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) and more",
            text_type_text,
        )
        nodes1 = split_nodes_image([node])
        nodes2 = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
            TextNode(" and more", text_type_text),
        ]
        self.assertEqual(nodes1, nodes2)

    def test_split_nodes_image3(self):
        node = TextNode(
            "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        nodes1 = split_nodes_image([node])
        nodes2 = [
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
        ]
        # print ("")        
        # print ("test_split_nodes_image")
        # print ("======================")
        # print (nodes1)
        # print ("")  
        # print (nodes2)
        self.assertEqual(nodes1, nodes2)

    def test_split_nodes_image4(self):
        node = TextNode(
            "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
            text_type_text,
        )
        nodes1 = split_nodes_image([node])
        nodes2 = [
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        ]
        # print ("")  
        # print ("")        
        # print ("test_split_nodes_image")
        # print ("======================")
        # print (nodes1)
        # print (nodes2)
        self.assertEqual(nodes1, nodes2)

    def test_split_nodes_image5(self):
        node = TextNode(
            "",
            text_type_text,
        )
        nodes1 = split_nodes_image([node])
        nodes2 = [
        ]
        # print ("")  
        # print ("")        
        # print ("test_split_nodes_image")
        # print ("======================")
        # print (nodes1)
        # print (nodes2)
        self.assertEqual(nodes1, nodes2)

    def test_split_nodes_image6(self):
        node = TextNode(
            "Just text",
            text_type_text,
        )
        nodes1 = split_nodes_image([node])
        nodes2 = [
            TextNode("Just text", text_type_text),
        ]
        # print ("")  
        # print ("")        
        # print ("test_split_nodes_image")
        # print ("======================")
        # print (nodes1)
        # print (nodes2)
        self.assertEqual(nodes1, nodes2)


    #test_split_nodes_link
    def test_split_nodes_link1(self):
        node = TextNode(
            "This is text with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        nodes1 = split_nodes_link([node])
        nodes2 = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
        ]
        # print ("")        
        # print ("test_split_nodes_image")
        # print ("======================")
        # print (nodes1)
        # print ("")  
        # print (nodes2)
        self.assertEqual(nodes1, nodes2)


if __name__ == "__main__":
    unittest.main()
