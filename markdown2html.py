#!/usr/bin/python3
""" Script that converts Markdown to HTML """

import sys
import os
import markdown
import chardet


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}")
        exit(1)

    encoding = detect_encoding(markdown_file)

    with open(markdown_file, 'r', encoding=encoding) as md_file:
        md_content = md_file.read()

    html_content = markdown.markdown(md_content)

    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    exit(0)


if __name__ == "__main__":
    main()
