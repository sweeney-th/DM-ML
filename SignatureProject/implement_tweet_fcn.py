from tweet_analyzer import get_metrics
import csv

# open file of tweets after initial review
with open('tweets2.csv') as infile:
	raw_data = csv.reader(infile)
	data = list(raw_data)[1:] # from the header on

header = "handle,text,is_retweet,original_author,in_reply_to_screen_name,is_quote_status,\
lang,retweet_count,favorite_count,truncated,Words,Hashtags,At_signs,URLs,Words_in_caps,\
Mean_word_length,Commas,Periods,Exclamation_points,Question_marks,Colon,Semi-colons,\
Number_of_sentences,Mean_sentence_length"

# open a file, write header and newline
outfile = open("engineered_tweet_data.csv", "w")
outfile.write(header + "\n")

# get metrics for the text of each tweet, append them to row, write to file
for row in data:
	analysis = get_metrics(row[1])
	for item in analysis:
		row.append(item)
	for item in row:
		if item != '':
			outfile.write(str(item) + ",")
outfile.close()