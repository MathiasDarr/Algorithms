"""



"""
import re
delimiters = "a", "...", "(c)"
example = "stackoverflow (c) is awesome... isn't it?"
regexPattern = '|'.join(map(re.escape, delimiters))
re.split(regexPattern, example)