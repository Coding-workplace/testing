import re
re.findall(r".", "a\nb")      # ['a', 'b']  (newline not matched)
re.findall(r".", "ab!")       # ['a','b','!']
re.findall(r"^Hello", "Hello world")            # ['Hello']
re.findall(r"^world", "Hello\nworld", re.M)     # ['world'] (with MULTILINE)
re.findall(r"end$", "the end")                  # ['end']
re.findall(r"end$", "end\nmore", re.M)          # ['end'] (matches line ending)
re.findall(r"a*b", "b ab aab aaab")             # ['b','ab','aab','aaab']
# matches zero or more 'a' followed by 'b'
re.findall(r"a+b", "b ab aab")                  # ['ab','aab']
# requires at least one 'a' before 'b'
re.findall(r"colou?r", "color colour colouur")   # ['color','colour']
# 'u' is optional
s = "<p>one</p><p>two</p>"
re.findall(r"<p>.*</p>", s)                     # greedy: ['<p>one</p><p>two</p>']
re.findall(r"<p>.*?</p>", s)                    # non-greedy: ['<p>one</p>','<p>two</p>']
# Similarly for +? and ??:
re.findall(r"a.+?b", "aab aaatb ab")            # minimal matches between a and b ['aab', 'aaatb']
re.findall(r"a{1,4}a", "aaaaaaaa")  # ['aaaaa', 'aaa']
re.findall(r"a{1,4}?a", "aaaaaaaa")  #['aa', 'aa', 'aa', 'aa']
re.findall(r"\.", "1.2 3")                      # ['.']  # literal dot
re.findall(r"\\", r"back\slash")                # ['\\'] # literal backslash
re.findall(r"[abc]", "apple banana cat")        # ['a','a','a','c','a']
re.findall(r"[^0-9]+", "a1b2")                  # ['a','b']  # non-digits
re.findall(r"cat|dog", "cat dog catfish")       # ['cat','dog','cat']
# alternation picks leftmost branch at each match
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "2025-10-30")
m.groups()                                      # ('2025','10','30')
# groups accessible by index in match object
# (?i) case-insensitive
re.findall(r"(?i)python", "PYTHON PyThOn")      # ['PYTHON','PyThOn']
# (?m) multiline makes ^/$ match line boundaries
re.findall(r"(?m)^start", "start\nother\nstart")# ['start','start']
# Non-capturing group
m = re.search(r"(?:ab){2}", "abab ab")
m.groups() # ()
m[0] # 'abab'
# Named capturing group
m = re.search(r"(?P<year>\d{4})-(?P<mo>\d{2})-(?P<day>\d{2})", "2025-10-30")
m.group('year'), m.group('mo')                   # ('2025','10')
re.findall(r"(?P<x>\w+)\s+(?P=x)", "yes yes no no maybe maybe")  
# ['yes','no','maybe']  # finds repeated word pairs
re.findall(r"ab(?#this is a comment)c", "abc abc")  # ['abc','abc']
# comment has no runtime effect
# Positive Lookahead
re.findall(r"\w+(?=\s=)", "a = b c = d")        # ['a','c']  # word followed by ' ='
# the '=’ is not consumed
# Negative Lookahead
re.findall(r"\w+(?!\s=)", "a = b c = d e")      # ['b','d','e']  # words not followed by ' ='
# "(?<=...)" — positive lookbehind (must be fixed-width)
re.findall(r"(?<=\$)\d+", "cost $30 and $5")    # ['30','5']  # digits preceded by $
re.findall(r"(?<!\$)\d+", "30 $40 50")          # ['30', '0', '50']  # numbers not preceded by $
# conditional based on a group having matched.
pattern = re.compile(r'(?P<g>A)?(?(g)B|C)')

tests = ['AB', 'C', 'B', 'A', 'AC']
for s in tests:
    m = pattern.fullmatch(s)
    print(s, '->', bool(m), 'match:', m.group(0) if m else None)
# AB -> True match: AB
# C -> True match: C
# B -> False match: None
# A -> False match: None
# AC -> False match: None

# "\number" — backreference by group number
re.findall(r"(\w)\1", "book apple cool")        # ['o','o']  # double letters matched by \1
re.findall(r"\AHello", "Hello\nHello", re.M)    # ['Hello']  # only start of entire string
re.findall(r"end\Z", "end\n")                   # ['end']  # matches end of string even if final newline
re.findall(r"\bcat\b", "concatenate cat scatter")  # ['cat']  # matches whole word only
re.findall(r"\Bcat\B", "concatenate")           # ['cat']  # 'cat' inside a word
re.findall(r"\d+", "ID 12345 and ٦٧٨")          # ['12345','٦٧٨']  # Unicode digits included
re.findall(r"\D+", "123abc456")                 # ['abc']  # sequences of non-digits
re.split(r"\s+", "a\tb\nc  d")                  # ['a','b','c','d']
re.findall(r"\S+", "a b  c\n")                  # ['a','b','c']
re.findall(r"\w+", "café_123 ¡hola!")           # ['café_123','hola']  # Unicode letters included; punctuation excluded
re.findall(r"\W+", "a_b! $")                    # ['! ',' $']  # sequences of non-word chars
re.findall(r"\\+", r"a\\b \\" )                 # ['\\\\','\\\\']  # matches backslashes (escaped in string)
# raw string literals (r"...") are recommended for patterns containing backslashes