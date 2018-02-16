#!/usr/bin/env python3
"""Retrieve and print words from a URL.

Usage:

    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """
    Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from
        the document
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """
    Prints the items in a list supplied as a parameter

    Args:
        items: A list of strings.

    Returns:
        No return. Prints strings.
    """
    for item in items:
        print(item)


def main(url):
    """
    This is the main function. It is called if the script
    is run from the command line.  The if at the end of this
    file checks the __name__ to determine whether it is
    __main__, and if it is, then the module is being run
    from the commandline and this function should be run.
    It can also be accessed directly from the REPL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        No return. Prints the words from the supplied document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
