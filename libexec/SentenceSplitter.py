#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys

indentation_pattern = re.compile('^　')
reporter_pattern = re.compile('(?:^【.+?】|【.+?】$)')

body = str(sys.stdin.read().rstrip(), 'utf-8')
buffer = ''
sentences = []
p_flag = False

for i in range(0, len(body)):
    c = body[i:i+1]
    if c != '\n':
        buffer = buffer + c
    if c == '。' and p_flag == False:
        sentences.append(buffer)
        buffer = ''
    if c == '「':
        p_flag = True
    if c == '」' and p_flag == True:
        p_flag = False
        if body[i+1:i+2] == '\n':
            sentences.append(buffer)
            buffer = ''

for sentence in sentences:
    sentence = indentation_pattern.sub('', sentence)
    sentence = reporter_pattern.sub('', sentence)
    if sentence != '':
        print('%s' % (sentence.encode('utf-8')))
