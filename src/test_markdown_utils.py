import unittest
from markdown_utils import markdown_to_blocks, markdown_to_html_node, block_to_block_type, extract_title
from block_type import BlockType



class TestMarkdownUtils(unittest.TestCase):
    """Test suite for MarkdownUtils functions"""

    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
    This is **bolded** paragraph




    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        """Test that headings are correctly identified"""
        # Test different heading levels
        block1 = "# This is a heading 1"
        block2 = "## This is a heading 2"
        block6 = "###### This is a heading 6"
        
        self.assertEqual(block_to_block_type(block1), BlockType.HEADING)
        self.assertEqual(block_to_block_type(block2), BlockType.HEADING)
        self.assertEqual(block_to_block_type(block6), BlockType.HEADING)

    def test_block_to_block_type_code_and_quote(self):
        """Test that code blocks and quotes are correctly identified"""
        # Test code block
        code_block = "```\nprint('Hello, world!')\n```"
        self.assertEqual(block_to_block_type(code_block), BlockType.CODE)
        
        # Test quote block
        quote_block = "> This is a quote"
        self.assertEqual(block_to_block_type(quote_block), BlockType.QUOTE)

    def test_block_to_block_type_lists_and_paragraph(self):
        """Test that different list types and paragraphs are correctly identified"""
        # Test unordered lists with different markers
        unordered_dash = "- Item 1"
        unordered_asterisk = "* Item 1"
        unordered_plus = "+ Item 1"
        
        self.assertEqual(block_to_block_type(unordered_dash), BlockType.unordered_list)
        self.assertEqual(block_to_block_type(unordered_asterisk), BlockType.unordered_list)
        self.assertEqual(block_to_block_type(unordered_plus), BlockType.unordered_list)
        
        # Test ordered list
        ordered_block = "1. First item"
        self.assertEqual(block_to_block_type(ordered_block), BlockType.ordered_list)
        
        # Test paragraph (default case)
        paragraph_block = "This is just a regular paragraph of text."
        self.assertEqual(block_to_block_type(paragraph_block), BlockType.PARAGRAPH)

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_extract_title_valid_h1(self):
        """Test extracting title from markdown with valid H1 heading"""
        markdown = "# My Title\n\nSome content here."
        result = extract_title(markdown)
        self.assertEqual(result, "My Title")

    def test_extract_title_with_leading_whitespace(self):
        """Test extracting title with leading whitespace in heading"""
        markdown = "#    Title with Spaces   \n\nContent follows."
        result = extract_title(markdown)
        self.assertEqual(result, "Title with Spaces")

    def test_extract_title_multiline_first_block(self):
        """Test extracting title when first block has multiple lines"""
        markdown = "# Main Title\nSubtitle line\n\nParagraph content."
        result = extract_title(markdown)
        self.assertEqual(result, "Main Title")

    def test_extract_title_no_heading(self):
        """Test when first block is not a heading"""
        markdown = "This is just a paragraph.\n\n# Later heading"
        result = extract_title(markdown)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()