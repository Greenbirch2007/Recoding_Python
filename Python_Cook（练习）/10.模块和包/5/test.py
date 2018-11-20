#
import sys

sys.path.extend(['foo-package','bar-package','my-package'])
# import spam.blah
# import spam.grok
#
# import spam
# print(spam.__path__)



import spam.custom
print(spam)


import spam

import imp
imp.reload(spam)