#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib, os, sys
sys.path.append("./vendor")
sys.path.append("./lib")
from BeautifulSoup import BeautifulSoup
from word import Word

class IncorrectLanguageError(Exception): pass

class Dokpro:
  def __init__(self, lang):
    if lang != "bokmaal" and lang != "nynorsk":
      raise IncorrectLanguageError, "Bruk enten nynorsk eller bokmaal"
    
    self.__wordlist = []
    self.__url = "http://www.dokpro.uio.no/perl/ordboksoek/ordbok.cgi?OPP=TERM&ordbok="\
                  + lang + "&alfabet=n&renset=j"

  def search(self, term):
    """VINK: Bruk '%' for null eller flere vilkårlige tegn og '_' for ett slikt:
    bok% = alt som starter med 'bok'. (Du får maksimalt 30 av tilslagene.)"""
    
    self.__wordlist = [] # first clear the old results
    self.parse_data(urllib.urlopen(self.__url.replace('TERM', term)).read())
  
  def parse_data(self, data):
    table = BeautifulSoup(data).find('table', border="1")
    
    try:
      for row in table('tr', valign="top"):
        first_cell = row.td.b.contents[0].strip()
        if first_cell != "&nbsp;":
          self.__wordlist.append(Word(first_cell))
        
        self.__wordlist[-1].add_article(self.__parse_article_from_element(row.td.nextSibling))
    except AttributeError:
      pass
    
  def size(self):
    return len(self.__wordlist)
    
  def words(self):
    return self.__wordlist
  
  def __parse_article_from_element(self, element):
    return "".join(map(str, element.contents[1:])).strip().replace('\n', '') \
      .replace('<i>', '_').replace('</i>', '_')
    