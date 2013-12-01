import newsfeatures

def init():
    
    words = newsfeatures.getarticlewords()
    allwords = words['allwords']
    articlewords = words['articlewords']
    articletitles = words['articletitles']
    
    transpObject = newsfeatures.makematrix(allwords,articlewords )
    A = transpObject.getArticleWordMat()
    wordvec = transpObject.getWordVector()
    
    print A
    
    W, H = newsfeatures.nnmf(A, 5, 10)
    
    print W
    print H
    
    newsfeatures.showfeatures(W, H, articletitles, wordvec)
    
init()
