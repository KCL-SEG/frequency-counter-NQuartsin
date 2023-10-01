"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    i = 0
    j = 1
        while(i<len(items)):
            if not items[i] in frequencies:
                counter = 1
                while(j<len(items)):
                    if (items[i] == items[j]):
                        counter = counter + 1
                    j = j + 1
                frequencies[items[i]] = counter
            i = i + 1
            j = i + 1
    return frequencies
