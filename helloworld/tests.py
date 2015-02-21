import os
import unittest

import vivtestfiles.helpers as v_helpers

class HelloWorldTest(unittest.TestCase):

    def test_helloworld_i386_exe(self):
        with v_helpers.testfd('helloworld','hello_i386.exe') as fd:
            pass

    def test_helloworld_amd64_exe(self):
        with v_helpers.testfd('helloworld','hello_i386.exe') as fd:
            pass

