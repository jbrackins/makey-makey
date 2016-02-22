# MAKEY-MAKEY
A set of scripts to set up a new project. Generates Makefile, starting .cpp and .h files, and doxygen configuration file.

# AUTHOR
* Julian A. Brackins

# USAGE
In order to run this script, follow these steps:
* create the <project-name> directory in your workspace.
* clone this repository into your workspace as well
* cd wakey-wakey
* ./wakey.sh <project-name>

# FUNCTIONALITY
This program currently builds the following:
* a directory structure that separates src, inc, and doc files
* Doxygen configuration built into your starting .cpp and .h files. Pre-initialized doxygen timeline starting on the current date.
* Makefile containing various make commands for compilation, doxygen generation, and tar archiving

Eventually more functionality may be added, including support for other languages besides C++. Who knows