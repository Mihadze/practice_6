def is_anagram(word1, word2):
    word1_list = list(word1)
    word2_list = list(word2)
    word1_list.remove(' ')
    word2_list.remove(' ')
    word1_list.sort()
    word2_list.sort()
    if (word1_list == word2_list):
        print('cовпадают')
    else:
        print('не совпадают')
