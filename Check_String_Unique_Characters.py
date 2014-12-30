import os
import datetime
import sys

def check_unique(string):
	if len(string) > 128:
		print "This string is unique"
		return True
	else:
		string_list = []
		for character in string:
			if character in string_list:
				print "This string is not unique"
				return False
			else:
				string_list.append(character)
		print "This string is unique"
		return True


string = raw_input("Enter a String:    ")
check_unique(string)



