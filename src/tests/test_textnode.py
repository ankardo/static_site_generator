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
    def setUp(self):
        self.test_eq_cases = [

            (TextNode("This is a text node", text_type_text),
             TextNode("This is a text node", text_type_text),
             self.assertEqual),

            (TextNode("This is a bold node", text_type_bold),
             TextNode("This is a bold node", text_type_bold),
             self.assertEqual),

            (TextNode("This is a italic node", text_type_italic),
             TextNode("This is a italic node", text_type_italic),
             self.assertEqual),

            (TextNode("This is a code node", text_type_code),
             TextNode("This is a code node", text_type_code),
             self.assertEqual),

            (TextNode("This is a image node", text_type_image),
             TextNode("This is a image node", text_type_image),
             self.assertEqual),

            (TextNode("This is a link node", text_type_link),
             TextNode("This is a link node", text_type_link),
             self.assertEqual),

            (TextNode("This is a text node", text_type_text,
                      "https://www.ex.com"),
             TextNode("This is a text node", text_type_text,
                      "https://www.ex.com"),
             self.assertEqual),

            (TextNode("This is a text node", text_type_bold),
             TextNode("This is a text node", text_type_bold, None),
             self.assertEqual),

            (TextNode("This is a text node", text_type_bold),
             TextNode("Another text node", text_type_bold),
             self.assertNotEqual),

            (TextNode("This is a text node", text_type_bold),
             TextNode("This is a text node", "italic"),
             self.assertNotEqual),

            (TextNode("This is a text node",
                      text_type_bold, "https://www.ex.com"),
             TextNode("This is a text node",
                      text_type_bold, "https://www.aex.com"),
             self.assertNotEqual),
        ]

    def test_eq(self):
        for first_node, second_node, assertion_method in self.test_eq_cases:
            with self.subTest(first_node=first_node, second_node=second_node):
                assertion_method(first_node, second_node)

    def test_repr(self):
        node = TextNode("This is text node", text_type_bold,
                        "https://www.ex.com")
        expected_repr = "TextNode(This is text node, bold, https://www.ex.com)"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()
