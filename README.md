# Brain

Brain is the ultra simple CLI app I use to manage a plain list of .md files of  
any kind.
It just adds, removes, edit and list .md files in a directory.
Files directory and text editor are fully configurable at /brain/config.py

You will not find anything fancy here. This just solves the problem of having  
to go out of your terminal to read or note something, that's it.
There's no built support for files tree structure. This is intended for a  
plain list of files, so if you need something more complex, this is not the  
right tool for you.

[## Commands:]

``brain add <file_name>``: Add a new file with the given name. If already  
exists works like edit.

``brain remove <file_name>``: Remove the file with the given name. If the file  
does not exist, nothing will happen.

``brain edit <file_name>``: Open the file with the given name in the  
configured text editor. If the file does not exist, it will be created first.

``brain list``: List all files in the configured directory.
