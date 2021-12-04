#!/usr/bin/env python3
'''
'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('INPUT', type=argparse.FileType(mode='rt'))
parser.add_argument('--part-two', action='store_true')
args = parser.parse_args()
