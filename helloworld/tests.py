import os
import unittest

import vivisect.lib.bexfile as v_bexfile
import vivtestfiles.helpers as v_helpers

class HelloWorldTest(unittest.TestCase):

    def test_helloworld_i386_exe(self):
        with v_helpers.testfd('helloworld','hello_i386.exe') as fd:
            bex = v_bexfile.getBexFile(fd)
            self.assertEqual( bex.baseaddr(), 0x400000 )

    def test_helloworld_amd64_exe(self):
        with v_helpers.testfd('helloworld','hello_amd64.exe') as fd:
            bex = v_bexfile.getBexFile(fd)
            self.assertEqual( bex.baseaddr(), 0x140000000 )

