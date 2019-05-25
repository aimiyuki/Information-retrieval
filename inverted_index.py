import sys

# create an empty "index"
reversed_index = {}

def add_file_to_index(filename):
    # read the content of the file
    with open(filename) as f:
        content = f.read()

    # split the file content into tokens
    tokens = content.split(" ")
    for token in tokens:
        # we strip the space of the tokens
        token = token.strip()

        """
        if we see the token for the first time
        we create a new empty list for it in our dictionary
        """

        if token not in reversed_index:
            reversed_index[token] = []

        """
        add the token/filename pair to the reversed index
        for example
        {"fox": []} -> {"fox": ["aaa.txt"]}
        """
        reversed_index[token].append(filename)


def build_index(files):
    # iterate on each file
    for filename in files:
        add_file_to_index(filename)


def print_index():
    # sort the index (this will sort by key)
    sorted_index = sorted(reversed_index.items())

    # iterate on the key/value pairs in the sorted index
    for key, value in sorted_index:
        """
        format the values so that ["aaa.txt", "bbb.txt"]
        becomes a single string "aaa.txt bbb.txt"
        """
        values = " ".join(value)
        print("{0}  {1}".format(key, values))

"""
given files aaa.txt and bbb.txt in the same
directory as this program
this program can be executed by running
python reversed_index.py aaa.txt bbb.txt
"""

"""
this will contain the files passe to the program
so ["aaa.txt", "bbb.txt"] for the example
"""

files = sys.argv[1:]

"""
build the index for all the files
passed to the program
"""

build_index(files)


# print the result
print_index()
