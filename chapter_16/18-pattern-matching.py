# Determine whether the given string matches the given pattern of a's and b's.
import unittest

def match(value,pattern,a=None,b=None):
  if (pattern==''):
    return None
  if (pattern[0]=='a'):
    if not(a):
      for a_index in range(1,len(value)):
        if match(pattern=pattern[1:],value=value[a_index:],a=value[:a_index]): 
          return True
      return False
    
    elif ((len(pattern)==1) and (value==a)):
      return True
    elif (value[:len(a)] != a):
        return False

    else:
      return match(pattern=pattern[1:],value=value[len(a):],a=a) 
  elif (pattern[0]=='b'):
    if (not(a) and not(b)):
      return match(pattern=normalize(pattern),value=value,a=a,b=b) 
    if a and not(b):
      for b_index in range(1,len(value)):
        if match(pattern=pattern[1:],value=value[b_index:],a=a,b=value[:b_index]):
          return True
      return False
    elif ((len(pattern)==1) and (value==b)):
      return True
    elif (value[:len(b)] != b):
        return False


def normalize(pattern : str):
  pattern = list(pattern)
  if (pattern[0]=='b'):
    for i in range(len(pattern)):
      if (pattern[i] == 'a'): 
        pattern[i] = 'b'
      else: 
        pattern[i] = 'a'

  return ''.join(pattern)





class Test(unittest.TestCase):
  def test_matches_pattern(self):
    self.assertTrue(match("dogdogturtledogdog", "aabaa"))
    self.assertTrue(match("dogdogturtledogdog", "aba"))
    self.assertFalse(match("dogdogturtledogdg", "aba"))
    self.assertFalse(match("catcatcatbirdbird", "aabb"))
    self.assertTrue(match("buffalobuffalobuffalobuffalo", "aaaa"))
    self.assertFalse(match("buffalobuffalouffalobuffalo", "aaaa"))
    self.assertTrue(match("dogdogturtledog", "aaba"))
    self.assertTrue(match("dogdogturtledogdo", "aba"))
    self.assertTrue(match("catcatbirdbird", "aabb"))
    self.assertTrue(match("dogdogturtledog", "bbab"))






if __name__ == "__main__":
  unittest.main()