from src.textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Delimiter split resulted in an even number of sections, which is invalid for inline formatting.")
        for i, section in enumerate(sections):
            if section == "":
                continue
            if i % 2 == 0:
                # Even index: regular text
                split_nodes.append(TextNode(section, TextType.TEXT, node.url))
            else:
                # Odd index: formatted text
                split_nodes.append(TextNode(section, text_type, node.url))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches