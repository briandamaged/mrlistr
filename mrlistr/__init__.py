'''
###################################################
#                    Mr. ListR                    #
#-------------------------------------------------#
# This library implements a few list operations   #
# that appear to be missing from Python 2.6       #
###################################################
'''

def filter_list(func, lizt):
  '''
  This is identical to the filter(...) function, except that
  it operates on the list in place.  This is useful if you need
  to modify an existing list rather than create a new list.
  '''
  index = 0
  while index < len(lizt):
    if func(lizt[index]):
      index += 1
    else:
      del lizt[index]
  return lizt


def map_list(func, lizt):
  '''
  This is identical to the map(...) function, except that
  it operates on the list in place.  This is useful if you need
  to modify an existing list rather than create a new list.
  '''
  index, last = 0, len(lizt)
  while index < last:
    lizt[index] = func(lizt[index])
    index += 1
  return lizt


