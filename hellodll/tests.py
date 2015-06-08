import os
import unittest

import vivisect.workspace as v_workspace
import vivisect.lib.binfile as v_binfile
import vivtestfiles.helpers as v_helpers

class HelloWorldTest(unittest.TestCase):

    def test_hellodll_i386(self):

        with v_helpers.testfd('hellodll','hellodll_i386.dll') as fd:
            bf = v_binfile.getBinFile(fd.read())

            self.assertEqual( bf.getLibName(), 'hellodll_i386' )

            self.assertEqual( bf.getBinType(), 'dyn' )
            self.assertIn( (4096,'foo','unkn'), bf.getExports() )
            self.assertIn( (40320, 'kernel32', 'GetTickCount'), bf.getImports() )

            vw = v_workspace.VivWorkspace()
            vw.loadBinFile(bf)

            basemaps = {'hellodll_i386':0x41410000}
            vv = vw.getVivView(basemaps=basemaps)
            self.assertEqual(vv.readMemory(0x41410000,2), b'MZ')

            cpu = vw.getVivCpu()

    def test_hellodll_amd64(self):

        with v_helpers.testfd('hellodll','hellodll_amd64.dll') as fd:
            bf = v_binfile.getBinFile(fd.read())

            self.assertEqual( bf.getLibName(), 'hellodll_amd64' )

            self.assertEqual( bf.getBinType(), 'dyn' )
            self.assertIn( (4096,'foo','unkn'), bf.getExports() )
            self.assertIn( (46360, 'kernel32','QueryPerformanceCounter'), bf.getImports() )

            vw = v_workspace.VivWorkspace()
            vw.loadBinFile(bf)

            basemaps = {'hellodll_amd64':0x41410000}
            vv = vw.getVivView(basemaps=basemaps)
            self.assertEqual(vv.readMemory(0x41410000,2), b'MZ')

            cpu = vw.getVivCpu()
