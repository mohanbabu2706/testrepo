from itertools import groupby
lines = '''
This is the
first paragraph.


This is the second.
'''.splitlines()
#use itertools.groupby and bool to return groups of
#consecutive lines that either hae content or don't
for has_chars, frags in groupby(lines,bool):
    if has_chars:
        print(' '.join(frags))
#PRINTS
#This is the first paragraph.
#This is the second.
