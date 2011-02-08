import unittest
from fetchapp.tests import FetchAppTest
try:
    import config
except:
    print "Could not find config.py. Please review config.py.sample."
    exit()

if __name__ == '__main__':
    unittest.main()
