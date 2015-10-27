# coding: cp1250
#!/usr/bin/python

import os
import sys
import csv
import argparse

parser = argparse.ArgumentParser(description='Process the text file into records and stores then in Google Spreadsheet')
parser.add_argument('-i', '--input_file', default='./Zgłoszenie.txt', help='input file')
parser.add_argument('-o', '--output_file', default='', help='output file')
parser.add_argument('-f', '--format', choices=['csv','txt'], default='csv', help='output format')
args = parser.parse_args()
if args.output_file == '':
  args.output_file = args.input_file + '.' + args.format
#print args

class Student:
  imie = ''
  nazwisko = ''
  emial = ''
  telefon = ''
  wydzial = ''
  dzial = ''
  doswiadczenie = ''
  motywacja = ''
  pass

database = []

def processFile(name):
  in_body = False
  f = open(name, 'r')
  for line in f:
    #print line'
    if line.startswith('\x0cFrom: "'):
      in_body = False
      #print data
      database.append(data)
    if in_body:
      processLine(line, data)
    if line.startswith('To: <academy@adbglobal.com>'):
      in_body = True
      data = Student()

def processLine(line, data):
  #print line,
  if line.startswith('Imię: '):
    data.imie = line[line.find(': ')+2:len(line)-2].replace('"',"'")
  elif line.startswith('Nazwisko: '):
    data.nazwisko = line[line.find(': ')+2:len(line)-2].replace('"',"'")
  elif line.startswith('E-Mail: '):
    data.email = line[line.find(': ')+2:len(line)-2].replace('"',"'")
  elif line.startswith('Telefon: '):
    data.telefon = line[line.find(': ')+2:len(line)-2].replace('"',"'")
  elif line.startswith('Uczelnia lub pracodawca: '):
    data.uczelnia = line[line.find(': ')+2:len(line)-2].replace('"',"'")
  elif line.startswith('Wydział/specjalizacja/rok lub dział w firmie: '):
    data.wydzial = line[line.find(': ')+2:len(line)-2].replace('"',"'")
  elif line.startswith('Doświadczenie/języki programowania/zainteresowania: '):
    data.doswiadczenie = line[line.find(': ')+2:len(line)-2].replace('"',"'")
  elif line.startswith('Motywacja lub uwagi: '):
    data.motywacja = line[line.find(': ')+2:len(line)-2].replace('"',"'")
  elif len(line) > 1:
    if data.motywacja != '':
      data.motywacja += '\n' + line[:len(line)-2].replace('"',"'")
    elif data.doswiadczenie != '':
      data.doswiadczenie += '\n' + line[:len(line)-2].replace('"',"'")

processFile(args.input_file)

if args.format == 'csv':
  with open(args.output_file, encoding='utf-8', mode='wb') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=['imie','nazwisko','email','telefon','uczelnia','wydzial','doswiadczenie','motywacja'], 
      dialect=csv.excel, delimiter=';')
    csvwriter.writeheader()
    for data in database:
     csvwriter.writerow({'imie':data.imie, 'nazwisko':data.nazwisko, 'email':data.email, 'telefon':data.telefon, 'uczelnia':data.uczelnia, 'wydzial':data.wydzial, 'doswiadczenie':data.doswiadczenie, 'motywacja':data.motywacja})

elif args.format == 'txt':
  for data in database:
    print '{0} {1} {2} {3} {4} {5} {6} {7}"'.format(data.imie, data.nazwisko, data.email, data.telefon, data.uczelnia, data.wydzial, data.doswiadczenie, data.motywacja) 