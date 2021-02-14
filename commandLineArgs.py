'''
Command-line arguments

* Python provides a getopt module that helps you parse command-line options and arguments.

* The Python sys module provides access to any command-line arguments via the sys.argv. 

'''
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
