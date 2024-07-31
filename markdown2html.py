#!/usr/bin/python3
""" Script that converts Markdown to HTML """

import sys
import os
import re


def convert_markdown(md_content):
    """ Convert Markdown headings and unordered lists to HTML. """
    html_content = []
    in_list = False

    for line in md_content.splitlines():
        match_heading = re.match(r'(#{1,6}) (.+)', line)
        if match_heading:
            level = len(match_heading.group(1))
            text = match_heading.group(2)
            html_content.append(f'<h{level}>{text}</h{level}>')
            in_list = False
        elif line.startswith('- '):
            if not in_list:
                html_content.append('<ul>')
                in_list = True
            html_content.append(f'<li>{line[2:]}</li>')
        else:
            if in_list:
                html_content.append('</ul>')
                in_list = False
            html_content.append(line)

    if in_list:
        html_content.append('</ul>')

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
        html_content = convert_markdown(md_content)

    with open(html_file, 'w') as html_filename:
        html_filename.write(html_content)

    exit(0)


if __name__ == "__main__":
    main()
