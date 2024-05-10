import unittest
from utils.inline_markdown import (
    extract_markdown_links,
    extract_markdown_images,
)


class TestExtractMarkdown(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            {
                "method": extract_markdown_images,
                "text": (
                    "This is text with an "
                    "![image](https://exampleUrl/example.png) "
                    "and ![another](https://exampleUrl/another_example.png)"
                ),
                "expected": [
                    ("image", "https://exampleUrl/example.png"),
                    ("another", "https://exampleUrl/another_example.png"),
                ],
            },
            {
                "method": extract_markdown_links,
                "text": (
                    "This is text with a [link](https://www.example.com) "
                    "and [another](https://www.example.com/another)"
                ),
                "expected": [
                    ("link", "https://www.example.com"),
                    ("another", "https://www.example.com/another"),
                ],
            },
        ]

    def test_extract_markdown(self):
        for test_case in self.test_cases:
            result = test_case["method"](test_case["text"])
            expected = test_case["expected"]
            self.assertEqual(result, expected)

    if __name__ == "__main__":
        unittest.main()
