import os
import pytest
import sys
sys.path.insert(1, 'C:/Users/scahill2/Documents/Git/Summer2022/utilities')
from checkvaliddir import checkValidDirectory


def testcheckvaliddir_nomake_pass():
    path = "./test"
    dir = checkValidDirectory(dir=path, make_if_fail=False)
    assert(path == dir)


def testcheckvaliddir_make_pass():
    path = "./test/blah"
    dir = checkValidDirectory(dir=path, make_if_fail=True)
    assert(path == dir)
    os.rmdir(path)
