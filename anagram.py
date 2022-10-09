def anagram(s1, s2):

    if len(s1) != len(s2):
        return False

    # return true if sorted strings are equal
    return sorted(s1) == sorted(s2)


# test the function with two strings that are anagrams
print(anagram('dog', 'god'))

 
