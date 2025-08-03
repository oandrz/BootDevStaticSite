import unittest
import markdown_utils
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
        blocks = markdown_utils.markdown_to_blocks(md)
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
        blocks = markdown_utils.markdown_to_blocks(md)
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
        
        self.assertEqual(markdown_utils.block_to_block_type(block1), BlockType.HEADING)
        self.assertEqual(markdown_utils.block_to_block_type(block2), BlockType.HEADING)
        self.assertEqual(markdown_utils.block_to_block_type(block6), BlockType.HEADING)

    def test_block_to_block_type_code_and_quote(self):
        """Test that code blocks and quotes are correctly identified"""
        # Test code block
        code_block = "```\nprint('Hello, world!')\n```"
        self.assertEqual(markdown_utils.block_to_block_type(code_block), BlockType.CODE)
        
        # Test quote block
        quote_block = "> This is a quote"
        self.assertEqual(markdown_utils.block_to_block_type(quote_block), BlockType.QUOTE)

    def test_block_to_block_type_lists_and_paragraph(self):
        """Test that different list types and paragraphs are correctly identified"""
        # Test unordered lists with different markers
        unordered_dash = "- Item 1"
        unordered_asterisk = "* Item 1"
        unordered_plus = "+ Item 1"
        
        self.assertEqual(markdown_utils.block_to_block_type(unordered_dash), BlockType.unordered_list)
        self.assertEqual(markdown_utils.block_to_block_type(unordered_asterisk), BlockType.unordered_list)
        self.assertEqual(markdown_utils.block_to_block_type(unordered_plus), BlockType.unordered_list)
        
        # Test ordered list
        ordered_block = "1. First item"
        self.assertEqual(markdown_utils.block_to_block_type(ordered_block), BlockType.ordered_list)
        
        # Test paragraph (default case)
        paragraph_block = "This is just a regular paragraph of text."
        self.assertEqual(markdown_utils.block_to_block_type(paragraph_block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()