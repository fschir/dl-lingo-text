"""
Quick and dirty cleanup of the textfile
"""

import os

all_lines = []

with open('corpus/kjv.txt') as corpus_raw:
    for line in corpus_raw:
        all_lines.append(line.strip())

with open('corpus/clean.txt', 'w') as corpus_clean:
    for line in all_lines:
        corpus_clean.write(line)

