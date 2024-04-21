from LeafNode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, target):
        return (
            self.text == target.text and
            self.text_type == target.text_type and
            self.url == target.url
        )
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


## Functions    
def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == "image":
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise TypeError(f"Wrong text_type: {text_node.text_type}")

# split_nodes_delimiter(old_nodes, delimiter, text_type)
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for old_node in old_nodes:
        if type(old_node) != TextNode:
            nodes.append (old_node)
        elif old_node.text_type != "text":
            nodes.append (old_node)
        else:
            text_parts = old_node.text.split(delimiter)
            if len(text_parts) % 2 == 0:
                raise Exception(f"Found odd number of delimiters '{delimiter}'")
            for i in range(0, len(text_parts)):
                if i % 2 == 0:
                    nodes.append(TextNode(text_parts[i], "text"))
                else:
                    nodes.append(TextNode(text_parts[i], text_type))
    return nodes

# extract_markdown_images(text)
# Takes raw text and returns a list of tuples. Each tuple should contain the alt text and the URL of any markdown images.
#   ext = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
#   [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
import re
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
# extract_markdown_links(text)
# Takes raw text and returns a list of tuples. It should return tuples of anchor text and URLs
#   text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
#   [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    nodes = []
    for old_node in old_nodes:
        if type(old_node) != TextNode:
            nodes.append (old_node)
        elif old_node.text_type != "text":
            nodes.append (old_node)
        else:
            images = extract_markdown_images(old_node.text)
            if len(images) == 0 and len (old_node.text) > 0:
                nodes.append (old_node)
            else:
                text = old_node.text
                for i in range(0, len(images)):
                    pattern = f"![{images[i][0]}]({images[i][1]})"
                    #print (f"Split pattern: {pattern}")
                    parts = text.split(pattern)
                    if len(parts)>0 and len(parts[0])>0 :
                        nodes.append(TextNode(parts[0],"text"))
                    if len(parts)>1:
                        text = parts[1]
                    else:
                        text = ""
                    nodes.append(TextNode(images[i][0],"image",images[i][1]))
                if len(text)>0:
                    nodes.append(TextNode(text,"text"))                    
    return nodes

def split_nodes_link(old_nodes):
    nodes = []
    for old_node in old_nodes:
        if type(old_node) != TextNode:
            nodes.append (old_node)
        elif old_node.text_type != "text":
            nodes.append (old_node)
        else:
            links = extract_markdown_links(old_node.text)
            if len(links) == 0 and len (old_node.text) > 0:
                nodes.append (old_node)
            else:
                text = old_node.text
                for i in range(0, len(links)):
                    pattern = f"[{links[i][0]}]({links[i][1]})"
                    #print (f"Split pattern: {pattern}")
                    parts = text.split(pattern)
                    if len(parts)>0 and len(parts[0])>0 :
                        nodes.append(TextNode(parts[0],"text"))
                    if len(parts)>1:
                        text = parts[1]
                    else:
                        text = ""
                    nodes.append(TextNode(links[i][0],"link",links[i][1]))
                if len(text)>0:
                    nodes.append(TextNode(text,"text"))                    
    return nodes
