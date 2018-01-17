#!/usr/bin/env python

'''

This script will ask the user three questions
and will combine their answers into a single sentence.

'''

# Ask the user three questions and store answers in separate variables
name = input("What is your name? ")
city = input("Hello {}. In what city were you born? ".format(name))
elementary = input("Interesting!  What was the name of the elementary school you went to? ".format(name))

# Combine and print all three of the inputs into a sentence
print("That's wild, {}!  I was also born in {} and I also went to {}.  What a small world!".format(name, city, elementary))