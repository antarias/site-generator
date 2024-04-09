from LeafNode import LeafNode

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



