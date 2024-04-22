import re
from TextNode import *

# split_nodes_delimiter(old_nodes, delimiter, text_type)
#  It takes a list of "old nodes", a delimiter, and a text type. 
#  It should return a new list of nodes, where any "text" type nodes in the input list are 
#  (potentially) split into multiple nodes based on the syntax.
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
#  Takes raw text and returns a list of tuples. Each tuple should contain the alt text and the URL of any markdown images.
#  Used only by split_nodes_image(old_nodes)
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)    

# split_nodes_image(old_nodes)
#
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

# extract_markdown_links(text)
#  Takes raw text and returns a list of tuples. It should return tuples of anchor text and URLs
#  Used only by split_nodes_link(old_nodes)
def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

# split_nodes_link(old_nodes)
# 
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

# text_to_textnodes(text) 
# Function that convert a raw string of markdown flavored text into a list of TextNode objects,
#  using above functions
def text_to_textnodes(text):
    nodes = []
    # First, convert the text to a TextNode (of 'text' type)
    nodes.append(TextNode(text, text_type_text))
    # Now, we split using all possible delimiters.
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*",  text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    # Split links and images
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
