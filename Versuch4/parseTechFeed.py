import feedparser
import docclass


def stripHTML(h):
  p=''
  s=0
  for c in h:
    if c=='<': s=1
    elif c=='>':
      s=0
      p+=' '
    elif s==0:
      p+=c
  return p

def init():  
        
    categoryA = "tech"
    categoryB = "nontech"
    
    ccTest = {categoryA: 0, categoryB: 0}
    fcTest = {}
    classifier = docclass.Classifier(fcTest, ccTest)
    
    trainTech=['http://rss.chip.de/c/573/f/7439/index.rss',
               'http://feeds.feedburner.com/netzwelt',
               'http://rss1.t-online.de/c/11/53/06/84/11530684.xml',
               'http://www.computerbild.de/rssfeed_2261.xml?node=13',
               'http://www.heise.de/newsticker/heise-top-atom.xml']
    
    trainNonTech=['http://newsfeed.zeit.de/index',
                  'http://newsfeed.zeit.de/wirtschaft/index',
                  'http://www.welt.de/politik/?service=Rss',
                  'http://www.spiegel.de/schlagzeilen/tops/index.rss',
                  'http://www.sueddeutsche.de/app/service/rss/alles/rss.xml'
                  ]
    test=["http://rss.golem.de/rss.php?r=sw&feed=RSS0.91",
              'http://newsfeed.zeit.de/politik/index',  
              'http://www.welt.de/?service=Rss'
               ]
    
    countnews={}
    countnews[categoryA]=0
    countnews[categoryB]=0
    countnews['test']=0
    
    print "--------------------News from trainTech------------------------"
    for feed in trainTech:
        f=feedparser.parse(feed)
        for e in f.entries:
          print '\n---------------------------'
          fulltext=stripHTML(e.title+' '+e.description)
          print fulltext
          countnews[categoryA]+=1
          classifier.train(fulltext, categoryA)
    print "----------------------------------------------------------------"
    print "----------------------------------------------------------------"
    print "----------------------------------------------------------------"
    print classifier.catcounts(categoryA)
    
    print "--------------------News from trainNonTech------------------------"
    for feed in trainNonTech:
        f=feedparser.parse(feed)
        for e in f.entries:
          print '\n---------------------------'
          fulltext=stripHTML(e.title+' '+e.description)
          print fulltext
          countnews[categoryB]+=1
          classifier.train(fulltext, categoryB)
    print "----------------------------------------------------------------"
    print "----------------------------------------------------------------"
    print "----------------------------------------------------------------"
    print classifier.catcounts(categoryB)
    
    print "--------------------News from test------------------------"
    for feed in test:
        f=feedparser.parse(feed)
        for e in f.entries:
          print '\n---------------------------'
          fulltext=stripHTML(e.title+' '+e.description)
          print fulltext
          countnews['test']+=1
          
          probCategoryA = classifier.prob(fulltext, categoryA)
          probCategoryB = classifier.prob(fulltext, categoryB)
          
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
              
          print " - Category: '" + probCategory1 + "' [" + str(probValue1) + "] (Category: '" + probCategory2 + "' [" + str(probValue2) + "])"
    print "----------------------------------------------------------------"
    print "----------------------------------------------------------------"
    print "----------------------------------------------------------------"
    print 'Number of used trainings samples in categorie ' + categoryA,countnews[categoryA]
    print 'Number of used trainings samples in categorie '+ categoryB,countnews[categoryB]
    print 'Number of used test samples',countnews['test']
    print '--'*30