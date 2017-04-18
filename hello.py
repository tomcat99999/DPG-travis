import sys
import multiprocessing as mp
print ("Hello world")
print ("Python  v: %s" % str(sys.version))
print ("cores:     %s" % str(mp.cpu_count()))
