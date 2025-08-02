from textnode import TextNode, TextType

def main():
    # Create a new TextNode object with dummy values
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(repr(text_node))

if __name__ == "__main__":
    main()