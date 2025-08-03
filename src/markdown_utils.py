import re

from block_type import BlockType


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(re.sub(r'\n +', '\n', block))
    return filtered_blocks

def starts_with_headings(s):
    return bool(re.match(r'^#{1,6} (.+)', s))

def block_to_block_type(block):
    if starts_with_headings(block):
        return BlockType.HEADING
    elif block.startswith("```") or block.endswith("~~~"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("- ") or block.startswith("* ") or block.startswith("+ "):
        return BlockType.unordered_list
    elif block[0].isdigit() and block[1] == ".":
        return BlockType.ordered_list
    else:
        return BlockType.PARAGRAPH
