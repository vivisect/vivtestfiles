import os

def testfile(*path):
    dirname = os.path.dirname(__file__)
    return os.path.join( *(dirname,) + path )

def testfd(*path):
    return open( testfile(*path), 'rb' )

