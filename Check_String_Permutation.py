import os
import datetime
import sys

def check_permutation(string1, string2):
	if not len(string1) == len(string2):
		return False
	else:
		string1_dict = {}
		for character in string1:
			if character in string1_dict:
				string1_dict[character] += 1
			else:
				string1_dict[character] = 1
		string2_dict = {}
		for character in string2:
			if character in string2_dict:
				string2_dict[character] += 1
			else:
				string2_dict[character] = 1		
		if string1_dict == string2_dict:
			return True
		else:
			return False

string1 = raw_input("Enter first string:  ")
string2 = raw_input("Enter second string:  ")

if check_permutation(string1, string2):
	print "The second string is a permutation of the first one"
else:
	print "The second string is not a permutation of the first one"

