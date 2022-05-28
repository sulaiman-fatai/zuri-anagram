# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
def Find_anagram (word, anagram):
 word = word.lower(), 
 anagram = anagram.lower()
 # driver code
word = input('Enter your first string:- ')
anagram = input('Enter your second string:- ')
Find_anagram(word, anagram)
# Get lengths of both strings
m1 = len(word)
m2 = len(anagram)       
# Sort both strings
if m1 == m2:
   sort_word = sorted(word)
   sort_anagram = sorted(anagram)
   #If arguement for anagram or not anagram
   if (sort_word == sort_anagram):
    print(word + " and " + anagram + " are anagrams. --> True")
   else:
     print(word + " and " + anagram +" are not anagrams. --> False")
else: 
     print("Since both "+ word + " and " + anagram + " have unequal character length hence they are not anagrams --> False.") 