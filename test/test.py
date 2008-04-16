#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest, sys
sys.path.append("./lib")
from dokpro import *

class TestWord(unittest.TestCase):
  def test_str(self):
    word = Word("Word")
    self.assertEqual("Word", word.__str__())

class TestDokpro(unittest.TestCase):
  def setUp(self):
    self.dokpro = Dokpro("bokmaal")
    
  def test_size(self):
    self.assertEqual(0, self.dokpro.size())
  
  def test_words(self):
    self.assertEqual([], self.dokpro.words())
  
  def test_parse_data(self):
    data=open('./test/html/staut.html', 'r').read()
    self.dokpro.parse_data(data)
    self.assertEqual(1, self.dokpro.size())
    self.assertEqual(3, len(self.dokpro.words()[0].articles()))
    
    for article in self.dokpro.words()[0].articles():
      print article

if __name__ == '__main__':
  unittest.main()
