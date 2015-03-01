import os
import unittest

import vivisect.workspace as v_workspace
import vivisect.lib.bexfile as v_bexfile
import vivtestfiles.helpers as v_helpers

class HelloWorldTest(unittest.TestCase):

    def test_helloworld_i386_exe(self):
        with v_helpers.testfd('helloworld','hello_i386.exe') as fd:
            bex = v_bexfile.getBexFile(fd)

            self.assertEqual( bex.arch(), 'i386' )
            self.assertEqual( bex.format(), 'pe' )
            self.assertEqual( bex.platform(), 'windows' )
            self.assertEqual( bex.byteorder(), 'little' )

            self.assertEqual( bex.baseaddr(), 0x400000 )
            self.assertIsNotNone( bex.section('.text') )

    def test_helloworld_amd64_exe(self):
        with v_helpers.testfd('helloworld','hello_amd64.exe') as fd:
            bex = v_bexfile.getBexFile(fd)

            self.assertEqual( bex.arch(), 'amd64' )
            self.assertEqual( bex.format(), 'pe' )
            self.assertEqual( bex.platform(), 'windows' )
            self.assertEqual( bex.byteorder(), 'little' )

            self.assertEqual( bex.baseaddr(), 0x140000000 )
            self.assertIsNotNone( bex.section('.text') )

    def test_helloworld_vw_i386(self):
        with v_helpers.testfd('helloworld','hello_i386.exe') as fd:
            bex = v_bexfile.getBexFile(fd)

            vw = v_workspace.VivWorkspace()
            md5 = vw.loadBexFile( bex )

            self.assertEqual( vw.getVivConfig('arch'), 'i386' )
            self.assertEqual( len(vw.getNodesByProp('fileaddr:entry',valu='func')), 1)

            view = vw.getVivView()
            self.assertEqual( view.readMemory( bex.baseaddr(), 2 ), b'MZ' )

    def test_helloworld_vw_amd64(self):
        with v_helpers.testfd('helloworld','hello_amd64.exe') as fd:
            bex = v_bexfile.getBexFile(fd)

            vw = v_workspace.VivWorkspace()
            vw.loadBexFile( bex )

            self.assertEqual( vw.getVivConfig('arch'), 'amd64' )
            self.assertEqual( len(vw.getNodesByProp('fileaddr:entry',valu='func')), 159)

            view = vw.getVivView()
            self.assertEqual( view.readMemory( bex.baseaddr(), 2 ), b'MZ' )
