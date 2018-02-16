"""Retrieve and print words from a URL.

Usage:

    python3 wordcount <filename_in> <filename_out>
"""

import sys

def count_words(filename_in, filename_out):
    """
    Function that counts the frequency of words.

    The function takes an input file key:value pairs
    of word and count, which can be saved to a .txt or
    .csv file.

    Args:
        filename_in: a string file name, no directory path. Can be a
            .txt file or a .raw file.
        filename_out: a string file name, no direcory path, to output
            the counts to. Can be .txt or .csv
    """
    results = dict()
    with open(filename_in, 'r') as f:
        for line in f:
            for word in line.split():
                word = word.replace(',', '').replace('.', '').lower()
                results[word] = results.setdefault(word, 0) + 1

    r = open(filename_out, 'w')

    for word, count in sorted(results.items(), key=lambda x: x[1]):
        #print('{} {}'.format(count, word))
        r.write('{}, {}'.format(word, count) + '\n')

    r.close()


if __name__ == '__main__':
    count_words(sys.argv[1], sys.argv[2])
