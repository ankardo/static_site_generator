import unittest

from textnode import (
    TextNode,
    split_node_delimiter,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("Another text node", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_text_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_url(self):
        node = TextNode("This is a text node", "bold", "https://www.ex.com")
        node2 = TextNode("This is a text node", "bold", "https://www.aex.com")
        self.assertNotEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_text, "https://www.ex.com")
        node2 = TextNode("This is a text node", text_type_text, "https://www.ex.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is text node", "bold", "https://www.ex.com")
        expected_repr = "TextNode(This is text node, bold, https://www.ex.com)"
        self.assertEqual(repr(node), expected_repr)

    def test_split_nodes_bold_delimiter(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        result = split_node_delimiter([node], "**", text_type_bold)

        expected = [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
        ]

        self.assertEqual(result, expected)

    def test_split_nodes_italic_delimiter(self):
        node = TextNode("This is text with a *italic* word", text_type_text)
        result = split_node_delimiter([node], "*", text_type_italic)

        expected = [
                TextNode("This is text with a ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
        ]

        self.assertEqual(result, expected)

    def test_split_nodes_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        result = split_node_delimiter([node], "`", text_type_italic)

        expected = [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
        ]

        self.assertEqual(result, expected)

    def test_split_nodes_no_delimiter(self):
        node = TextNode("This is plain text", text_type_text)

        result = split_node_delimiter([node], "**", text_type_bold)

        expected = [TextNode("This is plain text", text_type_text)]

        self.assertEqual(result, expected)

    def test_split_nodes_no_closing_delimiter(self):
        node = TextNode("** This should be plain text", text_type_text)

        result = split_node_delimiter([node], "**", text_type_bold)

        expected = [TextNode("** This should be plain text", text_type_text)]

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
