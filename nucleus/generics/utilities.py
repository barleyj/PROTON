__author__ = "Pruthvi Kumar, pruthvikumar.123@gmail.com"
__copyright__ = "Copyright (C) 2018 Pruthvi Kumar | http://www.apricity.co.in"
__license__ = "Public Domain"
__version__ = "1.0"

import copy

class MyUtilities(object):

    def __init__(self):
        super(MyUtilities, self).__init__()

    def validateListOfDictsConsistency(self, listOfDicts):
        """
        Validate id all the key value pairs in a list of dictionaries contain same keys.
        eg.  [{'category':2012,'column-1':10},{'category':2013,'column-1':11}] is valid
             [{'category':2012,'column-1':10},{'category':2013,'column-2':11}] is in-valid
        :param listOfDicts: A list of dictionaries
        :return: A boolean indicating consistency
        """
        c_rd = copy.deepcopy(listOfDicts)
        return any(reduce(lambda i1, i2: i1 if i1 == i2 else [], map(lambda rd: list(rd.keys()), c_rd)))
