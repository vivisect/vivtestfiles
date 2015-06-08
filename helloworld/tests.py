import os
import unittest

import vivisect.workspace as v_workspace
import vivisect.lib.binfile as v_binfile
import vivtestfiles.helpers as v_helpers

class HelloWorldTest(unittest.TestCase):

    def test_helloworld_i386_exe(self):
        with v_helpers.testfd('helloworld','hello_i386.exe') as fd:
            bf = v_binfile.getBinFile(fd.read())

            self.assertEqual( bf.getArch(), 'i386' )
            self.assertEqual( bf.getFormat(), 'pe' )
            self.assertEqual( bf.getPlatform(), 'windows' )
            self.assertEqual( bf.getByteOrder(), 'little' )

            self.assertEqual( bf.getBaseAddr(), 0x400000 )
            self.assertIsNotNone( bf.getSectionByName('.text') )

    def test_helloworld_amd64_exe(self):
        with v_helpers.testfd('helloworld','hello_amd64.exe') as fd:
            bf = v_binfile.getBinFile(fd.read())

            self.assertEqual( bf.getArch(), 'amd64' )
            self.assertEqual( bf.getFormat(), 'pe' )
            self.assertEqual( bf.getPlatform(), 'windows' )
            self.assertEqual( bf.getByteOrder(), 'little' )

            self.assertEqual( bf.getBaseAddr(), 0x140000000 )
            self.assertIsNotNone( bf.getSectionByName('.text') )

    def test_helloworld_vw_i386(self):
        with v_helpers.testfd('helloworld','hello_i386.exe') as fd:
            bf = v_binfile.getBinFile(fd.read())

            fh = bf.getMd5()

            vw = v_workspace.VivWorkspace()
            md5 = vw.loadBinFile( bf )

            self.assertEqual( vw.getVivConfig('arch'), 'i386' )
            self.assertEqual( len(vw.getNodesByProp('fileaddr:entry',valu='func')), 1)

            view = vw.getVivView()
            self.assertEqual( view.readMemory( bf.getBaseAddr(), 2 ), b'MZ' )
            self.assertEqual( view.addrToFileAddr( bf.getBaseAddr() + 20 ), (fh,20) )

    def test_helloworld_vw_amd64(self):
        with v_helpers.testfd('helloworld','hello_amd64.exe') as fd:
            bf = v_binfile.getBinFile(fd.read())

            fh = bf.getMd5()

            vw = v_workspace.VivWorkspace()
            vw.loadBinFile( bf )

            self.assertEqual( vw.getVivConfig('arch'), 'amd64' )
            self.assertEqual( len(vw.getNodesByProp('fileaddr:entry',valu='func')), 159)

            view = vw.getVivView()
            self.assertEqual( view.readMemory( bf.getBaseAddr(), 2 ), b'MZ' )
            self.assertEqual( view.addrToFileAddr( bf.getBaseAddr() + 20 ), (fh,20) )

    def test_helloworld_analyze_i386(self):
        with v_helpers.testfd('helloworld','hello_i386.exe') as fd:
            vw = v_workspace.VivWorkspace()
            vw.loadBinFd(fd)
            vw.runVivAnalyze()

    def test_helloworld_analyze_amd64(self):
        with v_helpers.testfd('helloworld','hello_amd64.exe') as fd:
            vw = v_workspace.VivWorkspace()
            vw.loadBinFd(fd)
            vw.runVivAnalyze()
