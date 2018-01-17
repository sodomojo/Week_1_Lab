#!/usr/bin/env python

'''

This script will ask the user three questions
and will combine their answers into a single sentence.

'''

# Ask the user three questions and store answers in separate variables
name = input("What is your name?: ")
year = input("Hello {}. What year were you born?: ".format(name))
first_car = input("What was your first car?: ")

# Combine and print all three of the inputs into a sentence
print("That's great, {}!  You were born in {} and your first car was a {}".format(name, year, first_car))