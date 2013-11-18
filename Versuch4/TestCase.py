import docclass

__author__ = 'janhorak'

'''Testcases'''

doc = u"It was the first time that her parents had left her alone at night, and she hated being alone in the dark. All her begging not to leave her to the monsters had been in vain so she placed the phone beside her bed and turned on the TV. But still, wasn't there a knocking? What if she didn't hear them coming because of the TV, or was it possible that they were already hiding in her closet waiting for the right moment to attack her? She turned off the TV, took a full bottle and approached the closet. Her heart was beating like a drum, and every step took hours. What if there was a monster in it and it was too big for her and would eat her? Wasn't it better to call the neighbors anyway? But monsters always hide from adults and they wouldn't believe her that there was something. Yes, she could feel that there was something, but where? Hadn't there just been a dim light shining through her window and a cracking in the branches of the tree in front of it? She looked at her watch and a shudder went through her: it was almost midnight! Then she had a brilliant idea: She turned on all lights, first in her room then in the stairwell, in her parents' bedroom, in the living room, the kitchen, just everywhere so that the whole house was ablaze. She took her father's baseball racket and waited in front of the big clock in the living room. Would a monster lurking behind the couch be killed by the light? There were ten seconds left! The clock struck midnight and nothing happened. She looked behind the couch and all she found were a few crumbs, the remains of the monster! Satisfied with her work but still leaving the lights on and taking the baseball racket with her she went to bed."

# simple tests#
ccTest = {'Good': 0, 'Bad': 0}
fcTest = {}
test = docclass.Classifier(fcTest, ccTest)
test.incc('Good')
test.incc('Bad')
test.incc('Good')
test.incc('Good')
test.incc('Good')

# simple test results #
print test.catcounts('Good') #should be 4
print test.catcounts('Bad') #should be 1
print test.totalcount() #should be 5


