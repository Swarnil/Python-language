#Capital Letter
# Write a function named capital_indexes. The function takes a single parameter, which is a string.
# Your function should return a list of all the indexes in the string that have capital letters.
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

def capital_indexes(s):
    list=[]
    for i in range(0,len(s)):
        if s[i].isupper()== True:
            list.append(i)
    return list
s='HeLlO'
print(capital_indexes(s))


# Middle letter
# Write a function named mid that takes a string as its parameter.
# Your function should extract and return the middle letter.
# If there is no middle letter, your function should return the empty string.
#
# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid(s):
    m=len(s)
    if m%2==0:
        return ""
    else:
        m=m//2
        return s[m]
s='abcdeeg'
print(mid(s))


# Challenge
# Online status
# The aim of this challenge is, given a dictionary of people's online status, '
# to count the number of people who are online.
#
# For example, consider the following dictionary:
#
# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }
# In this case, the number of people online is 2.
#
# Write a function named online_count that takes one parameter.
# The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
#
# Your function should return the number of people who are online.

def online_count(statuses):
    count=0
    # print(statuses.items())
    for i in statuses.values():
        if i == 'online':
            count+=1
    return count
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print(online_count(statuses))


# Randomness
# Define a function, random_number, that takes no parameters.
# The function must generate a random integer between 1 and 100, both inclusive, and return it.
#
# Calling the function multiple times should (usually) return different numbers.
#
# For example, calling random_number() some times might first return 42, then 63, then 1.

import random
def random_number():
    return random.randint(1,100)
random_number();


# Type check
# Write a function named only_ints that takes two parameters.
# Your function should return True if both parameters are integers, and False otherwise.
#
# For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.

def only_ints(a,b):
    if type(a)==type(b):
        return True
    else:
        return False
a=2
b='g'
print(only_ints(a,b))


# Double letters
# The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row.
# For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.
#
# Define a function named double_letters that takes a single parameter. The parameter is a string.
# Your function must return True if there are two identical letters in a row in the string, and False otherwise.

def double_letters(s):
    flag=0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            flag=1
    if flag==1:
        return True
    else:
        return False
print(double_letters('hello'))


# Adding and removing dots
# Write a function named add_dots that takes a string and adds "." in between each letter.
# For example, calling add_dots("test") should return the string "t.e.s.t".
#
# Then, below the add_dots function, write another function named remove_dots that removes all dots from a string.
# For example, calling remove_dots("t.e.s.t") should return "test".
#
# If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.
#
# (You may assume that the input to add_dots does not itself contain any dots.)
def add_dots(s1):
    empty = ''
    count = 0
    for i in range(len(s1)):
        count += 1
        empty = empty + s1[i]
        if count != len(s1):
            empty = empty + '.'
    return empty


def remove_dots(s2):
    empty2 = ''
    for i in range(len(s2)):
        if s2[i] != ".":
            empty2 = empty2 + s2[i]
    return empty2

print(remove_dots(add_dots("Gopal")))


# Counting syllables
# Define a function named count that takes a single parameter.
# The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:
#
# "ho-tel"
# "cat"
# "met-a-phor"
# "ter-min-a-tor"
# Your function should count the number of syllables and return it.
#
# For example, the call count("ho-tel") should return 2.
def count(s):
    count=0
    for i in s:
        if i=='-':
            count+=1
    return count+1
print(count("ter-min-a-tor"))

# Anagrams
# Two strings are anagrams if you can make one from the other by rearranging the letters.
#
# Write a function named is_anagram that takes two strings as its parameters.
# Your function should return True if the strings are anagrams, and False otherwise.
#
# For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.

def is_anagram(s,s1):
    s=sorted(s)
    print(s)
    s1=sorted(s1)
    print(s1)
    if(s==s1):
        return True
    else:
        return False
print(is_anagram("typhoon","opython"))


# Flatten a list
# Write a function that takes a list of lists and flattens it into a one-dimensional list.
#
# Name your function flatten. It should take a single parameter and return a list.
#
# For example, calling:
#
# flatten([[1, 2], [3, 4]])
# Should return the list:
#
# [1, 2, 3, 4]

def flatten(l):
    list=[]
    count=0
    for i in l:
        for j in i:
            list.append(j)
    return list
print(flatten([[1,2],[3,4]]))


# Min-maxing
# Define a function named largest_difference that takes a list of numbers as its only parameter.
#
# Your function should compute and return the difference between the largest and smallest number in the list.
#
# For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.
#
# You may assume that no numbers are smaller or larger than -100 and
def largest_difference(l):
    large=l[0]
    for i in range(1,len(l)):
        if l[i]>large:
            large=l[i]
    small=l[0]
    for i in range(1,len(l)):
        if l[i]<small:
            small=l[i]
    return large-small
print(largest_difference([1,2,3,4]))

# Divisible by 3
# Define a function named div_3 that returns True if its single integer parameter is divisible by 3 and False otherwise.
#
# For example, div_3(6) is True because 6/3 does not leave any remainder.
# However div_3(5) is False because 5/3 leaves 2 as a remainder.

def div_3(n):
    if n%3==0:
        return True
    else:
        return False
print(div_3(6))

# Palindrome
# A string is a palindrome when it is the same when read backwards.
#
# For example, the string "bob" is a palindrome. So is "abba".
# But the string "abcd" is not a palindrome, because "abcd" != "dcba".
#
# Write a function named palindrome that takes a single string as its parameter.
# Your function should return True if the string is a palindrome, and False otherwise.

def palindrome(s):
    s1=''
    for i in range(len(s)-1,-1,-1):
        s1=s1+s[i]
    if s==s1:
        return True
    else:
        return False
print((palindrome("madam")))