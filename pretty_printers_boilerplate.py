class XXXNameofPrinterClassXXX(object):
  """XXXDescription Goes hereXXX"""

  def __init__(self, val):
    self.val = val

  def to_string(self):
    return XXXDo Formatting of self.val hereXXX

def display_hint(self):
  return 'XXXPutHintHereXXX'

import gdb.printing

pp = gdb.printing.RegexpCollectionPrettyPrinter('XXXNameOfDatatypeXXX')
pp.add_printer('XXXNameOfDataTypeXXX', '^XXXNameOfDatatypeXXX$', XXXNameofPrinterClassXXX)
gdb.printing