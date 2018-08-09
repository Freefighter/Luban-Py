import sys
from luban import Luban

compressor = Luban()
for path in sys.argv[1:]:
    compressor.setPath(path)
    compressor.compress()
