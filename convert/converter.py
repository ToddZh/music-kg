from __future__ import print_function

import os
import subprocess


class PyRDF2Ntriples(object):
    def __init__(self):
        pass

    def convertTTL2NT(self, filepath):
        #Save to the same folder with .nt extension
        (outputDir, outputFile) = os.path.split(os.path.abspath(filepath))
        outputFile = outputFile.split(".")[0] + ".nt"
        outputPath = os.path.join(outputDir, outputFile)
        self.serdiTTL2NT(filepath, outputPath)

    def serdiTTL2NT(self, inpath, outpath):
        serdiCommand = "serdi -i turtle -o ntriples -b -q %s" % (inpath)
        p = self.execute(serdiCommand)
        f = open(outpath, "wb+")
        for line in p.stdout.readlines():
            print(line, file=f, end="")
        f.close()

    def executeRapper(self, inpath, outpath, serialization):
        pass

    def execute(self, command):
        p = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return p

if __name__ == "__main__":
    currentPath = os.path.dirname(os.path.realpath(__file__))
    testTtlPath = os.path.abspath(os.path.join(currentPath, "../test/data/test.ttl"))

    #instantiate class
    rdf2nt = PyRDF2Ntriples()

    #Test Ttl to nt conversion
    rdf2nt.convertTTL2NT(testTtlPath)

    

    import ipdb; ipdb.set_trace()
    print("pass")
