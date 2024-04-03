dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic4 = {}

def concatenate_dictionaries(dict):
    for k, v in dict.items():
        dic4[k] = v





concatenate_dictionaries(dic1)
concatenate_dictionaries(dic2)
concatenate_dictionaries(dic3)

print(dic4)