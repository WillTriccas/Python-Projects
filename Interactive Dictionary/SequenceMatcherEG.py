import difflib
from difflib import SequenceMatcher

# SequenceMatcher class consists of 4 parameters (only use first 3 really). The first one is the 'isjunk' parameter. This parameter would be used in the case where you are
#  comparing two blocks of text. In this example we are just comparing words so we can just put 'None' as the first argument. However, if we were, 
# and there was junk there like break lines and spaces then you need to pass a function here that ignores those lines
# 
# SequenceMatcher(isjunk=None, a='', b='', autojunk=True)S

print(SequenceMatcher(None, "rain", "rainn").ratio())


# the ratio method used on the SequenceMatcher class shows how similar the two words you entered are via a numerical value - this can be used with the 
# 
# 'get_close_matches' method!

