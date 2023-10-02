"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    i = 0
    items = [str(item).strip(" '") for item in items]
    while(i<len(items)):
        if items[i] not in frequencies:
            counter = 1
            j = i + 1
            while(j<len(items)):
                if (str(items[i] == items[j])):
                    counter = counter + 1
                j = j + 1
            frequencies[items[i]] = counter
        i = i + 1
    return frequencies
