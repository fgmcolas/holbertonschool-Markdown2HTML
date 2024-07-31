#!/usr/bin/python3
""" Script that converts Markdown to HTML """

import sys
import os
import re
import hashlib


def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()


def process_markdown(md_content):
    html_content = []
    in_list = None
    list_type = None

    for line in md_content.splitlines():
        match_heading = re.match(r'(#{1,6}) (.+)', line)
        if match_heading:
            level = len(match_heading.group(1))
            text = match_heading.group(2)
            html_content.append(f'<h{level}>{text}</h{level}>')
            in_list = None
            list_type = None
        elif line.startswith('- '):
            if in_list != 'ul':
                if in_list:
                    html_content.append('</ul>')
                html_content.append('<ul>')
                in_list = 'ul'
            html_content.append(f'<li>{line[2:]}</li>')
            list_type = 'ul'
        elif re.match(r'\d+\. ', line):
            if in_list != 'ol':
                if in_list:
                    html_content.append('</ol>')
                html_content.append('<ol>')
                in_list = 'ol'
            html_content.append(f'<li>{line.split(". ", 1)[1]}</li>')
            list_type = 'ol'
        else:
            if in_list:
                html_content.append(f'</{list_type}>')
                in_list = None

            line = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)
            line = re.sub(r'__(.+?)__', r'<em>\1</em>', line)
            line = re.sub(r'\*(.+?)\*', r'<em>\1</em>', line)
            line = re.sub(r'_(.+?)_', r'<em>\1</em>', line)
            line = re.sub(r'\[\[(.+?)\]\]',
                          lambda m: md5_hash(m.group(1)), line)
            line = re.sub(r'\(\((.+?)\)\)', lambda m:
                          m.group(1).replace('c', '').replace('C', ''), line)

            if line.strip():
                html_content.append(f'<p>{line.replace("\n", "<br/>")}</p>')

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
        html_content = process_markdown(md_content)

    with open(html_file, 'w') as html_filename:
        html_filename.write(html_content)

    exit(0)


if __name__ == "__main__":
    main()
