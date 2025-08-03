# Guide: Extracting Markdown Image Links in Python

## Problem
Given a string containing Markdown image syntax (e.g., `![alt text](url)`), extract all image alt texts and URLs as a list of tuples.

Example:
```python
text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# Desired output:
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
```

## Approach
1. **Use Regular Expressions**: Markdown images follow the pattern `![alt text](url)`. We can use Python's `re` module to find all such patterns.
2. **Regex Pattern**: The pattern for a Markdown image is:
   - Starts with `!` and `[` (literal characters)
   - Followed by any characters except `]` (the alt text)
   - Followed by `](` (literal characters)
   - Followed by any characters except `)` (the URL)
   - Ends with `)`
   
   Regex: `!\[([^\]]*)\]\(([^\)]+)\)`
   - `([^\]]*)` captures the alt text
   - `([^\)]+)` captures the URL

3. **Implementation**:
   - Import `re`
   - Use `re.findall` with the pattern
   - Return the list of tuples

## Example Implementation
```python
import re

def extract_markdown_images(text):
    pattern = r'!\[([^\]]*)\]\(([^\)]+)\)'
    return re.findall(pattern, text)

# Example usage:
text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))
# Output: [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
```

## Notes
- This approach assumes that the alt text and URL do not contain `]` or `)` respectively. For most Markdown, this is sufficient.
- If you need to handle nested or more complex Markdown, consider using a Markdown parser library.

