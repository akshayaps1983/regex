import re

txt = "this is a good place"
x = re.search("^this", txt)
if x:
    print("Found")
else:
    print("Not found")
print("--------------")
import re

txt = "good girl"
x = re.search("girl$", txt)
if x:
    print("Found")
else:
    print("not found")
print("---------------")
import re

txt = "good boy"
x = re.search("^good.*boy$", txt)
if x:
    print("found")
else:
    print("not found")
import re
txt = "good boy"
x = re.search("^good.*boy$", txt)
if x:
    print("found")
else:
    print("not found")
print("---------")

import re
txt ="good boy"
x =re.search("[a-z]", txt)
if x:
    print("Found")
else:
    print("not found")
print("-----------")
import re
txt ="akku"
x =re.search("[^bog]", txt)
if x:
    print("Found")
else:
    print("not found")
print("------------------")
import re
txt ="rashad"
x =re.search("rash?.d",txt)
if x:
    print("Found")
else:
    print("not found")
print("------------------")
import re
txt ="bathery"
x =re.search("bath+.d",txt)
if x:
    print("Found")
else:
    print("not found")