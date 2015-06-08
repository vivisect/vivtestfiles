import os
import unittest

import vivisect.workspace as v_workspace
import vivisect.lib.binfile as v_binfile
import vivtestfiles.helpers as v_helpers

class RedistDbghelpTest(unittest.TestCase):

    @unittest.skip('FIXME')
    def test_redist_dbghelp_i386(self):

        with v_helpers.testfd('redist','dbghelp','dbghelp_i386.dll') as fd:
            bf = v_binfile.getBinFile(fd.read())
            self.assertEqual( bf.arch(), 'i386' )
            self.assertEqual( bf.bintype(), 'dyn' )

            vw = v_workspace.VivWorkspace()
            vw.loadBinFile( bf )

            self.assertEqual( len(vw.getNodesByProp('fileaddr:reloc')), 10666)

            # FIXME use these for VS_VERSIONINFO validation

    @unittest.skip('FIXME')
    def test_redist_dbghelp_amd64(self):

        with v_helpers.testfd('redist','dbghelp','dbghelp_amd64.dll') as fd:
            bf = v_binfile.getBinFile(fd.read())

            self.assertEqual( bf.arch(), 'amd64' )
            self.assertEqual( bf.bintype(), 'dyn' )

            vw = v_workspace.VivWorkspace()
            vw.loadBinFile( bf )

            self.assertEqual( len(vw.getNodesByProp('fileaddr:reloc')), 4235)

            # FIXME use these for VS_VERSIONINFO validation

