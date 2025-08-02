from enum import Enum

class TextType(Enum):
    TEXT = "text"
    IMAGE = "image"
    BOLD = "bold_text"
    ITALIC = "italic_text"
    CODE = "code_text"
    LINK = "link_text"
    IMAGE_LINK = "image_link"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: object) -> bool:
        return isinstance(value, TextNode) and self.text == value.text and self.text_type == value.text_type and self.url == value.url
    
    def __hash__(self) -> int:
        return hash((self.text, self.text_type, self.url))
    
    def __str__(self) -> str:
        return f"{self.text_type.value}: {self.text}"
    
    def __repr__(self) -> str:
        return f"TextNode({self.text_type.value}, {self.text}, {self.url})"
