# You can remove 'pass' if you written code in the function 

# Exercise 1
def count_characters(text):
    return len(text)
    
# Exercise 2
def remove_spaces(text):
    return text.replace(" ", "")
    
# Exercise 3
def count_vowels(text):
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count += 1
    return count
        
# Exercise 4
def replace_vowels(text):
    result = ""
    for char in text:
        if char in "aeiou":
            result += "*"
        else:
            result += char
    return result

# Exercise 5
def count_words(text):
    # Write your code here
    pass

# Exercise 6
def find_longest_word(text):
    # Write your code here
    pass
