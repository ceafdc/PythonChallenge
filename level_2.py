#!/usr/bin/env python3

# url: http://www.pythonchallenge.com/pc/def/ocr.html

from collections import Counter

with open('ocr.txt') as fin:
    text = fin.read().replace('\n', '')

histogram = Counter(text)
avg = len(text)/len(histogram)

text = [c for c in text if histogram[c] < avg]
text = ''.join(text)

print(text)

# next: http://www.pythonchallenge.com/pc/def/equality.html
