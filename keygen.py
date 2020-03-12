#!/usr/bin/env python3

# Copyleft (C) Alexandria Pettit, GNU GPLv3 or something
# IDK, the code is fairly trivial, but I'll put that there anyway

# This is my solution to "keyGme by rion" challenge! 
# See: https://crackmes.one/crackme/5c268e8333c5d41e58e00654

import random, string

def genSumchar(string):
    summation = 0
    for ch in string:
        summation = (summation + ord(ch) >> 1) % 0xf00 + 10
    return chr(summation)

def genCapitalAlphanum(length):
    alphanum = ''
    options = string.ascii_uppercase + string.digits
    for i in range(length):
        alphanum += random.choice(options)
    return alphanum

random_str = genCapitalAlphanum(15)
sumchar = genSumchar(random_str)
key = random_str + sumchar

print(f'Your new key is: {key}\nHave a nice day ^w^' )
