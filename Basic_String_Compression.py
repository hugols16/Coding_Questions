import os
import datetime
import sys



def basic_string_compression(string1):
	if not string1:
		return False
	else:
		string1_dict = {}
		for character in string1:
			if character in string1_dict:
				string1_dict[character] += 1
			else:
				string1_dict[character] = 1
		return_string = ""
		if len(string1_dict) == len(string1):
			return string1
		else:
			for key in string1_dict:
				return_string += str(key)
				return_string += str(string1_dict[key])
			return return_string

string1 = raw_input("Enter a string:  ")
print "The compression is: "
print basic_string_compression(string1)
