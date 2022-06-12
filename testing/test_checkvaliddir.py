import pytest
from utilities.checkvaliddir import checkValidDirectory
import os


def testcheckvaliddir_nomake_pass():
    path = "./test"
    dir = checkValidDirectory(dir=path,make_if_fail=False)
    assert(path==dir)

def testcheckvaliddir_make_pass():
    path = "./test/blah"
    dir = checkValidDirectory(dir=path,make_if_fail=True)
    assert(path==dir)
    os.rmdir(path) 

