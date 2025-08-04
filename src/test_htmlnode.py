import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html_empty_props(self):
        """Test props_to_html returns empty string when props is empty"""
        node = HTMLNode("p", "Hello world")
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_none_props(self):
        """Test props_to_html returns empty string when props is None"""
        node = HTMLNode("div", "Content", None, None)
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_single_prop(self):
        """Test props_to_html with a single property"""
        node = HTMLNode("a", "Click me", None, {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
    
    def test_props_to_html_multiple_props(self):
        """Test props_to_html with multiple properties"""
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("a", "Click me", None, props)
        result = node.props_to_html()
        
        # Since dict order might vary, check that both attributes are present
        self.assertIn('href="https://www.google.com"', result)
        self.assertIn('target="_blank"', result)
        self.assertTrue(result.startswith(" "))
    
    def test_props_to_html_complex_attributes(self):
        """Test props_to_html with complex HTML attributes"""
        props = {
            "class": "btn btn-primary",
            "id": "submit-button",
            "data-toggle": "modal",
            "aria-label": "Submit form"
        }
        node = HTMLNode("button", "Submit", None, props)
        result = node.props_to_html()
        
        # Verify all attributes are present
        self.assertIn('class="btn btn-primary"', result)
        self.assertIn('id="submit-button"', result)
        self.assertIn('data-toggle="modal"', result)
        self.assertIn('aria-label="Submit form"', result)
        self.assertTrue(result.startswith(" "))
    
    def test_props_to_html_special_characters(self):
        """Test props_to_html handles special characters in attribute values"""
        props = {"title": "This is a 'quoted' string with & symbols"}
        node = HTMLNode("img", None, None, props)
        result = node.props_to_html()
        self.assertEqual(result, ' title="This is a \'quoted\' string with & symbols"')
    
    def test_htmlnode_initialization_defaults(self):
        """Test HTMLNode initializes with proper defaults"""
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.value)
        self.assertIsNone(node.value)
    
    def test_htmlnode_initialization_with_values(self):
        """Test HTMLNode initializes correctly with provided values"""
        children = [HTMLNode("span", "child")]
        props = {"class": "container"}
        node = HTMLNode("div", "Some text", children, props)
        
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Some text")
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, props)
    
    def test_htmlnode_to_html_not_implemented(self):
        """Test that to_html method raises NotImplementedError"""
        node = HTMLNode("p", "text")
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_htmlnode_repr(self):
        """Test HTMLNode string representation"""
        node = HTMLNode("a", "link", [], {"href": "http://example.com"})
        expected = "HTMLNode(tag=a, value=link, children=[], props={'href': 'http://example.com'})"
        self.assertEqual(repr(node), expected)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()