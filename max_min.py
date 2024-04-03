di = {'a': 5, 'b': 3, 'c': 9, 'd': 14, 'e': 2, 'f': 20, 'g': 9, 'h': 12}

most_common_letter = None
tally = -1
for key, value in di.items():
    if value > tally:
        tally = value
        most_common_letter = key

print(most_common_letter, tally)