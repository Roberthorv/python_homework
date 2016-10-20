## import the os package:
import os

## making the new class FastaParser:

class FastaParser(object):
	"""A FastaParser class
	Input-object: a file containing DNA sequences in a fasta format. 
	This class will put the information from the fasta-files in a dictionary.
	FastaParser just take one input: the path to the fasta-file.
	"""

	def __init__(self, path = "none"):
		""" Defining the init of the FastaParser class """
		if path == "none": raise TypeError("Missing input!") # This will return a TypeError if the user don't give an input 
		self.path = os.path.join(os.getcwd(), path) # This will define the absolut path to the input fasta-file.
		if os.path.isfile(self.path) == False: raise IOError("The file doesn't exist!") # This will test if the file given by the user exists. If not a IOError will be returned.

	def my_dic(self):
		""" A method the will put the information from the fasta-file in a dictionary and return this new dictionary."""
		file = [l.strip("\n").split(",") for l in open(self.path)] # Read in the fasta-file
		my_dictionary = {} # Creating a empty dictionary 
		for line in file:
			if str(line).find(">") >= 0: # Chek if the line starts with > aka dose this line contain a sequence name?
				my_dictionary.update({ str(line).replace("['>","").replace("']","") : "",}) # If the line dose contain the sequence name: create a new entry in my_dictionary with the sequence name as key and an empty value.
				my_key = str(line).replace("['>","").replace("']","") # define my_key as the newly created key 
			else:
				my_dictionary[my_key] = my_dictionary[my_key] + str(line).replace("['","").replace("']","") # Add the coresponding sequence to the new entry of my_dictionary
		return my_dictionary

	def count(self):
		""" A method counting the number of given sequences """
		return len(self.my_dic())
	
	def __len__(self):
		""" Defining the len function for the FastaParser class """
		return len(self.my_dic())

	def __getitem__(self, key):
		""" Define a key for the FastaParser class.
		Keys for the FastaParser class can be number or the name of the DNA sequences.
		"""

		""" Finde the right sequence if the key is a number: """
		if isinstance(key, int) == True:
			if key > len(self): raise IndexError("Index out of boundary!") # This will return an IndexError if the number given as key is to big
			num = -1
			for i in self.my_dic(): # Find the n-th key (the key coresponding to the number provided by the user) in my_dictionary
				num += 1
				if num == key:
					return self.my_dic()[i]

		""" Finde the right sequence if the key is the name of the sequence """
		if isinstance(key, str) == True:
			try:
				self.my_dic()[key]
			except KeyError:
				raise KeyError("There is no %s key found in the %s file!" % (key, self.path)) # This will return an KeyError if the sequence name given by the user dosen't exist
			return self.my_dic()[key]

	def extract_length(self, my_len):
		""" A method geting all sequences under a certain length"""
		new_list = [] # Creating a empty list for the results
		for i in self.my_dic():
			if len(str(self.my_dic()[i])) < my_len:
				new_list.append(str(self.my_dic()[i])) # Adding the sequence found to be shorter than the length provided by the user to the result list
		return new_list

	def length_dist(self, PDF_path):
		""" A method creating a PDF with a plot showing the length distribution of the sequences"""

		""" Importing some packages """
		import numpy as np
		import matplotlib.mlab as mlab
		import matplotlib.pyplot as plt

		""" Saving the length of each sequence in the fasta-file in a list """
		my_length = []
		for i in self.my_dic():
			my_length.append(len(str(self.my_dic()[i])))

		""" Ploting and saving th eplot in a PDF """
		my_plot = plt.hist(my_length)
		plt.xlabel("Length")
		plt.ylabel("Number of sequences")
		plt.savefig(PDF_path)












