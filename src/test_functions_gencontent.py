import unittest
from functions_gencontent import *

class TestFunctions(unittest.TestCase):

    def test_extract_title1(self):
      text = ''' Esto es texto
## Esto no es el titulo
# Esto es el título
Más texto
'''
      res1 = extract_title(text)
      res2 = "Esto es el título"
      self.assertEqual(res1, res2)

    def test_extract_title2(self):
      text = ''' Aquí no hay título. Esto es texto
## Esto no es el titulo
Más texto
'''
      self.assertRaises(Exception, extract_title, text)
        
if __name__ == "__main__":
    unittest.main()
