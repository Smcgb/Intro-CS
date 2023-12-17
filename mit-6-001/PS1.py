#!/usr/bin/env python
# coding: utf-8

# ## PS1
# 
# ### Problem 1
# 
# Assume s is a string of lower case characters.
# 
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
# 
# `Number of vowels: 5`

# In[1]:


def count_vowel(s):
    """
    Count the number of vowels in a given string.

    Args:
        s (str): The input string to count vowels from.

    Returns:
        None: This function does not return anything, it only prints the result.

    Example:
        >>> count_vowel('Hello, World!')
        Number of vowels: 3
    """
    s = str.lower(s)
    vowel_list = ['a','e','i','o','u']
    
    count_vowel = 0
    
    for l in s:
        if l in vowel_list:
            count_vowel += 1
    
    print('Number of vowels:', count_vowel)
    
# count_vowel(s) # used for unit testing within MITx grader
# test cast

s = 'azcbobobegghakl'
count_vowel(s)


# ### Problem 2
# 
# Assume s is a string of lower case characters.
# 
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
# 
# `Number of times bob occurs is: 2`

# In[2]:


def count_bob(s):
    """
    Count the number of times the substring 'bob' occurs in a given string.

    Args:
        s (str): The input string to count 'bob' from.

    Returns:
        None: This function does not return anything, it only prints the result.

    Example:
        >>> count_bob('azcbobobegghakl')
        Number of times bob occurs is: 2
    """
    bobs = 0

    for num, letter in enumerate(s):
        if letter == 'b':
            if s[num:(num+3)] == 'bob':
                bobs += 1
            
    print('Number of times bob occurs is: ', bobs)

# count_bob(s) # used for unit testing within MITx grader
# test cast

s = 'azcbobobegghakl'
count_bob(s)


# ### Problem 3
# 
# Assume s is a string of lower case characters.
# 
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
# 
# `Longest substring in alphabetical order is: beggh`
# 
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# 
# `Longest substring in alphabetical order is: abc`

# In[3]:


def find_longest_substring(s):
    """
    Find the longest substring in alphabetical order in a given string.

    Args:
        s (str): The input string to find the longest substring in alphabetical order from.

    Returns:
        str: None: This function does not return anything, it only prints the result.

    Example:
        >>> find_longest_substring('azcbobobegghakl')
        'beggh'
    """
for i,v in enumerate(s):
    if i == 0:
        longest = v
        current = v
    elif v >= s[i-1]:
        current += v
        if len(current) > len(longest):
            longest = current
    else:
        current = v

print("Longest substring in alphabetical order is: " + longest)

# find_longest_substring(s) # used for unit testing within MITx grader
# test cast

s = 'azcbobobegghakl'
find_longest_substring(s)


# In[4]:


get_ipython().system('jupyter nbconvert PS1.ipynb --to python')

