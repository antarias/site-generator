from HTMLNode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value=None, props = None):
        if (value == None):
            raise ValueError()
        super().__init__(tag, value, None ,props)        

    def to_html(self):       
        if self.tag == None:
            return self.value
        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
    