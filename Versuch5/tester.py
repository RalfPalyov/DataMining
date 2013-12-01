import newsfeatures

def init():
    
    print "Gestartet. Sammle Feeds...\n\n"
    
    words = newsfeatures.getarticlewords()
    allwords = words['allwords']
    articlewords = words['articlewords']
    articletitles = words['articletitles']
    
    transpObject = newsfeatures.makematrix(allwords,articlewords )
    
    A = transpObject.getArticleWordMat()
    wordvec = transpObject.getWordVector()
    
    H, W = newsfeatures.nnmf(A, 5, 10)

    newsfeatures.showfeatures(W, H, articletitles, wordvec)
    
init()
