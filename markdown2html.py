#!/usr/bin/python3
""" Script that converts Markdown to HTML """

import sys
import os
import markdown


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.exists(md_file):
        sys.stderr.write(f"Missing {md_file}\n")
        sys.exit(1)

    try:
        with open(md_file, 'r', encoding='utf-8') as md_filename:
            md_content = md_filename.read()
            html_content = markdown.markdown(md_content)

        with open(html_file, 'w', encoding='utf-8') as html_filename:
            html_filename.write(html_content)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
