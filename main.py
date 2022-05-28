# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    str1_list = list(word)
    str1_list.sort()
    str2_list = list(anagram)
    str2_list.sort()

    if str1_list == str2_list:
        return True
    else:
        return False

print(find_anagram("war", "raw"))