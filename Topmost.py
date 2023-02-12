import wordfreq
import sys
import urllib.request
import os.path

def main(file1,file2,n):
    if os.path.isfile(file2):
        with open(file2, "r") as article:
            p = article.read()
    else:
        response = urllib.request.urlopen(file2)
        p = response.read().decode("utf8").split()

    words = wordfreq.tokenize(p)
    with open(file1, "r") as listWords:
        stopWords = listWords.read().split()

    for i in range(len(stopWords)):
        stopWords[i] = stopWords[i].strip()

    frequencies = wordfreq.countWords(words, stopWords)

    return wordfreq.printTopMost(frequencies, int(n))

main(sys.argv[1], sys.argv[2], sys.argv[3])