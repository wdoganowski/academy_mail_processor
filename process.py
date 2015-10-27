#!/usr/local/bin/python
# coding: latin-1

import os
import sys                

def usage():
  sys.exit('Usage: {0} [-f file] [-o csv|txt]'.format(sys.argv[0]))


input_file = ''
if '-f' in sys.argv:
  n = sys.argv.index('-f')
  if len(sys.argv) > n+1 and sys.argv[n+1] != '-o':
    input_file = sys.argv[n+1]
  else:
    usage()

if input_file == '':
  input_file = '/Users/Wojtek/Dropbox/ADB/Lista Uczestnikow/Zgłoszenie.txt'
  print 'Using default file', input_file  

output_format = 'csv'
if '-o' in sys.argv:
  n = sys.argv.index('-o')
  if len(sys.argv) > n+1  and sys.argv[n+1] in ('csv', 'txt'):
    output_format = sys.argv[n+1]
  else:
    usage()  

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
    #print line,
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

processFile(input_file)

if output_format == 'csv':
  print '"Imię","Nazwisko","E-Mail","Telefon","Uczelnia/pracodawca","Wydział/dział","Doswiadczenie","Motywacja"'
  for data in database:
    print '"{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}"'.format(data.imie, data.nazwisko, data.email, data.telefon, data.uczelnia, data.wydzial, data.doswiadczenie, data.motywacja)
elif output_format == 'txt':
  for data in database:
    print '{0} {1},'.format(data.imie, data.nazwisko)
else:
  usage()  