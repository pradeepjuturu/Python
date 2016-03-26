# Simple program to create a directory
import os
import shutil
import sys
import argparse

def copyFile(args):
    if not os.path.exists(args.destination):
        os.makedirs(args.destination)
    srcFile = args.source + args.file
    if not os.path.isfile(srcFile):
        print "File doesn't exist"
        sys.exit(1)
    print "Copying file {0} to {1}".format(srcFile, args.destination)
    shutil.copy2(srcFile, args.destination)
def main():
    print "Start !"
    parser = argparse.ArgumentParser(description="Simple utility to copy a file")
    parser.add_argument("-src", "--source", help="Source directory", required=True)
    parser.add_argument("-dst", "--destination", help="Destination directory", required=True)
    parser.add_argument("-f", "--file", help="File to be copied", required=True)
    args = parser.parse_args()
    copyFile(args)
    #if not os.path.exists("testdir"):
     #   os.makedirs("testdir")
if __name__ == "__main__":
    main()
