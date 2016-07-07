import functools
import random
import re
import unicodedata

def benisify(s):
    return functools.reduce(lambda acc, f: f(acc), [
        lambda s: s.lower(),
        lambda s: unicodedata.normalize('NFKD', s),
        lambda s: s.replace('x', 'cks'),
        lambda s: re.sub(r'ing','in', s),
        lambda s: re.sub(r'you', 'u', s),
        lambda s: re.sub(r'oo', 'u', s),
        lambda s: re.sub(r'ck\b', 'g', s),
        lambda s: re.sub(r'ck', 'gg', s),
        lambda s: re.sub(r'\bthe\b', 'da', s),
        lambda s: re.sub(r'(t+)', lambda x: 'd' * len(x.group(1)), s),
        lambda s: s.replace('p', 'b'),
        lambda s: re.sub(r'\bc', 'g', s),
        lambda s: re.sub(r'\bis\b', 'are', s),
        lambda s: re.sub(r'c+(?![eiy])', 'g', s),
        lambda s: re.sub(r'know', 'no', s),
        lambda s: re.sub(r'kn', 'n', s),
        lambda s: re.sub(r'[qk]', 'g', s),
        #lambda s: re.sub(r'([?!.]|$)+', lambda x: (x.group(0) * random.randint(2, 5)) + " " + "".join((":" * random.randint(1, 2)) + ("D" * random.randint(1, 4)) for _ in range(random.randint(2, 5))), s),
    ], s)
