#!/usr/bin/env python
# coding: utf-8

# ## File paths

# - Windows filenames: 
#     - Uses backslash
#     - C:\some_folder\some_file.txt
# 
# - Most other operating systems:(UNIX,Linux)
#     - Forward slash
#     - /some_folder/some_file.txt
#     
# - Reason:The forward slash character was already taken by UNIX when windows was made so they used a backslash instead.

# - Relative path: The path relative to the folder we are currently working in.
# - Absolute path: The path that is relative to the operating system

# - If you want your Python code to work on both Windows and Mac/Linux, you’ll need to deal with these kinds of platform-specific issues. 
# 
# - Luckily, Python 3 has a new module called pathlib that makes working with files nearly painless.

# - we have to provide path 
# - path->all directories+file name
# 
# - If we just give file name
#     - Python considers it relative
#         - relative to cwd (os.cwd)
#     - For absolute path
#         - Linux: Starts with (/) /home/alarm/filename.txt 
#         - starts with C:\

# - you can use os module or pathlib module or defining paths manually(worst) for the same
