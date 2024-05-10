import unittest

from nodes.textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestTextNode(unittest.TestCase):

    def test_eq(self):

        test_cases = [
            (
                "Type Test Case - Text Type",
                TextNode("This is a text node", text_type_text),
                TextNode("This is a text node", text_type_text),
                self.assertEqual
            ),
            (
                "Type Test Case - Bold Type",
                TextNode("This is a bold node", text_type_bold),
                TextNode("This is a bold node", text_type_bold),
                self.assertEqual
            ),
            (
                "Type Test Case - Italic Type",
                TextNode("This is a italic node", text_type_italic),
                TextNode("This is a italic node", text_type_italic),
                self.assertEqual
            ),
            (
                "Type Test Case - Code Type",
                TextNode("This is a code node", text_type_code),
                TextNode("This is a code node", text_type_code),
                self.assertEqual
            ),
            (
                "Type Test Case - Image Type",
                TextNode("This is a image node", text_type_image),
                TextNode("This is a image node", text_type_image),
                self.assertEqual
            ),
            (
                "Type Test Case - Link Type",
                TextNode("This is a link node", text_type_link),
                TextNode("This is a link node", text_type_link),
                self.assertEqual
            ),
            (
                "Same Url Test Case",
                TextNode("This is a text node",
                         text_type_text, "https://www.ex.com"),
                TextNode("This is a text node",
                         text_type_text, "https://www.ex.com"),
                self.assertEqual
            ),
            (
                "None Url Test Case",
                TextNode("This is a text node", text_type_bold),
                TextNode("This is a text node", text_type_bold, None),
                self.assertEqual
            ),
            (
                "Non Equal Text Test Case",
                TextNode("This is a text node", text_type_bold),
                TextNode("Another text node", text_type_bold),
                self.assertNotEqual
            ),

            (
                "Non Equal Text Type Test Case",
                TextNode("This is a text node", text_type_bold),
                TextNode("This is a text node", text_type_italic),
                self.assertNotEqual
            ),
            (
                "Non Equal Url Test Case",
                TextNode("This is a text node", text_type_bold,
                         "https://www.ex.com"),
                TextNode("This is a text node", text_type_bold,
                         "https://www.aex.com"),
                self.assertNotEqual
            ),
        ]

        for case_name, first_node, second_node, method in test_cases:
            with self.subTest(case_name=case_name):
                method(first_node, second_node,
                       msg=f"Test case: {case_name}")

    def test_repr(self):
        node = TextNode("This is text node", text_type_bold,
                        "https://www.ex.com")
        expected_repr = "TextNode(This is text node, bold, https://www.ex.com)"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()
