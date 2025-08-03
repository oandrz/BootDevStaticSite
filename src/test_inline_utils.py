import unittest
from inline_utils import extract_markdown_images, extract_markdown_links


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_single_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) inside."
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_multiple_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_no_images(self):
        text = "This is text with no images."
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_image_with_empty_alt(self):
        text = "Here is an image: ![](https://example.com/img.png)"
        expected = [("", "https://example.com/img.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_image_with_special_characters(self):
        text = "![alt!@#](https://example.com/img.png)"
        expected = [("alt!@#", "https://example.com/img.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_images_multiple_prompt(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(extract_markdown_images(text), expected)

if __name__ == "__main__":
    unittest.main()

