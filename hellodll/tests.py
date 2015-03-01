import os
import unittest

import vivisect.workspace as v_workspace
import vivisect.lib.bexfile as v_bexfile
import vivtestfiles.helpers as v_helpers

class HelloWorldTest(unittest.TestCase):

    def test_hellodll_i386(self):

        with v_helpers.testfd('hellodll','hellodll_i386.dll') as fd:
            bex = v_bexfile.getBexFile(fd)

            self.assertEqual( bex.bintype(), 'dyn' )
            self.assertIn( (4096,'foo','unkn'), bex.exports() )
            self.assertIn( (40320, 'kernel32', 'GetTickCount'), bex.imports() )

    def test_hellodll_amd64(self):

        with v_helpers.testfd('hellodll','hellodll_amd64.dll') as fd:
            bex = v_bexfile.getBexFile(fd)

            self.assertEqual( bex.bintype(), 'dyn' )
            self.assertIn( (4096,'foo','unkn'), bex.exports() )
            self.assertIn( (46360, 'kernel32','QueryPerformanceCounter'), bex.imports() )
