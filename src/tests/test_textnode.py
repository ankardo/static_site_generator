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

            # Same Url Test case
            (TextNode("This is a text node", text_type_text,
                      "https://www.ex.com"),
             TextNode("This is a text node", text_type_text,
                      "https://www.ex.com"),
             self.assertEqual),

            # None Url Test case
            (TextNode("This is a text node", text_type_bold),
             TextNode("This is a text node", text_type_bold, None),
             self.assertEqual),

            # Non equal text Test case
            (TextNode("This is a text node", text_type_bold),
             TextNode("Another text node", text_type_bold),
             self.assertNotEqual),

            # Non equal text type Test case
            (TextNode("This is a text node", text_type_bold),
             TextNode("This is a text node", text_type_italic),
             self.assertNotEqual),

            # Non equal Url Test case
            (TextNode("This is a text node",
                      text_type_bold, "https://www.ex.com"),
             TextNode("This is a text node",
                      text_type_bold, "https://www.aex.com"),
             self.assertNotEqual),
        ]
        for first_node, second_node, assertion_method in test_cases:
            with self.subTest(first_node=first_node, second_node=second_node):
                assertion_method(first_node, second_node)

    def test_repr(self):
        node = TextNode("This is text node", text_type_bold,
                        "https://www.ex.com")
        expected_repr = "TextNode(This is text node, bold, https://www.ex.com)"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()
