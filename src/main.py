from file_utils import copy_static_to_public
from page_generator import generate_pages_recursive


def main():
    print("\nCopying static assets to public directory...")
    # Test the functions
    success = copy_static_to_public()
    if success:
        print("Successfully copied static directory to public directory")
    else:
        print("Failed to copy static directory to public directory")

    generate_pages_recursive(
        dir_path_content="./content",
        template_path="./template.html",
        dest_path_dir="./public"
    )


if __name__ == "__main__":
    main()