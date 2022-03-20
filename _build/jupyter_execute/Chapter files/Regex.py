#!/usr/bin/env python
# coding: utf-8

# ## Regex rules

# - Search for pattern in dataset

# ### Single Character

# - Note: [] denotes set of characters (once only)

# - a a
# - b b
# - c c
# - abc abc
# - [abc] a,b or c
# - [^abc] any character except  a,b and c
# - [a-z] a to z
# - [A-Z] A to Z
# - [0-9] 0 to 9 or \d
# - [^0-9] 0 to 9 or \D
# - [a-zA-Z] a to z,A-Z
# - [a-zA-Z0-9] \w
# - [^a-zA-Z0-9] \W
# - \s whitespace character
# - \S non whitespace character

# ### Frequency of characters

# ?+*{} symbols are used to set frequency

# - occurs 0 or 1 times []?
# - occurs 0 or more times "acx*"
# - occurs 1 or more times "abc+"
# - occurs exactly n times "abc{n}"
# - occurs exactly n or more times []{n,}

# ### More

# - starts with sahil "^sahil"
# - ends with choudhary "choudhary$"
# - any character except newline .
# - either c or d "c|d"
# - capture and group ( )

# ### Options

# - i case insensitive
# - \ to treat them as special characters not as strings
