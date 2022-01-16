# Write a Python program that prints all ‘.py’ files from a directory.
# Give the file extension as a parameter.

import argparse
import os
import sys
import glob

parser = argparse.ArgumentParser()
parser.add_argument('--ext', help='files extension', default = "py")
args = parser.parse_args()

dir_tmpl = os.path.dirname(sys.argv[0])+"/*."+args.ext

print("Template:\n", dir_tmpl)

print("Files:\n","\n".join(glob.glob(dir_tmpl)))