import os
import unittest

import vivisect.workspace as v_workspace
import vivisect.lib.bexfile as v_bexfile
import vivtestfiles.helpers as v_helpers

class LinuxVivTests(unittest.TestCase):

    def test_linux_ls_amd64(self):
        with v_helpers.testfd('linux','ls.amd64') as fd:
            bex = v_bexfile.getBexFile(fd)

            self.assertEqual( bex.arch(), 'amd64' )
            self.assertEqual( bex.format(), 'elf' )
            self.assertEqual( bex.bintype(), 'exe' )
            #self.assertEqual( bex.platform(), 'linux' )
            self.assertEqual( bex.byteorder(), 'little' )

            self.assertEqual( bex.baseaddr(), 0x400000 )
            self.assertIsNotNone( bex.section('.text') )

            print('prelink',bex.info('elf:prelink'))
