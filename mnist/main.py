import cPickle as pickle
import gzip
import random

from numpy import *
# extract a subset of the data

# compressed data
data_orig="mnist.pkl.gz"

# file to save data
data = "mnist_liteR1.pkl.gz"


f_orig=gzip.open(data_orig)

# load data into the 3 data sets
print " LOADING . . . . . ",
training_set,validation_set,test_set=pickle.load(f_orig)

image=training_set[0][0]


for i in image:
    print i

