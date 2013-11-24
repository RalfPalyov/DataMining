# -*- coding: utf-8 -*-

import docclass

def init():
    
    categoryA = "Good"
    categoryB = "Bad"
    
    ccTest = {categoryA: 0, categoryB: 0}
    fcTest = {}
    
    classifier = docclass.Classifier(fcTest, ccTest)
    
    catAStrings =[u"nobody owns the water", u"the quick rabbit jumps fences",
                  u"the quick brown fox jumps", u"next meeting is at night",
                  u"brown fox sales pharamceuticals for money"]    
    
    catBStrings = [u"buy pharmaceuticals now", u"make quick money at the online casino",
                  u"meeting with your superstar", u"money like water",
                  u"quick money in rabbit casino"]
    
    for item in catAStrings:
        classifier.train(item, categoryA)
    
    for item in catBStrings:
        classifier.train(item, categoryB)

    testText = u"the money jumps"
    
    probCategoryA = classifier.prob(testText, categoryA)
    probCategoryB = classifier.prob(testText, categoryB)
    
    if probCategoryA > probCategoryB:
         probCategory1 = categoryA
         probValue1 = probCategoryA
         probCategory2 = categoryB
         probValue2 = probCategoryB
    else:
        probCategory1 = categoryB
        probValue1 = probCategoryB
        probCategory2 = categoryA
        probValue2 = probCategoryA
    
    print "items in category '" + categoryA + "': " + str(classifier.catcounts(categoryA))
    print "items in category '" + categoryB + "': " + str(classifier.catcounts(categoryB))        
    print testText + " - Category: '" + probCategory1 + "' [" + str(probValue1) + "] (Category: '" + probCategory2 + "' [" + str(probValue2) + "])"

init()