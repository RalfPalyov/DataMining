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
                encodedWord = u"" + str(string.lower(word).encode("utf-8"))
                result[encodedWord] = 1
    
    return result

def init():
    text = u"Thomas Felder, zwanzig Jahre jünger als Schwindt, war ein hochgewachsener, schwarzhaariger Mann, mit kantigem Gesicht und dunkelbraunen Augen. Im Gegensatz zu seinem Vorgesetzten Schwindt, im leichten, musterlos hellgrauen Anzug, trug er einen marineblauen, korrekt geknöpften Zweireiher. \
„Dann wollen wir mal ...“, sagte Schwindt, nachdem er seinen Porsche ausgemacht hatte. Schwindts Direktoren-Kollegen in Deutschland standen auf schwarz lackierte Mercedeswagen oder BMW; Schwindt war die auffallende Ausnahme: ein Porsche! – und dann auch noch weiß? \
Felder antwortete forsch mit „Jawohl!“ und „Es ist an der Zeit!“ \
„Ich bewundere immer wieder Ihren Eifer“, bemerkte Schwindt ironisch."

    test = getwords(text)
    print test
        
