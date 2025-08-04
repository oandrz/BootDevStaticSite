from pathlib import Path

from markdown_utils import markdown_to_html_node, extract_title
from file_utils import write_html_to_file

def generate_pages_recursive(dir_path_content, template_path, dest_path_dir):
    dir_path_content = Path(dir_path_content)
    dest_path_dir = Path(dest_path_dir)

    if not dir_path_content.is_dir():
        print(f"Error: {dir_path_content} is not a valid directory.")
        return

    if not dest_path_dir.exists():
        dest_path_dir.mkdir(parents=True, exist_ok=True)

    for item in dir_path_content.iterdir():
        if item.is_file() and item.suffix == '.md':
            dest_file = dest_path_dir / (item.stem + '.html')
            generate_page(item, template_path, dest_file)
        elif item.is_dir():
            new_dest_dir = dest_path_dir / item.name
            generate_pages_recursive(item, template_path, new_dest_dir)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_content = read_file(from_path)
    template_content = read_file(template_path)
    if markdown_content is None or template_content is None:
        print("Error reading files, cannot generate page.")
        return
    html_markdown_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    template_content = template_content.replace(
        "{{ Content }}",
        html_markdown_content
    ).replace("{{ Title }}", title if title else "Untitled Page")

    write_html_to_file(template_content, dest_path, log_operations=True)

def read_file(path):
  """Read markdown file and return content or None if error."""
  try:
      with open(path, 'r', encoding='utf-8') as file:
          return file.read()
  except (FileNotFoundError, IOError) as e:
      print(f"Error reading {path}: {e}")
      return None