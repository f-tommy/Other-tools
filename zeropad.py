#!/usr/bin/env python3
# echo "aaa" | zerofill.py 4
#  0aaa
# Created by f-tommy, 2018/09/04
import fileinput
import argparse

# Obtain argument
parser = argparse.ArgumentParser()
parser.add_argument("td",type=int)
parser.add_argument("files",metavar='FILE', nargs='*')
args = parser.parse_args()

# Process line input
for line in fileinput.input(files=args.files):
    lin = line.rstrip('\n')
    col = lin.split()
    tmp = str(col[0])
    tmp0 = tmp.rjust(args.td,'0')
    tmp1 = ' '.join(col[1:]) # list to string
    print(tmp0,tmp1) 
