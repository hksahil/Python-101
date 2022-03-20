#!/usr/bin/env python
# coding: utf-8

# ### Windows Command Line  

# In[1]:


get_ipython().system('dir')


# #### Note:In CLI, foldersare called directories
# - Give list of all files and folders in current directory: ```dir```
#     - Files are tagged as Blanks
#     - Folders are tagged as ```<DIR>```
# - Create Folder: ```mkdir <name of folder>```
# - Delete folder: ```rmdir <name of folder>```
#     - Use ```rmdir /s <name of directory>``` if  folder has stuff in it
# - Going one level up in Directory: ```cd <name>```
#     - Going to any folder: ```cd C:\Desktop\Folder\Subfolder```
# - Going one level down in Directory: ```cd ..```
# - Clear Screen: ```cls```
# - Open Files: Type name of file without any command
#     - It opens file in default program

# ### Installing packages

# To install latest version(default) : ```!pip <commands> [options] [name of library] ```
# 
# To install previous/specific version: ```!pip <commands> [options] [name of library]==Syntax Number``` 

# - Commands:
#    - install
#    - uninstall
#    - freeze - Gives a list of all the modules installed with their version in one go in Module name==module version format
# - Options:
#     - ```-h or --help``` to get help
#     - ```pip -h``` Overall help
#     - ```pip subcommand -h``` gives you help for that sub command
#     - ```-y``` automatically says yes to prompts
#     - ```-V``` To know current version
#     - ```-U``` To upgrade package to the latest versions 
#     - ```--force-reinstall ``` Reinstall all packages
