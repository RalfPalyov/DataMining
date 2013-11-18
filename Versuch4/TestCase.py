import docclass

__author__ = 'janhorak'

'''Testcases'''

ccTest = {'Good': 0, 'Bad': 0}
fcTest = {}
test = docclass.Classifier(fcTest, ccTest)
test.incc('Good')
test.incc('Bad')
test.incc('Good')
test.incc('Good')
test.incc('Good')

print test.catcounts('Good') #should be 4
print test.catcounts('Bad') #should be 1
print test.totalcount() #should be 5
