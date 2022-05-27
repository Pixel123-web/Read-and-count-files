# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


from pydoc import text


def read_file_content(filename):
    # [assignment] Add your code here 
    filename = "story.txt"
    with open(filename, "r") as f:
        doc = f.read()
        return(doc)

def count_words():
    text = read_file_content("story.txt")
    words = []

    words = text.lower().split() 
    myDict = {}
    for key in words:
        myDict[key] = words.count(key)

    print("Dictionary Items  :  ",  myDict)

count_words()
    