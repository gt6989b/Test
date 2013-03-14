#!/usr/bin/python

##----------------------------------------------------------------------------##
## \file  sudoku.py                                                           ##
## \brief Toy implementation of a sudoku solver                               ##
##                                                                            ##
## Given an input sudoku board file (a CSV format with numeric or empty       ##
## columns, of square shape), this solves the sudoku problem, publishing the  ##
## result.                                                                    ##
##----------------------------------------------------------------------------##

# import now - to make help screen quicker...
from datetime import datetime as dt
import os, sys

def computeExcludedSection(idx, size):
    start = (idx/size)*size  # integer arithmetic
    return range(start, idx) + range(idx+1, start+size)

class Board:
    '''A sudoku board'''
    blank = 0

    def __init__(self):
        self.Init()

    def __init__(self, inFile):
        self.Init()
        self.ReadFromFile(inFile)

    def __str__(self):
        return '\n'.join([','.join([str(elt) for elt in row]) for row in self.data])

    def Dump(self):
	return str(self) + '\n-------------\nCANDIDATES\n----------------\n' \
	  + '\n'.join([','.join([str(x) for x in col]) \
		            for row in self.candidates for col in row])

    def Init(self):
        self.size        = 9
        self.range       = range(self.size)
        self.sectionSize = 3
        self.data        = [x[:] for x in [[self.blank]*self.size]*self.size]

        # construct a list of independent blocks
        self.blocks \
            = [[(x,y) for x in self.range] for y in self.range] + \
              [[(y,x) for x in self.range] for y in self.range]

        for xBase in range(0,self.size,self.sectionSize):
            for yBase in range(0,self.size,self.sectionSize):
                self.blocks.append(\
                    [(x,y) for x in range(xBase,xBase+self.sectionSize) \
                           for y in range(yBase,yBase+self.sectionSize) ])

        self.allCand = range(1,self.size+1)
        # cannot use [allCand]*3*3 here because that copies references
        self.candidates  = [[set(self.allCand) for x in self.range] for y in self.range]

    def ReadFromFile(self, inFile):
        from csv import reader

        rowIdx = 0
        for row in reader(inFile, delimiter = ',', quotechar = '"'):
            [self.Set(row   = rowIdx,
                      col   = colIdx,
                      value = int(row[colIdx])) for colIdx in range(len(row)) \
		                                if  row[colIdx]]
            rowIdx += 1

    def Set(self, row, col, value):
        self.data[row][col] = value
        self.candidates[row][col].clear()

        updateSet = set([(row, x) for x in self.range])
        updateSet.update([(x, col) for x in self.range])

        rows = computeExcludedSection(row, self.sectionSize)
        cols = computeExcludedSection(col, self.sectionSize)
        updateSet.update([(x,y) for x in rows for y in cols])

        for (rowIdx, colIdx) in updateSet:
            self.candidates[rowIdx][colIdx].discard(value)

def Singles(board):
    return [(row, col, iter(board.candidates[row][col]).next())\
                for row in board.range for col in board.range \
                    if len(board.candidates[row][col]) == 1]

def OnlyValues(board):
    candidates = set([])
    # precompute the memberships

    for block in board.blocks:
        for value in board.allCand:
            members = [(row,col) for (row,col) in block \
                                  if value in board.candidates[row][col]]
            if len(members) == 1:
                candidates.add((members[0][0], members[0][1], value))
    return candidates

def parseCommandLine(argv):
    import argparse

    parser = argparse.ArgumentParser(description = 'Solve sudoku puzzles')

    parser.add_argument("inFile", type = argparse.FileType('r'),
                        help = 'input sudoku board')
    parser.add_argument("-o", "--outFile", type = argparse.FileType('w'),
                        help = 'file to publish the output board to')
    parser.add_argument("-v", "--verbose", action = "store_true",
                        help = "increase output verbosity")

    opts = parser.parse_args(argv[1:]) # ignore program name
    return opts

def main(argv = None):
    if argv is None:
        argv = sys.argv

    opts = parseCommandLine(argv)
    if opts is None:
        return 0

    if opts.verbose:
        print '%s Reading the board from %s' % (str(dt.now()), opts.inFile.name)

    board = Board(opts.inFile)

    if opts.verbose:
        print '%s Solving the board' % str(dt.now())

    techniques = [Singles, OnlyValues]
    inferences = 1 # actually a list of tuples, will be over-written
    while inferences:
        for technique in techniques:
            inferences = technique(board)
            if inferences:
                for (row, col, value) in inferences:
                    board.Set(row = row, col = col, value = value)
                break # restart techniques from the most basic ones

    if opts.outFile:
	if opts.verbose:
	    print '%s Writing the board to %s' % (str(dt.now()), opts.outFile.name)
	opts.outFile.write(str(board))
    else:
        print board

    return 0

if __name__ == '__main__':
    sys.exit(main())
