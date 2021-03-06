'''
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
first_not_repeating_character(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
first_not_repeating_character(s) = '_'.

There are no characters in this string that do not repeat.

[execution time limit] 4 seconds (py3)

[input] string s

A string that contains only lowercase English letters.

[output] char

The first non-repeating character in s of '_' if there are no characters that do not repeat.
'''


def first_not_repeating_character(s):
    # create a dict with key of letter, value of increments of how many time the letters appear
    # add the order of the character to a list
    # loop through letter order, find the len of 1 in the dict
    # return that letter
    letter_order = []
    dict = {}
    for letter in s:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
            letter_order.append(letter)
    print(dict)
    print(letter_order)
    for letter in letter_order:
        if dict[letter] == 1:
            return letter
    return "_"


'''
Time complexity: O(n+n) ~ O(n)
Space complexity: O(n)
'''

print(first_not_repeating_character("abacabad"))
print(first_not_repeating_character("abacabaabacaba"))
