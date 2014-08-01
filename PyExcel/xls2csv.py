#!/usr/bin/python

from sys  import argv
from xlrd import open_workbook

wkbook = open_workbook(argv[1])
for s in wkbook.sheets():
    print 'Sheet:', s.name
