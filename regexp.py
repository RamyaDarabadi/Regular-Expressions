#First we need to import re to use Regualr Expr.
# There are some methods/attributes in Regular Expressions.
# findall(), search(), sub(), compile(), match(), finditer().
#Let us see all examples one by one. :-)

import re
string = 'ramya@emmela.com, ramya@atad.xyz, ramyalatha3004@gmail.com, raja@emmela.com, ,'
#re.findall() - which gives a list of matched string
#syntax - re.findall(pattern, string)
s = re.findall('[\w.]+@[\w.]+', string)
# \w returns any alphanumeric [a-zA-Z0-9_]
# . any character except newline
# + one or more repetitons. Empty string shouldn't match.
print s

line = 'In order to succeed we must first believe that we can'
#re.search() - The string would be searched for the pattern anywhere in the string
#syntax -  re.search(pattern, string)
l = re.search(r'believe',line) # Here r is raw string.
if l:
    print l.group() # method group() returns string matched by RE
else:
    print 'not found' 

programming = ["Python", "Perl", "PHP", "C++"]
pattern = 'Py.*|.*rl|.HP|\w.+' # | is or operation
for lang in programming:
    if re.search(pattern, lang, re.IGNORECASE): # IGNORECASE Do case-sensitive matches.
        print lang, 'FOUND'
    else:
        print lang, 'NOT FOUND'

text = "Python for beginner is a very cool"
t = re.sub("cool", "good", text) #substitute good in the place of cool.
print t

 
