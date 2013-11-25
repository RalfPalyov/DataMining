import feedparser

def getNewsDict():
    
    feedList=['http://feeds.reuters.com/reuters/topNews',
              'http://feeds.reuters.com/reuters/worldNews',
              'http://feeds2.feedburner.com/time/world',
              'http://feeds2.feedburner.com/time/business',
              'http://feeds2.feedburner.com/time/politics',
              'http://rss.cnn.com/rss/edition.rss',
              'http://rss.cnn.com/rss/edition_world.rss',
              'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/business/rss.xml',
              'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/europe/rss.xml',
              'http://www.nytimes.com/services/xml/rss/nyt/World.xml',
              'http://www.nytimes.com/services/xml/rss/nyt/Economy.xml'
              ]
    
    newsDict = {}
    
    for feed in feedList:
        
        newsFeed = feedparser.parse(feed)

        newsTitle = newsFeed['entries'][1]['title']
        newsDescription = newsFeed['entries'][1]['summary']
        
        print newsTitle
        print newsDescription
    
        tmpNewsDict = {newsTitle:newsDescription}
        
        newsDict.update(tmpNewsDict)
        
    return newsDict


