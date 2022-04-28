"""
There is a malfunctioning keyboard where some letter keys do not work.
 All other keys on the keyboard work properly.
Given a string text of words separated by a single space (no leading or trailing spaces) 
and a string brokenLetters of all distinct letter keys that are broken, 
return the number of words in text you can fully type using this keyboard.
"""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        #split the broken letters
        x = list(brokenLetters)
        #get all the words in the text given
        keep = text.split(" ")
        result = 0
        counter = 0
        
        #loop through each word
        for word in keep:
            #go through every letter in the workd and check if is broken
            for ch in word:
                if ch not in x:
                    counter +=1
            #if our counter is equal with the length of the word, it means there are no broken letters
            if counter == len(word):
                result+=1
            counter=0
        return result
                    
text = "hello world"
brokenLetters = "ad"