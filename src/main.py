from file_utils import copy_static_to_public
from page_generator import generate_page


def main():
    print("\nCopying static assets to public directory...")
    # Test the functions
    success = copy_static_to_public()
    if success:
        print("Successfully copied static directory to public directory")
    else:
        print("Failed to copy static directory to public directory")

    generate_page(
        from_path="./content/index.md",
        template_path="./template.html",
        dest_path="./public/index.html"
    )


if __name__ == "__main__":
    main()