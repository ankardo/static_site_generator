from nodes.textnode import (
    TextNode,
)
from utils.inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images
)


def main():
    new_text_node = TextNode(
        "This is a text node and this should be **bold**", "text", "www.google.com")
    split_nodes_delimiter([new_text_node], "**", "bold")
    result = extract_markdown_links(
        "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    )
    print(result)
    result2 = extract_markdown_images(
        "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    )
    print(result2)


if __name__ == "__main__":
    main()
