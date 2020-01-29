#get sentence from user

#give_the_users_answer_and_convert_to_lowercase_and_remove_any_extra_space

original = input("Please enter a sentece:").strip().lower()

#to split sentence into words

words = original.split()

#loop through words and convert to pig latin

new_words = []

for word in words:
    if word[0] in "aeiou":
      new_word = word + "yay"
      new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
               else:                   break                cons = word[:vowel_pos]
                the_rest = word[vowel_pos:]
                new_word = the_rest + cons + "ay"
                new_words.append(new_word)
                
      
#if starts with a vowel, just add "yay"

output =" ".join(new_words)
#otherwise, move the first consonant cluser to end, and add "ay"

#stick words back together
print(output)
