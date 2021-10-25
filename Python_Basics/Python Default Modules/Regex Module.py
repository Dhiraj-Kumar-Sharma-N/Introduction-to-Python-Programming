"""

NAME
    re - Support for regular expressions (RE).

DESCRIPTION
    This module provides regular expression matching operations similar to
    those found in Perl.  It supports both 8-bit and Unicode strings; both
    the pattern and the strings being processed can contain null bytes and
    characters outside the US ASCII range.

    Regular expressions can contain both special and ordinary characters.
    Most ordinary characters, like "A", "a", or "0", are the simplest
    regular expressions; they simply match themselves.  You can
    concatenate ordinary characters, so last matches the string 'last'.

    The special characters are:
        "."      Matches any character except a newline.
        "^"      Matches the start of the string.
        "$"      Matches the end of the string or just before the newline at
                 the end of the string.
        "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
                 Greedy means that it will match as many repetitions as possible.
        "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
        "?"      Matches 0 or 1 (greedy) of the preceding RE.
        *?,+?,?? Non-greedy versions of the previous three special characters.
        {m,n}    Matches from m to n repetitions of the preceding RE.
        {m,n}?   Non-greedy version of the above.
        "\\"     Either escapes special characters or signals a special sequence.
        []       Indicates a set of characters.
                 A "^" as the first character indicates a complementing set.
        "|"      A|B, creates an RE that will match either A or B.
        (...)    Matches the RE inside the parentheses.
                 The contents can be retrieved or matched later in the string.
        (?aiLmsux) Set the A, I, L, M, S, U, or X flag for the RE (see below).
        (?:...)  Non-grouping version of regular parentheses.
        (?P<name>...) The substring matched by the group is accessible by name.
        (?P=name)     Matches the text matched earlier by the group named name.
        (?#...)  A comment; ignored.
        (?=...)  Matches if ... matches next, but doesn't consume the string.
        (?!...)  Matches if ... doesn't match next.
        (?<=...) Matches if preceded by ... (must be fixed length).
        (?<!...) Matches if not preceded by ... (must be fixed length).
        (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                           the (optional) no pattern otherwise.

    The special sequences consist of "\\" and a character from the list
    below.  If the ordinary character is not on the list, then the
    resulting RE will match the second character.
        \number  Matches the contents of the group of the same number.
        \A       Matches only at the start of the string.
        \Z       Matches only at the end of the string.
        \b       Matches the empty string, but only at the start or end of a word.
        \B       Matches the empty string, but not at the start or end of a word.
        \d       Matches any decimal digit; equivalent to the set [0-9] in
                 bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the whole
                 range of Unicode digits.
        \D       Matches any non-digit character; equivalent to [^\d].
        \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v] in
                 bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the whole
                 range of Unicode whitespace characters.
        \S       Matches any non-whitespace character; equivalent to [^\s].
        \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
                 in bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the
                 range of Unicode alphanumeric characters (letters plus digits
                 plus underscore).
                 With LOCALE, it will match the set [0-9_] plus characters defined
                 as letters for the current locale.
        \W       Matches the complement of \w.
        \\       Matches a literal backslash.

    This module exports the following functions:
        match     Match a regular expression pattern to the beginning of a string.
        fullmatch Match a regular expression pattern to all of a string.
        search    Search a string for the presence of a pattern.
        sub       Substitute occurrences of a pattern found in a string.
        subn      Same as sub, but also return the number of substitutions made.
        split     Split a string by the occurrences of a pattern.
        findall   Find all occurrences of a pattern in a string.
        finditer  Return an iterator yielding a Match object for each match.
        compile   Compile a pattern into a Pattern object.
        purge     Clear the regular expression cache.
        escape    Backslash all non-alphanumerics in a string.

    Some of the functions in this module takes flags as optional parameters:
        A  ASCII       For string patterns, make \w, \W, \b, \B, \d, \D
                       match the corresponding ASCII character categories
                       (rather than the whole Unicode categories, which is the
                       default).
                       For bytes patterns, this flag is the only available
                       behaviour and needn't be specified.
        I  IGNORECASE  Perform case-insensitive matching.
        L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.
        M  MULTILINE   "^" matches the beginning of lines (after a newline)
                       as well as the string.
                       "$" matches the end of lines (before a newline) as well
                       as the end of the string.
        S  DOTALL      "." matches any character at all, including the newline.
        X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
        U  UNICODE     For compatibility only. Ignored for string patterns (it
                       is the default), and forbidden for bytes patterns.

    This module also defines an exception 'error'.

CLASSES
    builtins.Exception(builtins.BaseException)
        error
    builtins.object
        Match
        Pattern

    class Match(builtins.object)
     |  The result of re.match() and re.search().
     |  Match objects always have a boolean value of True.
     |
     |  Methods defined here:
     |
     |  __copy__(self, /)
     |
     |  __deepcopy__(self, memo, /)
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  end(self, group=0, /)
     |      Return index of the end of the substring matched by group.
     |
     |  expand(self, /, template)
     |      Return the string obtained by doing backslash substitution on the string template, as done by the sub() method.
     |
     |  group(...)
     |      group([group1, ...]) -> str or tuple.
     |      Return subgroup(s) of the match by indices or names.
     |      For 0 returns the entire match.
     |
     |  groupdict(self, /, default=None)
     |      Return a dictionary containing all the named subgroups of the match, keyed by the subgroup name.
     |
     |      default
     |        Is used for groups that did not participate in the match.
     |
     |  groups(self, /, default=None)
     |      Return a tuple containing all the subgroups of the match, from 1.
     |
     |      default
     |        Is used for groups that did not participate in the match.
     |
     |  span(self, group=0, /)
     |      For match object m, return the 2-tuple (m.start(group), m.end(group)).
     |
     |  start(self, group=0, /)
     |      Return index of the start of the substring matched by group.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  endpos
     |      The index into the string beyond which the RE engine will not go.
     |
     |  lastgroup
     |      The name of the last matched capturing group.
     |
     |  lastindex
     |      The integer index of the last matched capturing group.
     |
     |  pos
     |      The index into the string at which the RE engine started looking for a match.
     |
     |  re
     |      The regular expression object.
     |
     |  regs
     |
     |  string
     |      The string passed to match() or search().

    class Pattern(builtins.object)
     |  Compiled regular expression object.
     |
     |  Methods defined here:
     |
     |  __copy__(self, /)
     |
     |  __deepcopy__(self, memo, /)
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  findall(self, /, string, pos=0, endpos=9223372036854775807)
     |      Return a list of all non-overlapping matches of pattern in string.
     |
     |  finditer(self, /, string, pos=0, endpos=9223372036854775807)
     |      Return an iterator over all non-overlapping matches for the RE pattern in string.
     |
     |      For each match, the iterator returns a match object.
     |
     |  fullmatch(self, /, string, pos=0, endpos=9223372036854775807)
     |      Matches against all of the string.
     |
     |  match(self, /, string, pos=0, endpos=9223372036854775807)
     |      Matches zero or more characters at the beginning of the string.
     |
     |  scanner(self, /, string, pos=0, endpos=9223372036854775807)
     |
     |  search(self, /, string, pos=0, endpos=9223372036854775807)
     |      Scan through string looking for a match, and return a corresponding match object instance.
     |
     |      Return None if no position in the string matches.
     |
     |  split(self, /, string, maxsplit=0)
     |      Split string by the occurrences of pattern.
     |
     |  sub(self, /, repl, string, count=0)
     |      Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl.
     |
     |  subn(self, /, repl, string, count=0)
     |      Return the tuple (new_string, number_of_subs_made) found by replacing the leftmost non-overlapping occurrences of pattern with the replacement repl.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  flags
     |      The regex matching flags.
     |
     |  groupindex
     |      A dictionary mapping group names to group numbers.
     |
     |  groups
     |      The number of capturing groups in the pattern.
     |
     |  pattern
     |      The pattern string from which the RE object was compiled.

    class error(builtins.Exception)
     |  error(msg, pattern=None, pos=None)
     |
     |  Exception raised for invalid regular expressions.
     |
     |  Attributes:
     |
     |      msg: The unformatted error message
     |      pattern: The regular expression pattern
     |      pos: The index in the pattern where compilation failed (may be None)
     |      lineno: The line corresponding to pos (may be None)
     |      colno: The column corresponding to pos (may be None)
     |
     |  Method resolution order:
     |      error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, msg, pattern=None, pos=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |      exception cause
     |
     |  __context__
     |      exception context
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

FUNCTIONS
    compile(pattern, flags=0)
        Compile a regular expression pattern, returning a Pattern object.

    escape(pattern)
        Escape special characters in a string.

    findall(pattern, string, flags=0)
        Return a list of all non-overlapping matches in the string.

        If one or more capturing groups are present in the pattern, return
        a list of groups; this will be a list of tuples if the pattern
        has more than one group.

        Empty matches are included in the result.

    finditer(pattern, string, flags=0)
        Return an iterator over all non-overlapping matches in the
        string.  For each match, the iterator returns a Match object.

        Empty matches are included in the result.

    fullmatch(pattern, string, flags=0)
        Try to apply the pattern to all of the string, returning
        a Match object, or None if no match was found.

    match(pattern, string, flags=0)
        Try to apply the pattern at the start of the string, returning
        a Match object, or None if no match was found.

    purge()
        Clear the regular expression caches

    search(pattern, string, flags=0)
        Scan through string looking for a match to the pattern, returning
        a Match object, or None if no match was found.

    split(pattern, string, maxsplit=0, flags=0)
        Split the source string by the occurrences of the pattern,
        returning a list containing the resulting substrings.  If
        capturing parentheses are used in pattern, then the text of all
        groups in the pattern are also returned as part of the resulting
        list.  If maxsplit is nonzero, at most maxsplit splits occur,
        and the remainder of the string is returned as the final element
        of the list.

    sub(pattern, repl, string, count=0, flags=0)
        Return the string obtained by replacing the leftmost
        non-overlapping occurrences of the pattern in string by the
        replacement repl.  repl can be either a string or a callable;
        if a string, backslash escapes in it are processed.  If it is
        a callable, it's passed the Match object and must return
        a replacement string to be used.

    subn(pattern, repl, string, count=0, flags=0)
        Return a 2-tuple containing (new_string, number).
        new_string is the string obtained by replacing the leftmost
        non-overlapping occurrences of the pattern in the source
        string by the replacement repl.  number is the number of
        substitutions that were made. repl can be either a string or a
        callable; if a string, backslash escapes in it are processed.
        If it is a callable, it's passed the Match object and must
        return a replacement string to be used.

    template(pattern, flags=0)
        Compile a template pattern, returning a Pattern object

DATA
    A = <RegexFlag.ASCII: 256>
    ASCII = <RegexFlag.ASCII: 256>
    DOTALL = <RegexFlag.DOTALL: 16>
    I = <RegexFlag.IGNORECASE: 2>
    IGNORECASE = <RegexFlag.IGNORECASE: 2>
    L = <RegexFlag.LOCALE: 4>
    LOCALE = <RegexFlag.LOCALE: 4>
    M = <RegexFlag.MULTILINE: 8>
    MULTILINE = <RegexFlag.MULTILINE: 8>
    S = <RegexFlag.DOTALL: 16>
    U = <RegexFlag.UNICODE: 32>
    UNICODE = <RegexFlag.UNICODE: 32>
    VERBOSE = <RegexFlag.VERBOSE: 64>
    X = <RegexFlag.VERBOSE: 64>
    __all__ = ['match', 'fullmatch', 'search', 'sub', 'subn', 'split', 'fi...

VERSION
    2.2.1


"""
import re

my_str = "Python testing is easier and it is quick_"

print(my_str.split("is"))  # ['Python testing ', ' easier and it ', ' quick']
print(my_str.split("it"))  # ['Python testing is easier and ', ' is quick']

print(re.split("i[st]", my_str))  # ['Python testing ', ' easier and ', ' ', ' quick']

pattern = "is"

print(re.findall(pattern, my_str))  # ['is', 'is']

print(re.findall("i[st]", my_str))  # ['is', 'it', 'is']

print(re.findall("i", my_str))  # ['i', 'i', 'i', 'i', 'i', 'i']

print(re.findall("[qP]", my_str))  # ['P', 'q']

print(re.findall("[abcdef]", my_str))  # ['e', 'e', 'a', 'e', 'a', 'd', 'c']
print(re.findall("[a-f]", my_str))  # ['e', 'e', 'a', 'e', 'a', 'd', 'c']

print(re.findall("[a-zA-Z0-9]",
                 my_str))  # ['P', 'y', 't', 'h', 'o', 'n', 't', 'e', 's', 't', 'i', 'n', 'g', 'i', 's', 'e', 'a', 's', 'i', 'e', 'r', 'a', 'n', 'd', 'i', 't', 'i', 's', 'q', 'u', 'i', 'c', 'k']
print(re.findall(r"\w", my_str))

print(re.findall(r"\w\w",
                 my_str))  # ['Py', 'th', 'on', 'te', 'st', 'in', 'is', 'ea', 'si', 'er', 'an', 'it', 'is', 'qu', 'ic', 'k_']

# 1 \w = a-zA-Z0-9_
# 2 \w = a-zA-Z0-9_|a-zA-Z0-9_
#  \W =NOT ANY CHARACTER FROM THIS a-zA-Z0-9_
# \d single digit
# \d\d double digit
# ^ in the beginning of the String
# $ in the end of the String
# \b space (except first and last word in string)
# \B non-space(any character except space)
# \t Tab
# \n New line
# {2} two times of a character
# {2,4} 2,3,4 times of a character
# {2,}  2 OR More times of character
# {1,} 1 time or more
# +    1 time or more
# *   0 or more number of times
# ?  0 or 1 time of character
# re.I IGNORE_CASE FLAG FOR Regex
# re.M MULTI_LINE FLAG FOR Regex
# re.I|re.M Pipe symbol for multiple regex flags

print(re.findall(r"\W", my_str))  # [' ', ' ', ' ', ' ', ' ', ' ', ' ']

print(re.findall(r"\W", "mystery @123 KIL^"))  # [' ', '@', ' ', '^']

Text = "IP Address = 104.330.22.20 and Python version is Python27 Please upgrade to python3"

print(re.findall(r"\d", Text))  # ['1', '0', '4', '3', '3', '0', '2', '2', '2', '0', '2', '7', '3']

print(re.findall(r"\d\d", Text))  # ['10', '33', '22', '20', '27']

print(re.findall(r"\d\d\d", Text))  # ['104', '330']

print(re.findall(r"python\d", Text))  # ['python3']

print(re.findall(".", Text))  # All single characters including \w and \W

print(re.findall(".....",
                 Text))  # ['IP Ad', 'dress', ' = 10', '4.330', '.22.2', '0 and', ' Pyth', 'on ve', 'rsion', ' is P', 'ython', '27 Pl', 'ease ', 'upgra', 'de to', ' pyth']

print(re.findall(r"\.", Text))  # ['.', '.', '.']

print(re.findall(r'\.\d\d', Text))  # ['.33', '.22', '.20']

patt = r"\d\d\d\.\d\d\d.\d\d\.\d\d"

print(re.findall(patt, Text))  # ['104.330.22.20']

Str = "this     \t is  python3learnand it is easy \nto learn and it is  quick to learn"

print(re.findall("^thi[st]", Str))  # ['this']

print(re.findall("learn$", Str))  # ['learn']

print(re.findall("learn", Str))  # ['learn', 'learn', 'learn'] ==> learn
print(re.findall(r"\blearn", Str))  # ['learn', 'learn'] ==> _learn
print(re.findall(r"\blearn\b", Str))  # ['learn', 'learn']  ==> _learn_

print(re.findall("learn", Str))  # ['learn', 'learn', 'learn'] ==> learn
print(re.findall(r"\Blearn", Str))  # ['learn'] ==> *learn
print(re.findall(r"\Blearn\B", Str))  # ['learn']  ==> *learn*

print(re.findall(r"\n", Str))  # ['\n']
print(re.findall(r"\t", Str))  # ['\t']

text = "This is a pythonnnn and python aaa haaaafd xyzaaaaaaaa"
# my_pat=r'\bpython{4}\b'
my_pat = r'\bxyza{8}\b'
print(re.findall(my_pat, text))

text = "xaz asdfa sdf xaaz xaaaaaaaz xaaaaz  xz"
# my_pat=r'\bxa{2,}z\b'
# my_pat=r'xa{1,}z'
# my_pat=r'xa*z'
my_pat = r'xa?z'
print(re.findall(my_pat, text))

text = "this is a string ThIs is a new staring THIS"
my_pat = r'this'
print(re.findall(my_pat, text, re.I))  # ['this', 'ThIs', 'THIS']

text = """this is a string EnD
this is second line enD
This is third line end
asfasd this end"""
# print(text)

# my_pat=r'^this'
my_pat = r'end$'

print(re.findall(my_pat, text, re.M | re.I))  # ['EnD', 'enD', 'end', 'end']

# =========================================== SEARCH OPERATION =============================
text = """This  is for
python2 and there are two major
vers python3 and python in future python4"""

pat = r'\bpython[23]?\b'

# print(re.findall(pat,text))
search_ob = re.search(pat, text)
# rint(match_ob)
if search_ob:
    print("match from ur pattern: ", search_ob.group())
    print('Starting index: ', search_ob.start())
    print('Ending index: ', search_ob.end() - 1)
    print("Length: ", search_ob.end() - search_ob.start())
else:
    print("No match found")
"""
search and returns first occurrence from the find all list of values

match from ur pattern:  python2
Starting index:  13
Ending index:  19
Length:  7

"""
# =========================================== MATCH OPERATION =============================

text = """PYTHON2 and there are two major
vers python3 and python in future python4"""

pat = r'\bpython[23]?\b'
match_ob = re.match(pat, text, re.I)
if match_ob:
    print("match from ur pattern: ", match_ob.group())
    print('Starting index: ', match_ob.start())
    print('Ending index: ', match_ob.end() - 1)
    print("Length: ", match_ob.end() - match_ob.start())
else:
    print("No match found")

"""

search and returns value only the first word of String or multi-linr string

match from ur pattern:  PYTHON2
Starting index:  0
Ending index:  6
Length:  7

"""

# =========================================== FINDALL OPERATION =============================
text = """PYTHON2 and there are two major
vers python3 and python in future python4"""

pat = r'\bpython[23]?\b'
print(re.findall(pat, text, re.I))

# ['PYTHON2', 'python3', 'python']

# =========================================== FINDITER OPERATION =============================

# To give more detailed information of each element from find all list Finditer is used

my_str = "This is python and we are having python2 and python3 version"
my_pat = r'\bpython[23]?\b'
# print(re.search(my_pat,my_str))
# print(len(re.findall(my_pat,my_str)))
# print(re.findall(my_pat,my_str))

for each_ob in re.finditer(my_pat, my_str):
    print(f'The match is: {each_ob.group()} starting index: {each_ob.start()}, ending index {each_ob.end() - 1}')

"""

The match is: python starting index: 8, ending index 13
The match is: python2 starting index: 33, ending index 39
The match is: python3 starting index: 45, ending index 51

"""

# =========================================== SPLIT OPERATION =============================

my_str = "This is python and we are having python2 and Python3 version"

print(re.split('python[23]?', my_str, ))

# ['This is ', ' and we are having ', ' and ', ' version']

print(re.split('python[23]?', my_str, maxsplit=1, flags=re.I))

# ['This is ', ' and we are having python2 and Python3 version']

# =========================================== SUBSTITUTE OPERATION =============================

my_str1 = "This is python and we are having python2 and python3 version"

print(re.sub('python[23]?', 'DHIRAJ', my_str))

# This is DHIRAJ and we are having DHIRAJ and Python3 version

print(re.sub('python[23]?', 'DHIRAJ', my_str, flags=re.IGNORECASE))

# This is DHIRAJ and we are having DHIRAJ and DHIRAJ version

print(re.sub('python[23]?', 'DHIRAJ', my_str, count=1, flags=re.IGNORECASE))

# This is DHIRAJ and we are having python2 and Python3 version


# =========================================== SUBSTITUTE OPERATION =============================

# Returns a tuple consisting of replaced string and the count of it

my_str1 = "This is python and we are having python2 and python3 version"

print(re.subn('python[23]?', 'DHIRAJ', my_str))

# ('This is DHIRAJ and we are having DHIRAJ and Python3 version', 2)

print(re.subn('python[23]?', 'DHIRAJ', my_str, flags=re.IGNORECASE))

# ('This is DHIRAJ and we are having DHIRAJ and DHIRAJ version', 3)

print(re.subn('python[23]?', 'DHIRAJ', my_str, count=1, flags=re.IGNORECASE))

# ('This is DHIRAJ and we are having python2 and Python3 version', 1)

# =========================================== COMPILE OPERATION =============================

# A pattern object is created using compile object in order that all re functions are performed on the string using the object

my_str = "This is about python. Python is easy to learn  and we have two major versions: python2 and python3 "

my_pat = r'\bPython[23]?\b'

# print(re.search(my_pat,my_str))
# print(re.findall(my_pat,my_str,flags=re.I))
# print(re.split(my_pat,my_str))


pat_ob = re.compile(my_pat, flags=re.I)
print(pat_ob)
print(pat_ob.search(my_str))
print(pat_ob.findall(my_str))

# re.findall(my_pat,my_str)===> re.compile(my_pat).findall(my_str)

"""

re.compile('\\bPython[23]?\\b', re.IGNORECASE)
<re.Match object; span=(14, 20), match='python'>
['python', 'Python', 'python2', 'python3']

"""