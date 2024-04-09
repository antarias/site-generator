from HTMLNode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        if tag == None or tag == "":
            raise ValueError("Missing tag")
        if children == None:
            raise ValueError("Missing children")
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        html = ""       
        if self.tag != None:
            html += f"<{self.tag}{super().props_to_html()}>"
        for child in self.children:
            html += child.to_html()
        if self.tag != None:         
            html += f"</{self.tag}>"
        return html
    
