#!/usr/local/bin/python
# coding: latin-1

import os
import sys                
import csv
import argparse

parser = argparse.ArgumentParser(description='Process the text file into records and stores then in Google Spreadsheet')
parser.add_argument('-f', '--file_output', default='~/Dropbox/ADB/Lista Uczestnikow/Zgłoszenie.txt', help='output file')
parser.add_argument('-o', '--output_format', choices=['cvs','txt'], default='cvs', help='output format')
parser.add_argument('file', help='input file')
parser.add_argument('user', help='google user name')
parser.add_argument('password', help='google password')

args = parser.parse_args()
print args