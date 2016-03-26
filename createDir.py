# Simple program to create a directory
import os
import sys

def main():
    print "Start !"
    if not os.path.exists("testdir"):
        os.makedirs("testdir")
if __name__ = "__main__":
    main():
