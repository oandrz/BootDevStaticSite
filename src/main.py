from file_utils import copy_static_to_public
from page_generator import generate_pages_recursive
import sys


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(f"Base path set to: {basepath}")

    print("\nCopying static assets to public directory...")
    # Test the functions
    success = copy_static_to_public()
    if success:
        print("Successfully copied static directory to public directory")
    else:
        print("Failed to copy static directory to public directory")

    generate_pages_recursive(
        dir_path_content="../content",
        template_path="../template.html",
        dest_path_dir="../docs",
        basepath = basepath
    )


if __name__ == "__main__":
    main()