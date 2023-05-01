

import random
import itertools

def random_number() :

    answerlist=[''.join(x) for x in list(itertools.permutations('0123456789',4))]
    answer = random.choice(answerlist)
    return (answer)
