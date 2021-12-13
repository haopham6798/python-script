
# import OptionParser class 
# from optparse module.
from optparse import OptionParser
  
# create a OptionParser
# class object
parser = OptionParser()
  
# ass options
parser.add_option("-s", "--source",
                  dest = "srcfile",
                  help = "path to imported file", 
                  metavar = "FILE")

parser.add_option("-d", "--destination",
                  dest = "dstfile",
                  help = "path to file config", 
                  metavar = "FILE")

parser.add_option("-q", "--quiet",
                  action = "store_false", 
                  dest = "verbose", default = True,
                  help = "don't print status messages to stdout")
  
(options, args) = parser.parse_args()

srcfile = options.srcfile
dstfile = options.dstfile
if srcfile and dstfile:
    with open(srcfile, 'r') as fout:
        with open(dstfile, 'a') as fin:
            lines = fout.readlines()
            for line in lines:
                fin.write(line)
        fin.close
    fout.close


