#!/usr/bin/python3
""" Script that converts Markdown to HTML """

import sys
import os
import re


def convert_headings(md_content):
    """ Convert Markdown headings to HTML headings. """
    html_content = []
    for line in md_content.splitlines():
        match = re.match(r'(#{1,6}) (.+)', line)
        if match:
            level = len(match.group(1))
            text = match.group(2)
            html_content.append(f'<h{level}>{text}</h{level}>')
        else:
            html_content.append(line)
    return '\n'.join(html_content)


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.exists(md_file):
        sys.stderr.write(f"Missing {md_file}\n")
        exit(1)

    with open(md_file, 'r') as md_filename:
        md_content = md_filename.read()
        html_content = convert_headings(md_content)

    with open(html_file, 'w') as html_filename:
        html_filename.write(html_content)

    exit(0)


if __name__ == "__main__":
    main()
