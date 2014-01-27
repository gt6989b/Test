#!/usr/bin/python

##----------------------------------------------------------------------------##
## \file  unitCircle.py                                                       ##
## \brief Study of providing uniform random selection from the unit circle    ##
##                                                                            ##
##----------------------------------------------------------------------------##

from datetime import datetime as dt
import sys

def parseCommandLine(argv):
    import argparse

    parser = argparse.ArgumentParser(
                 description = 'Unit circle random selection study')

    # parser.add_argument("inFile", type = argparse.FileType('r'),
    #                     help = 'input sudoku board')
    # parser.add_argument("-o", "--outFile", type = argparse.FileType('w'),
    #                     help = 'file to publish the output board to')
    # parser.add_argument("-d", "--db", help = "database (instance) name")
    parser.add_argument("-p", "--prefix", default = '',
                        help = "graph prefix")
    parser.add_argument("-N", "--num", type = int, default = 1000,
                        help = "# of points to plot")
    # parser.add_argument("-t", "--runTime",
    #                     help = "run as of a YYYYMMDDHHMMSS (default: now)")
    # parser.add_argument("-v", "--verbose", action = "store_true",
    #                     help = "increase output verbosity")

    opts = parser.parse_args(argv[1:]) # ignore program name
    return opts

def getResults(size = 100):
    import numpy as np

    results = [[None,None]]*4

    # z --> 1/z
    results[0] = np.random.uniform(-1, 1, size), np.random.uniform(-1, 1, size)
    x,y = results[0]
    r = x*x + y*y
    for i in range(size):
        if r[i] > 1:
           x[i] /=  r[i]
           y[i] /= -r[i]
    results[0] = list(results[0]) + ['Complex Inversion']

    # z --> |1/z| same angle
    results[1] = np.random.uniform(-1, 1, size), np.random.uniform(-1, 1, size)
    x,y = results[1]
    r = x*x + y*y
    for i in range(size):
        if r[i] > 1:
           x[i] /= r[i]
           y[i] /= r[i]
    results[1] = list(results[1]) + ['Invert radius']

    # uniform r, theta
    r, a = np.random.uniform(0, 1, size), np.random.uniform(-np.pi, np.pi, size)
    results[2] = list(r*[np.cos(a), np.sin(a)]) + ['Uniform r and theta']

    # uniform in the circle
    results[3] = [(x,y) for x, y in zip(np.random.uniform(-1, 1, 4*size), \
                                        np.random.uniform(-1, 1, 4*size)) \
                      if x*x + y*y <= 1.][:size]
    results[3] = zip(*results[3]) + ['Uniform circle from box'] # unzip

    return results

def plotResults(results, prefix = '', outFormat = 'png'):
    import matplotlib.pyplot as plt

    for idx in range(len(results)):
        x,y, label = results[idx]
        fig = plt.figure()
        unitCircle = plt.Circle((0,0), radius = 1, fill = False, color = 'k')
        plt.plot(x, y, 'ro', markersize = 1)
        plt.xlim(xmin = -1, xmax = 1) # force y between -1 and 1
        plt.ylim(ymin = -1, ymax = 1) # force y between -1 and 1
        plt.axes().add_patch( unitCircle )
        plt.title(label)
        fig.savefig('%s.%d.%s' % (prefix, idx, outFormat),
                        format      = outFormat,
                        transparent = False)
        plt.close()

def main(argv = None):
    print dt.now(), 'Setting up the run'
    if argv is None:
        argv = sys.argv

    opts = parseCommandLine(argv)
    if opts is None:
        return 0

    print dt.now(), 'Beginning the run'

    results = getResults(size = opts.num)
    print dt.now(), 'Results computed with %d points each' % opts.num

    plotResults(results = results, prefix = opts.prefix)
    print dt.now(), 'Graphical summary generated'

    print dt.now(), 'Completed'
    return 0

if __name__ == '__main__':
    sys.exit(main())
