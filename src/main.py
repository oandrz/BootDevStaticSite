from textnode import TextNode, TextType
from file_utils import copy_static_to_public


def main():
    # Create a new TextNode object with dummy values
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(repr(text_node))
    
    # Copy static assets to public directory
    print("\nCopying static assets to public directory...")
    success = copy_static_to_public()
    if success:
        print("✓ Successfully copied static assets to public directory")
    else:
        print("✗ Failed to copy static assets to public directory")


if __name__ == "__main__":
    main()