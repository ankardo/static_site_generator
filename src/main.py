from nodes.textnode import (
        TextNode,
)
from utils.inline_markdown import (
    split_nodes_delimiter,
)


def main():
    new_text_node = TextNode("This is a text node and this should be **bold**", "text", "www.google.com")
    split_nodes_delimiter([new_text_node], "**", "bold")
    print(new_text_node)


if __name__ == "__main__":
    main()
