class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        """Convert the props dictionary to HTML attribute string"""
        if not self.props:
            return ""
        
        html_attrs = []
        for key, value in self.props.items():
            html_attrs.append(f'{key}="{value}"')
        
        return " " + " ".join(html_attrs)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"