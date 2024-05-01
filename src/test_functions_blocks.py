import unittest
from functions_blocks import *

class TestFunctions(unittest.TestCase):

    def test_markdown_to_blocks(self):
        text = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item'''
        res1 = markdown_to_blocks (text)
        res2 = ['# This is a heading',
                'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
'''* This is a list item
* This is another list item'''               
        ]
        self.assertEqual(res1, res2)

    def test_markdown_to_blocks2(self):
        text = '''
# The Unparalleled Majesty of "The Lord of the Rings"

[Back Home](/)

![LOTR image artistmonkeys](/images/rivendell.png)

> "I cordially dislike allegory in all its manifestations, and always have done so since I grew old and wary enough to detect its presence.       
        '''
        res1 = markdown_to_blocks (text)
        res2 = ['# The Unparalleled Majesty of "The Lord of the Rings"',
                '[Back Home](/)',
                '![LOTR image artistmonkeys](/images/rivendell.png)',
                '> "I cordially dislike allegory in all its manifestations, and always have done so since I grew old and wary enough to detect its presence.'            
        ]
        self.assertEqual(res1, res2)


    def test_block_to_block_type(self):
        test_cases = [
          ('Normal paragraph', block_type_paragraph),
          ('# Heading 1', block_type_heading),
          ('###### Heading 6', block_type_heading),
          ('####### No heading, just paragraph', block_type_paragraph),
          ('###No heading, just paragraph', block_type_paragraph),
          ('```Code block\n```', block_type_code),
          ('>Quote block', block_type_quote),
          ('* Unordered list', block_type_ulist),
          ('- Unordered list', block_type_ulist),
          ('*No list, just paragraph', block_type_paragraph),
          ('1. ', block_type_olist),
          ('23. ', block_type_paragraph),
          ('1.Just paragraph', block_type_paragraph),
          ('12 Just paragrapgh', block_type_paragraph),
        ]                     
        res1 = []
        res2 = []
        for case in test_cases:
          type = block_to_block_type(case[0])
          res1.append(type)
          res2.append(case[1])
          if type != case[1]:
            print (f"BLOQUE: {case[0]}")
            print (f"   ERROR - RES: {case[1]} CALC: {type}")
        self.assertEqual(res1, res2)                

    def test_block_to_block_type2(self):
        test_cases = [
                ('# The Unparalleled Majesty of "The Lord of the Rings"', block_type_heading),
                ('[Back Home](/)', block_type_paragraph),
                ('![LOTR image artistmonkeys](/images/rivendell.png)', block_type_paragraph),
                ('> "I cordially dislike allegory in all its manifestations, and always have done so since I grew old and wary enough to detect its presence.', block_type_quote)         
        ]                        
        res1 = []
        res2 = []
        for case in test_cases:
          type = block_to_block_type(case[0])
          res1.append(type)
          res2.append(case[1])
          if type != case[1]:
            print (f"BLOQUE: {case[0]}")
            print (f"   ERROR - RES: {case[1]} CALC: {type}")
        self.assertEqual(res1, res2)        

        

if __name__ == "__main__":
    unittest.main()
