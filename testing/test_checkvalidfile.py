
import pytest
import sys
sys.path.insert(1, 'C:/Users/scahill2/Documents/Git/Summer2022/utilities')
from checkvalidfile import checkValidFile

def testcheckvalidfile_fileexists_pass():
    path = "C:/Users/scahill2/Documents/Git/Summer2022/test/test.txt"
    file = checkValidFile(path)
    assert(file == path)


def testcheckvalidfile_filenoexist_pass():
    