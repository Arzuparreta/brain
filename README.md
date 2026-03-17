# Brain

Brain is the ultra simple CLI that I use to manage a plain list of .md files  
of any kind. It just adds, removes, edit and list .md files in a directory.

Files directory and text editor are fully configurable at /brain/config.py

You will not find anything fancy here. This just solves the problem of  
having to get out of your terminal (if you use an in-terminal editor) to  
read or note something, that's it.

## Commands
``brain edit <file_name>``: Open the file with the given name in the  
configured text editor. If the file does not exist, root brain  
directory will be opened in your text editor.

``brain add <file_name>``: Add a new file with the given name. If already  
exists works like edit.

``brain remove <file_name>``: Remove the file with the given name. If the file  
does not exist, nothing will happen.

``brain list``: List all files in the configured directory.
