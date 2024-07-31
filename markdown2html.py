#!/usr/bin/python3
""" Script that converts Markdown to HTML """

import sys
import os
import markdown


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.exists(md_file):
        sys.stderr.write(f"Missing {md_file}\n")
        exit(1)

    try:
        with open(md_file, 'r', encoding='utf-8') as md_filename:
            md_content = md_filename.read()
            html_content = markdown.markdown(md_content)
    except UnicodeDecodeError:
        sys.stderr.write(f"Error: {md_file} is not UTF-8 encoded\n")
        exit(1)

    with open(html_file, 'w', encoding='utf-8') as html_filename:
        html_filename.write(html_content)

    exit(0)


if __name__ == "__main__":
    main()