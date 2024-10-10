import math
import re
from collections import Counter


def get_cosine(doc1, doc2):
    vec1 = text_to_vector(doc1)
    vec2 = text_to_vector(doc2)

    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(doc):
    return Counter(doc)




# document1 = "This is a foo bar sentence ."
# document2 = "This sentence is similar to a foo bar sentence ."
# cosine = get_cosine(document1, document2)
# print("Cosine:", cosine)