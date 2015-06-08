import os
import unittest

import vivisect.workspace as v_workspace
import vivisect.lib.binfile as v_binfile
import vivtestfiles.helpers as v_helpers

class LinuxVivTests(unittest.TestCase):

    def test_linux_ls_amd64(self):
        with v_helpers.testfd('linux','ls.amd64') as fd:
            bf = v_binfile.getBinFile(fd.read())

            self.assertEqual( bf.getArch(), 'amd64' )
            self.assertEqual( bf.getFormat(), 'elf' )
            self.assertEqual( bf.getBinType(), 'exe' )
            self.assertEqual( bf.getPlatform(), 'linux' )
            self.assertEqual( bf.getBaseAddr(), 0x400000 )
            self.assertEqual( bf.getByteOrder(), 'little' )

            self.assertIsNotNone( bf.getSectionByName('.text') )
            self.assertFalse( bf.getInfo('elf:prelink') )

            self.assertEqual( bf.getInfo('elf:gnu:abi')[1], (2,6,24) )
            self.assertEqual( bf.getInfo('elf:gnu:buildid'), '35d6cd3799517f5855400489f9bf3a6227200039')
