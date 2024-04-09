class HTMLNode:
    
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError()
            
    def props_to_html(self):
        if self.props == None:
            return ""
        html = ''
        for prop in self.props:
            html += f' {prop}="{self.props[prop]}"'
        return html
                                    
    def __repr__(self):
        return f"TextHTML({self.tag}, {self.value}, {self.children}, {self.props})"
    