import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle

print "Loading matrix X ..."

f = open('matrix.pkl','rb') # open the file in read binary mode
# load the data in the .pkl file into a new variable spmat
matrix = cPickle.load(f) 
f.close()

print "matrix X loaded"