"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    i = 0
    #items = items.split(',')
    mod_items = []
    for item in items:
        item = item.strip().strip("'")
        mod_items.append(item)
    while(i<len(mod_items)):
        if mod_items[i] not in frequencies:
            counter = 1
            j = i + 1
            while(j<len(mod_items)):
                if mod_items[i] == mod_items[j]:
                    counter = counter + 1
                j = j + 1
            frequencies[mod_items[i]] = counter
        i = i + 1
    return frequencies
