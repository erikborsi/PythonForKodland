# Write a program that asks the user for the number of lines for the entered poem. It then allows the user to enter the
# desired number of lines. Then output the number of lines, vowels and consonants in the poem and in each line.
# For simplicity, let us enter the poem in small English letters only.
#
# Input example:
# How many lines will there be? 4
#
# Once there was an elephant,
# Who tried to use the telephant
# No! No! I mean an elephone
# Who tried to use the telephone
#
# Example result:
# Number of vowels: 40
# Number of consonants: 51

# So the question not makes sense compared to the example shown.
# It says, "Then output the number of lines, vowels and consonants in the poem and in each line".
# That's fine, but then look on the example.
# The example shows the total numbers, not the numbers at each line.
# The example also not shows the line number.
# Call me silly but it does not makes sense, haha.
# Whatever, so I designed mine in mind if both needed.
# Just comment out the line 15 if it is needed to be seen after each line.

def prompt():
    poem_lines_list = []
    number_of_lines = int(input("How many lines will there be? "))
    for i in range(number_of_lines):
        poem_line = input()
        # count_vowels_and_consonants(poem_line)
        poem_lines_list.append(poem_line)
    poem = ''.join(poem_lines_list)
    count_vowels_and_consonants(poem)


def count_vowels_and_consonants(poem):
    vowels = 0
    consonants = 0
    poem = ''.join(i for i in poem if i.isalnum())
    for i in poem.lower():
        if i in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    console_out(vowels, consonants)


def console_out(vowels, consonants):
    print("Number of vowels: " + str(vowels))
    print("Number of consonants: " + str(consonants))


prompt()
