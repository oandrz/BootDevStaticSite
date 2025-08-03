import unittest
from textnode import TextNode, TextType
from inline_utils import text_to_textnodes

class TestTextNode(unittest.TestCase):
    
    def test_eq_same_properties(self):
        """Test that two TextNode objects with identical properties are equal"""
        node1 = TextNode("Hello world", TextType.TEXT, "https://example.com")
        node2 = TextNode("Hello world", TextType.TEXT, "https://example.com")
        self.assertEqual(node1, node2)
    
    def test_eq_no_url(self):
        """Test that two TextNode objects with None URL are equal"""
        node1 = TextNode("Plain text", TextType.TEXT)
        node2 = TextNode("Plain text", TextType.TEXT)
        self.assertEqual(node1, node2)
    
    def test_eq_none_url_explicit(self):
        """Test that TextNode objects with explicitly None URL are equal"""
        node1 = TextNode("Bold text", TextType.BOLD, None)
        node2 = TextNode("Bold text", TextType.BOLD, None)
        self.assertEqual(node1, node2)
    
    def test_not_eq_different_text(self):
        """Test that TextNode objects with different text are not equal"""
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("World", TextType.TEXT)
        self.assertNotEqual(node1, node2)
    
    def test_not_eq_different_text_type(self):
        """Test that TextNode objects with different text_type are not equal"""
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Hello", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    
    def test_not_eq_different_url(self):
        """Test that TextNode objects with different URLs are not equal"""
        node1 = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://different.com")
        self.assertNotEqual(node1, node2)
    
    def test_not_eq_url_vs_none(self):
        """Test that TextNode with URL is not equal to TextNode with None URL"""
        node1 = TextNode("Image", TextType.IMAGE, "https://example.com/image.jpg")
        node2 = TextNode("Image", TextType.IMAGE, None)
        self.assertNotEqual(node1, node2)
    
    def test_not_eq_none_vs_url(self):
        """Test that TextNode with None URL is not equal to TextNode with URL"""
        node1 = TextNode("Code", TextType.CODE, None)
        node2 = TextNode("Code", TextType.CODE, "https://github.com")
        self.assertNotEqual(node1, node2)
    
    def test_not_eq_different_types_same_text(self):
        """Test various text types with same text are not equal"""
        base_text = "Sample text"
        text_node = TextNode(base_text, TextType.TEXT)
        bold_node = TextNode(base_text, TextType.BOLD)
        italic_node = TextNode(base_text, TextType.ITALIC)
        code_node = TextNode(base_text, TextType.CODE)
        
        self.assertNotEqual(text_node, bold_node)
        self.assertNotEqual(text_node, italic_node)
        self.assertNotEqual(text_node, code_node)
        self.assertNotEqual(bold_node, italic_node)
        self.assertNotEqual(bold_node, code_node)
        self.assertNotEqual(italic_node, code_node)
    
    def test_not_eq_with_non_textnode(self):
        """Test that TextNode is not equal to other object types"""
        node = TextNode("Hello", TextType.TEXT)
        self.assertNotEqual(node, "Hello")
        self.assertNotEqual(node, None)
        self.assertNotEqual(node, 42)
        self.assertNotEqual(node, {"text": "Hello", "text_type": TextType.TEXT})

    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )

if __name__ == "__main__":
    unittest.main()