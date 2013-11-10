from pandas.compat import scipy

import math
import operator

def cosinusSim(vec1, vec2):
    counter = reduce( operator.add, map( operator.mul, vec1, vec2))
    denominator1 = math.sqrt(sum([n**2 for n in vec1]))
    denominator2 = math.sqrt(sum(n**2 for n in vec2))
    denominator = denominator1 * denominator2
    return counter / denominator


def isAverageFree(vec1, vec2, amountDecimalPlaces):
    cos = cosinusSim(vec1, vec2)
    pearson = scipy.stats.pearsonr(vec1, vec2)
    cosString = repr(cos)
    pearString = repr(pearson)
    if cosString[:amountDecimalPlaces] == pearString[:amountDecimalPlaces]:
        return True
    return False