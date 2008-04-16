#!/usr/bin/python
# -*- coding: utf-8 -*-

class Word:
  "Represents a word in the Dokpro dictionary."
  
  def __init__(self, word):
    self.__word = word
    self.__articles = []
    
  def __str__(self):
    return self.__word
    
  def add_article(self, article):
    self.__articles.append(article)
  
  def articles(self):
    return self.__articles
