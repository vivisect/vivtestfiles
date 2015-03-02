import os
import unittest

import vivisect.workspace as v_workspace
import vivisect.lib.bexfile as v_bexfile
import vivtestfiles.helpers as v_helpers

class RedistDbghelpTest(unittest.TestCase):

    def test_redist_dbghelp_i386(self):

        with v_helpers.testfd('redist','dbghelp','dbghelp_i386.dll') as fd:
            bex = v_bexfile.getBexFile(fd)
            self.assertEqual( bex.arch(), 'i386' )
            self.assertEqual( bex.bintype(), 'dyn' )

            vw = v_workspace.VivWorkspace()
            vw.loadBexFile( bex )

            self.assertEqual( len(vw.getNodesByProp('fileaddr:reloc')), 10666)

            # FIXME use these for VS_VERSIONINFO validation

    def test_redist_dbghelp_amd64(self):

        with v_helpers.testfd('redist','dbghelp','dbghelp_amd64.dll') as fd:
            bex = v_bexfile.getBexFile(fd)

            self.assertEqual( bex.arch(), 'amd64' )
            self.assertEqual( bex.bintype(), 'dyn' )

            vw = v_workspace.VivWorkspace()
            vw.loadBexFile( bex )

            self.assertEqual( len(vw.getNodesByProp('fileaddr:reloc')), 4235)

            # FIXME use these for VS_VERSIONINFO validation

