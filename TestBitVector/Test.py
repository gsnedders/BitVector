#!/usr/bin/env python

import os.path
import sys
import unittest

base_path = os.path.split(__file__)[0]
lib_dir = os.path.join(base_path, os.path.pardir, 'BitVector')
sys.path.insert(0, lib_dir)

import TestBooleanLogic
import TestConstructors
import TestComparisonOps
import TestPermutations
import TestCircularShifts

class BitVectorTestCase( unittest.TestCase ):
    def checkVersion(self):
        import BitVector


testSuites = [unittest.makeSuite(BitVectorTestCase, 'check')] 

for test_type in [
            TestConstructors,
            TestBooleanLogic,
            TestComparisonOps,
            TestPermutations,
            TestCircularShifts,
    ]:
    testSuites.append(test_type.getTestSuites('check'))

def getTestDirectory():
    try:
        return os.path.abspath(os.path.dirname(__file__))
    except:
        return '.'

import os

os.chdir(getTestDirectory())

runner = unittest.TextTestRunner()
runner.run(unittest.TestSuite(testSuites))

