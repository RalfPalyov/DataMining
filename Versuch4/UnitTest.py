__author__ = 'janhorak'
import unittest
import docclass

class JUnitTestCases(unittest.TestCase):

    __cc = {}
    __fc = {}
    __doc1 = u"It was the first time that her parents had left her alone at night, and she hated being alone in the dark. All her begging not to leave her to the monsters had been in vain so she placed the phone beside her bed and turned on the TV. But still, wasn't there a knocking? What if she didn't hear them coming because of the TV, or was it possible that they were already hiding in her closet waiting for the right moment to attack her? She turned off the TV, took a full bottle and approached the closet. Her heart was beating like a drum, and every step took hours. What if there was a monster in it and it was too big for her and would eat her? Wasn't it better to call the neighbors anyway? But monsters always hide from adults and they wouldn't believe her that there was something. Yes, she could feel that there was something, but where? Hadn't there just been a dim light shining through her window and a cracking in the branches of the tree in front of it? She looked at her watch and a shudder went through her: it was almost midnight! Then she had a brilliant idea: She turned on all lights, first in her room then in the stairwell, in her parents' bedroom, in the living room, the kitchen, just everywhere so that the whole house was ablaze. She took her father's baseball racket and waited in front of the big clock in the living room. Would a monster lurking behind the couch be killed by the light? There were ten seconds left! The clock struck midnight and nothing happened. She looked behind the couch and all she found were a few crumbs, the remains of the monster! Satisfied with her work but still leaving the lights on and taking the baseball racket with her she went to bed."

    __doc2 = u"For the most wild, yet most homely narrative which I am about to pen, I neither expect nor solicit belief. Mad indeed would I be to expect it, in a case where my very senses reject their own evidence. Yet, mad am I not - and very surely do I not dream. But to-morrow I die, and to-day I would unburthen my soul. My immediate purpose is to place before the world, plainly, succinctly, and without comment, a series of mere household events. In their consequences, these events have terrified - have tortured - have destroyed me. Yet I will not attempt to expound them. To me, they have presented little but Horror - to many they will seem less terrible than barroques. Hereafter, perhaps, some intellect may be found which will reduce my phantasm to the common-place - some intellect more calm, more logical, and far less excitable than my own, which will perceive, in the circumstances I detail with awe, nothing more than an ordinary succession of very natural causes and effects."
    __doc3 = u"A child was standing on a street-corner. He leaned with one shoulder against a high board-fence and swayed the other to and fro, the while kicking carelessly at the gravel. \
    Sunshine beat upon the cobbles, and a lazy summer wind raised yellow dust which trailed in clouds down the avenue. Clattering trucks moved with indistinctness through it. The child stood dreamily gazing. \
    After a time, a little dark-brown dog came trotting with an intent air down the sidewalk. A short rope was dragging from his neck. Occasionally he trod upon the end of it and stumbled. \
    He stopped opposite the child, and the two regarded each other. The dog hesitated for a moment, but presently he made some little advances with his tail. The child put out his hand and called him. In an apologetic manner the dog came close, and the two had an interchange of friendly pattings and waggles. The dog became more enthusiastic with each moment of the interview, until with his gleeful caperings he threatened to overturn the child. Whereupon the child lifted his hand and struck the dog a blow upon the head."
    __doc4 = u"During the whole of a dull, dark, and soundless day in the autumn of the year, when the clouds hung oppressively low in the heavens, I had been passing alone, on horseback, through a singularly dreary tract of country; and at length found myself, as the shades of the evening drew on, within view of the melancholy House of Usher. I know not how it was--but, with the first glimpse of the building, a sense of insufferable gloom pervaded my spirit. I say insufferable; for the feeling was unrelieved by any of that half-pleasurable, because poetic, sentiment, with which the mind usually receives even the sternest natural images of the desolate or terrible."


    def setUp(self):
        self.__cc = {'Good': 0, 'Bad': 0}
        self.__fc = {
          "night":      {"Bad": 1},
          "hated":      {"Bad": 1},
          "dark":       {"Bad": 1},
          "alone":      {"Bad": 1},
          "monsters":   {"Bad": 1},
          "tv":         {"Bad": 1},
          "light":      {"Good": 1},
          "bed":        {"Good": 1},
          "parents":    {"Good": 1},
          "bedroom":    {"Good": 1},
          }

    def cleanUp(self):
        del self.__fc
        del self.__cc

    def test_setUp(self):
        self.assertIsNotNone(self.__cc)
        self.assertIsNotNone(self.__fc)


    def test_simpleTests(self):
        self.setUp()
        self.test_setUp()
        test = docclass.Classifier(self.__fc, self.__cc)
        test.incc('Good')
        test.incc('Bad')
        test.incc('Good')
        test.incc('Good')
        test.incc('Good')
        test.incf("Apple", "Bad")
        test.incf("Orange", "Bad")
        test.incf("Banana", "Good")
        self.assertTrue(test.catcounts('Bad') is 1)
        self.assertTrue(test.catcounts('Good') is 4)

        test.train(self.__doc1, "Bad")
        self.assertAlmostEqual(test.weightedprob('hated', 'Bad'), 0.83333333)
        self.assertTrue(test.catcounts('Good') is 4)
        self.assertTrue(test.catcounts('Bad') is 2)
        self.assertTrue(self.__fc["Apple"]["Bad"] is 1)
        self.assertTrue(self.__fc["monsters"]["Bad"] is 2)


        self.cleanUp()
        del test

    def test_complexTests(self):
        self.setUp()
        self.test_setUp()
        test = docclass.Classifier(self.__fc, self.__cc)
        self.assertTrue(test.catcounts("cat") is 0)
        self.assertTrue(test.fcount("none", "cat") is 0)
        self.assertFalse(test.incc('cat'))
        self.assertTrue(test.catcounts("cat") is 0)
        self.assertFalse(test.incf('none', 'cat'))
        self.assertTrue(test.fcount("none", "cat") is 0)
        test.train(self.__doc1, 'Good')
        test.train(self.__doc2, 'Good')
        test.train(self.__doc3, 'Bad')
        self.assertIsNotNone(test.prob(self.__doc4, 'Good'))
        self.assertIsNotNone(test.prob(self.__doc4, 'Bad'))

        self.cleanUp()
        del test


suite = unittest.TestLoader().loadTestsFromTestCase(JUnitTestCases)
unittest.TextTestRunner(verbosity=2).run(suite)