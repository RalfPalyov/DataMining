# -*- coding: utf-8 -*-
'''
Created on 18.11.2013

@author: am095
'''
import string
import re


def getwords(doc):
    '''
    Transform a document to a dictionary. Split it at each word.
    All words will be transformed into lowercase.
    Caution: Words with a letter count greater than 19 or lower than 4 will be ignored.
    
    Parameter:
    doc: String, a document (Text)
    
    Return:
    Dictionary with words as keys and 1 as values
    '''

    result = {}    
    
    words = re.split('([,.;:-\?!“"\'\)\]]+\s)|(\s[\[\(„"\']+)|(\s)', doc)

    for word in words:
        if type(word) == unicode:
            if len(word) < 20 and len(word) > 3:
                encodedWord = unicode(string.lower(word))
                result[encodedWord] = 1
    return result
