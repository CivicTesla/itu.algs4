# Created for BADS 2018
# See README.md for details
# Python 3
import sys, os
def setpath():
    exe = sys.argv[0]
    p = os.path.split(exe)[0]
    sys.path.insert(0, os.path.join(p, '..', 'stdlib'))
    sys.path.insert(0, p)
setpath()
import stdio

#  Execution:    python file_index.py file1.txt file2.txt file3.txt ...
#
#  % python file_index.py ex*.txt
#  age
#   ex3.txt
#   ex4.txt 
# best
#   ex1.txt 
# was
#   ex1.txt
#   ex2.txt
#   ex3.txt
#   ex4.txt 
#
#  % python file_index.py *.txt
#
#  % python file_index.py *.py


"""
 *  The {@code FileIndex} class provides a client for indexing a set of files,
 *  specified as command-line arguments. It takes queries from standard input
 *  and prints each file that contains the given query.
"""

# key = word, value = set of files containing that word
st = {} 
        # TODO use ST instead?
args = sys.argv[1:]

# create inverted index of all files
print("Indexing files")
for filename in args:
    print("  " + filename)
    file = open(filename, 'r')
    for line in file.readlines():
        for word in line.split():
            if not word in st:
                st[word] = set()
            s = st.get(word)
            s.add(file)

# read queries from standard input, one per line
while not stdio.isEmpty():
    query = stdio.readString()
    if query in st:
        s = st.get(query)
        for file in s:
            print(" " + file.name)
# TODO close files in the end?