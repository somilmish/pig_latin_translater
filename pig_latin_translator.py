#This is a pig latin translator made for fun!

''' Rules:
* If word starts with vowel, add 'ay' to the end
* If word does not start with vowel, put first letter at the end, then add 'ay' '''
def pig_latin(word):
    ''' takes in the word in the variable word'''
    if word[0] in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + word[0] + 'ay'

    return pig_word