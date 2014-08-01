#!/usr/bin/python

import sys, xlrd

from datetime import date, datetime as dt

def Transpose(arr):
    return [[arr[r][c] for r in range(len(arr))] for c in range(len(arr[0]))]

class Table:
    def __init__(self, name = '', cols = '', types = [], data = []):
        self.name  = name
        self.cols  = cols
        self.types = types
        self.data  = data

class excelDB:
    def __init__(self, dbFile, verboseOutput = False):
        self.verbose = verboseOutput
        self.tables = {}
        wb = self.OpenAndValidateWorkbook(xlFile = dbFile)
        for s in wb.sheets():
            if self.verbose:
               print dt.now(), 'Processing sheet', s.name
            self.SheetToTable(s)

    def OpenAndValidateWorkbook(self, xlFile):
        wb = xlrd.open_workbook(xlFile)

        # make sure names are convertible to regular string, not Unicode
        names = set([s.name.encode('ascii', 'ignore') for s in wb.sheets()])
        if len(names) != len(wb.sheets()):
            raise RuntimeError('sheet names of %s need unicode' % xlFile)
        if self.verbose:
            print dt.now(), 'Workbook %s validated' % xlFile
        return wb

    def SheetToTable(self, xlSheet):
        name = xlSheet.name.encode('ascii', 'ignore')
        cols = [xlSheet.cell(0,col).value.encode('ascii', 'ignore') \
                        for col in range(xlSheet.ncols)]
        colTypeSets = [set([xlSheet.cell(row,col).ctype \
                        for row in range(xlSheet.nrows)]) \
                        for col in range(xlSheet.ncols)]
        types = [s.pop() if len(s) == 1 else '' for s in colTypeSets]

        # initially make a list of columns
        data = [[xlSheet.cell(row,col).value \
                        for row in range(1, xlSheet.nrows)] \
                        for col in range(xlSheet.ncols)]
        for idx in range(len(types)): # actually indexes over the columns
            type = types[idx]
            if type == xlrd.XL_CELL_TEXT:
               data[idx] = [x.encode('ascii', 'ignore') for x in data[idx]]
#            elif type == xlrd.XL_CELL_DATE:

        self.tables[name] = Table(name  = name,  cols = cols,
                                  types = types, data = Transpose(arr = data))

def ParseArgs(argv):
    import argparse
    parser = argparse.ArgumentParser(description='Simulate DB routines')
    parser.add_argument('dbFile', help = 'database xl file')
    parser.add_argument('-v', "--verbosity",
                        dest = 'verbose', action = 'store_true',
                        help = 'verbose output')
    try:
        args = parser.parse_args(argv[1:])
    except Exception as err:
        raise RuntimeError('str(err)\nUsage: ' + parser.usage())

    return args

def main(argv = None):
    if argv is None:
        argv = sys.argv
    try:
        args = ParseArgs(argv)
        db   = excelDB(dbFile        = args.dbFile,
                       verboseOutput = args.verbose)
        for t in db.tables.values():
            print 'Table %s (%d rows, %d cols)\nCols: %s\nTypes %s\nSample %s\n' \
                  %(t.name, len(t.data), len(t.data[0]),
                    ', '.join(t.cols), ', '.join([str(x) for x in t.types]),
                    ', '.join([str(x) for x in t.data[0]]))

    except Exception as err:
        print >>sys.stderr, str(err)
        return 2

if __name__ == "__main__":
    sys.exit(main())
