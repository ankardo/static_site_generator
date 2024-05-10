import unittest
from utils.inline_markdown import split_nodes_delimiter
from nodes.textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


def get_node_type(delimiter):
    if delimiter == "**":
        return text_type_bold
    elif delimiter == "*":
        return text_type_italic
    elif delimiter == "`":
        return text_type_code
    else:
        return text_type_text


class TestSplitNodes(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            # Test case for bold delimiter
            {
                "input_node": TextNode("This is text with a **bolded** word",
                                       text_type_text),
                "delimiter": "**",
                "expected": [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("bolded", text_type_bold),
                    TextNode(" word", text_type_text),
                ]
            },
            # Test case for italic delimiter
            {
                "input_node": TextNode("This is text with a *italic* word",
                                       text_type_text),
                "delimiter": "*",
                "expected": [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("italic", text_type_italic),
                    TextNode(" word", text_type_text),
                ]
            },
            # Test case for code delimiter
            {
                "input_node": TextNode("This is text with a `code block` word",
                                       text_type_text),
                "delimiter": "`",
                "expected": [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("code block", text_type_code),
                    TextNode(" word", text_type_text),
                ]
            },
            # Test case for no delimiter
            {
                "input_node": TextNode("This is plain text", text_type_text),
                "delimiter": "**",
                "expected": [TextNode("This is plain text", text_type_text)]
            },
            # Test case for no closing delimiter
            {
                "input_node": TextNode("** This should be plain text",
                                       text_type_text),
                "delimiter": "**",
                "expected_exception": ValueError
            }
        ]

    def test_split_nodes(self):
        for case in self.test_cases:
            if "expected_exception" in case:
                with self.assertRaises(case["expected_exception"]):
                    split_nodes_delimiter(
                        [case["input_node"]], case["delimiter"],
                        text_type_bold
                    )
            else:
                result = split_nodes_delimiter(
                    [case["input_node"]], case["delimiter"],
                    get_node_type(case["delimiter"])
                )
                self.assertEqual(result, case["expected"])

    if __name__ == "__main__":
        unittest.main()
