import re

"""

Author: Thadryan Sweeney, Bioinformatics student, Northeastern University
Class:  Introduction to Data Mining and Machine Learning
Usage:  Engineer 14 complementary features for the kaggle reviewed dataset "Hillary Clinton and Donald Trump Tweets" https://www.kaggle.com/benhamner/clinton-trump-tweets
Notes:  This project started with 'manual' review of the dataset in libre office calc, where several features were removed
	    by simple deletion of row (URLs, id numbers, etc)
Python: Python 3.5.3 (default, Jan 19 2017, 14:11:04) [GCC 6.3.0 20170118] on linux 
0S:     Distributor ID:	Debian
        Description:	Debian GNU/Linux 9.2 (stretch)
        Release:	9.2
        Codename:	stretch

This function extracts numerous metrics from tweets such as number of sentences, average sentence length, 
and the presence and quantity of various syntactic and punctuation features. It also finds features of
technological interest like number of URLs and @ signs. A complete list of the features is at the bottom
of the page

"""

def get_metrics(tweet):
	
	# empty dict for results
	results = []

	# split tweet on spaces
	strings = tweet.split(" ")	
	
	###list comprehensions to get conditional counts

	# get count of words wth no URLs or web addresses 	
	word_list = [item for item in strings if "http" not in item and '#' not in item]

	# count the hashtags
	hashtag_count = len([item for item in strings if "#" in item])

	# count the @s
	at_count = len([item for item in strings if "@" in item])

	# count the URLS
	url_count = len([item for item in strings if "http" in item])

	# count the words in all caps (Exclude "I" because it gives false positive)
	all_caps_count = len([item for item in strings if item != "I" and item == item.upper()])
	
	### determine the average word lenth

	total_word_lengths = 0 
	for item in word_list:
		total_word_lengths += len(item)
	if len(word_list) > 0:
		mean_word_length = float(total_word_lengths)/float(len(word_list))
	else:
		mean_word_length = 0
	
	### find the number of sentences
	
	# start with a the words only tweet (join the words only list on spaces)
	tweet_text = " ".join(word_list)

	# remove quotes as they confuse the sentence parser 
	tweet_text = tweet_text.replace("'", "")
	tweet_text = tweet_text.replace('"', '')
	
	# this has been modified from a consesus approach on stack overflow
	# it iterates through the text and stop at a ".", ":", "?". "!".
	sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!|\:)(\s|[A-Z].*)', tweet_text)

	# remove empty strings from sentences - some '' and ' ' were counted as sentences
	for item in sentences:
		if len(item) == 0:
			sentences.remove(item)
		if item == ' ':
			sentences.remove(item)
	
	# get the number of sentences
	number_of_sentences = len([sentence for sentence in sentences if len(sentence) != 0])

	sentences_word_count = 0 
	mean_word_count = 0
	for item in sentences:
		sentences_word_count += (len(item.split(" ")))
		if sentences_word_count > 0:
			mean_word_count = float(sentences_word_count)/float(len(sentences))
		else:
			pass

	# count various syntactic and punctuation features
	commas = tweet_text.count(",")
	periods = tweet_text.count(".")
	exclamation_points = tweet_text.count("!")
	question_marks = tweet_text.count("?")
	colons = tweet_text.count(":")
	semi_colons = tweet_text.count(";")
	
	# store results in an array

	results.append(len(word_list)) 			# Number of words
	results.append(hashtag_count) 			# Number of hashtags
	results.append(at_count) 				# Number of "@" signs
	results.append(url_count) 				# Number of URLs
	results.append(all_caps_count) 			# Number of words_in_caps
	results.append(mean_word_length) 		# Mean_word_length
	results.append(commas) 					# Number of commas
	results.append(periods) 				# Number of periods
	results.append(exclamation_points) 		# Number of exclamation_points
	results.append(question_marks) 			# Number of question_marks
	results.append(colons) 					# Number of colons
	results.append(semi_colons) 			# Number of semi-colons
	results.append(number_of_sentences) 	# Number of entences
	results.append(mean_word_count) 		# Mean_sentence_length
	
	return results
