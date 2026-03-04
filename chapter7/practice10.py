# Write a function that takes a string and returns the count of vowels and consonants separately.

def countVowConso(string) :
    vowels = "aeiouAEIOU"

    countVowels = 0
    countconsonants = 0

    for str in string :
        if(str.isalpha()):
            if(str in vowels):
                countVowels += 1
            else:
                countconsonants += 1

    return countVowels, countconsonants


vowels, consonants = countVowConso("Parth Lad")

print(vowels, consonants)