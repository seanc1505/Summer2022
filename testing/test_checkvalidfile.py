from click import File
import pytest
from utilities.checkvalidfile import checkValidFile

def testcheckvalidfile_nomake_pass():
    path = "./test/test.txt"
    file = checkValidFile(dir=path,make_if_fail=False)
    assert(file==path)