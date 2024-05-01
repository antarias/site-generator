import unittest

from TextNode import *
from functions_inline import *

class Test_functions_inline(unittest.TestCase):

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

    #text_to_textnodes
    def test_text_to_textnodes1(self):
        text = "This is **bold text** with an *italic word* and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev) and a last part."
        nodes1 = text_to_textnodes(text)
        nodes2 = [
            TextNode("This is ", text_type_text),
            TextNode("bold text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic word", text_type_italic),
            TextNode(" and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
            TextNode(" and a last part.", text_type_text),                        
        ]
        # print ("")        
        # print ("test_text_to_textnodes")
        # print ("======================")
        # print (nodes1)
        # print ("")  
        # print (nodes2)
        self.assertEqual(nodes1, nodes2)

    def test_text_to_textnodes2(self):
        text = '![LOTR image artistmonkeys](/images/rivendell.png)'
        nodes1 = text_to_textnodes(text)
        nodes2 = [
            TextNode("LOTR image artistmonkeys", text_type_image, "/images/rivendell.png"),
        ]
        # print ("")        
        # print ("test_text_to_textnodes")
        # print ("======================")
        # print (nodes1)
        # print ("")  
        # print (nodes2)
        self.assertEqual(nodes1, nodes2)


if __name__ == "__main__":
    unittest.main()
    