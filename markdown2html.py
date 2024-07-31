#!/usr/bin/python3
""" Script that converts Markdown to HTML """

import sys
import os
import re


def convert_markdown(md_content):
    """
    Convert Markdown headings, unordered lists, and ordered lists to HTML.
    """
    html_content = []
    in_list = False
    list_type = None

    for line in md_content.splitlines():
        match_heading = re.match(r'(#{1,6}) (.+)', line)
        if match_heading:
            level = len(match_heading.group(1))
            text = match_heading.group(2)
            if in_list:
                if list_type:
                    html_content.append(f'</{list_type}>')
                in_list = False
                list_type = None
            html_content.append(f'<h{level}>{text}</h{level}>')
        elif re.match(r'\d+\. ', line):
            if not in_list or list_type != 'ol':
                if in_list:
                    html_content.append(f'</{list_type}>')
                html_content.append('<ol>')
                list_type = 'ol'
                in_list = True
            html_content.append(f'<li>{line.split(". ", 1)[1]}</li>')
        elif line.startswith('- '):
            if not in_list or list_type != 'ul':
                if in_list:
                    html_content.append(f'</{list_type}>')
                html_content.append('<ul>')
                list_type = 'ul'
                in_list = True
            html_content.append(f'<li>{line[2:]}</li>')
        else:
            if in_list:
                html_content.append(f'</{list_type}>')
                in_list = False
                list_type = None
            html_content.append(line)

    if in_list:
        html_content.append(f'</{list_type}>')

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
