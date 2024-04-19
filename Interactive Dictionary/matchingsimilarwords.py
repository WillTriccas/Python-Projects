import json

data = json.load(open("data.json"))

word = input("please type word here: ")

import difflib
from difflib import get_close_matches

# get_close_matches(word, possibilities, n=3, cutoff=0.6)
# Use SequenceMatcher to return list of the best "good enough" matches.

# word is a sequence for which close matches are desired (typically a string).

# possibilities is a list of sequences against which to match word (typically a list of strings).

# Optional arg n (default 3) is the maximum number of close matches to
# return.  n must be > 0.

# Optional arg cutoff (default 0.6) is a float in [0, 1].  Possibilities
# that don't score at least that similar to word are ignored.

print(get_close_matches(word, data.keys()))