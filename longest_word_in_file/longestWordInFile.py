def longest_word_in_file():
	"""
	A program that takes in a filename and displays the longest word(s) in the file,
	we\'ll be making use of text files only.
	: return: None
	"""
	filename = input('Enter the filename only, the file extension would be added: ')
	filename = filename.strip() + '.txt'
	words_and_their_length = {}
	try:
		with open(filename, 'r') as f_obj:
			for i in f_obj:
				split_sentence = i.split()
				for j in split_sentence:
					words_and_their_length[j] = len(j)
	except FileNotFoundError:
		print(f'The file \'{filename}\' couldn\'t be found')
	else:
		length_of_each_word = [i for i in words_and_their_length.values()]
		longestWord = max(length_of_each_word)
		if length_of_each_word.count(longestWord) == 1:
			for i,j in words_and_their_length.items():
				if j == longestWord:
					print(f'The Longest word in the file is {i}')
		else:
			tie_words = [i for i,j in words_and_their_length.items() if j == longestWord]
			print('The Longest words in the file are {}'.format(', '.join(tie_words)))

longest_word_in_file()