import re

s = "If we stand together, there's nothing we can't do! Make sure you're ready to VOTE: https://t.co/tTgeqxNqYm https://t.co/Q3Ymbb7UNy #GetFucked"

def analyze_tweet(tweet):
	
	# empty array for results
	results = {}

	# split tweet on spaces
	strings = tweet.split(" ")	
	
	# list comprehensions to get conditional counts
	# get count of words wth no URLs or web addresses 	
	word_list = [item for item in strings if "http" not in item and '#' not in item]

	# count the hashtags
	hashtag_count = len([item for item in strings if "#" in item])

	# count the URLS
	url_count = len([item for item in strings if "http" in item])

	# count the words in all caps
	all_caps_count = len([item for item in strings if item == item.upper()])
	
	# determine the average word lenth
	total_word_lengths = 0 
	for item in words:
		total_word_lengths += len(item)
	mean_word_length = float(total_word_lengths)/float(len(words))

	# count various syntactic and punctuation features
	commas = tweet.count(",")
	periods = tweet.count(".")
	exclamation_points = tweet.count("!")
	question_marks = tweet.count("?")
	colons = tweet.count(":")
	semi_colons = tweet.count(";")
	
	# find the number of sentences
	
	# start with a the words only tweet (join the words only list on spaces)
	tweet_text = " ".join(word_list)
	
	# this has been modified from a consesus approach on stack overflow
	# it iterates through the text and stop at a ".", ":", "?". "!".
	sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!|\:)(\s|[A-Z].*)', tweet_text)
	
	number_of_sentences = len(sentences)
	
	total_sentence_length = 0
	for item in number_of_sentences:
		total_sentence_length += len(item)
	mean_sentence_length = float(total_sentence_length)/float(len(sentences))
	
	
		

	# store results in dictionary
	results["Words"] = len(word_list)
	results["Hashtags"] = hashtag_count
	results["URLs"] = url_count
	results["Words in caps"] = all_caps_count
	results["Mean word length"] = mean_word_length
	results["Commas"] = commas
	results["Periods"] = periods
	results["Excamation points"] = exclamation_points
	results["Question marks"] = question_marks
	results["Colon"] = colons
	results["Semi-colons"] = semi_colons
	results["Number of sentences"] = number_of_sentences
	results["Mean sentence length"] = mean_sentence_length

	return results

data = analyze_tweet(s)

#for item in data:
#	print(item, data[item])

sent = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!|\:)(\s|[A-Z].*)', s)

rint("Tweet Words")
	print(tweet_words)
