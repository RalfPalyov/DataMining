import newsfeatures

def init():
    
    words = newsfeatures.getarticlewords()
    allwords = words['allwords']
    articlewords = words['articlewords']
    articletitles = words['articletitles']
    
    transpObject = newsfeatures.makematrix(allwords,articlewords )
    A = transpObject.getArticleWordMat()
    wordvec = transpObject.getWordVector()
    
    W, H = newsfeatures.nnmf(A, 10, 10)

    newsfeatures.showfeatures(W, H, articletitles, wordvec)
    
init()
