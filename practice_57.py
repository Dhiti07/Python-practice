# finding the group of anagrams in the whole list

def group_anagrams(words):
    anagrams = {}
    for eachword in words:
        sorted_word = ''.join(sorted(eachword))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(eachword)
        else:
            anagrams[sorted_word] = [eachword]

    return list(anagrams.values())

words = ['eat','tea','tan','ate','nat','bat']
print(group_anagrams(words))