from nose.tools import *
#from .context import sample

import aforgizmo

def setup(self):
    print 'SETUP!'

def teardown():
    print 'TEARDOWN!'

def test_basic():
    print 'I RAN!'
