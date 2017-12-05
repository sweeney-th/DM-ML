from tweet_analyzer import get_metrics
import csv

# this script implements the get metrics function described in "tweet_analyzer.py"
# open file of tweets after initial review
with open('tweets2.csv') as infile:
	raw_data = csv.reader(infile)
	data = list(raw_data)[1:] # from the header on

print(data)
header = "handle,text,is_retweet,original_author,in_reply_to_screen_name,is_quote_status,\
lang,retweet_count,favorite_count,truncated,Words,Hashtags,At_signs,URLs,Words_in_caps,\
Mean_word_length,Commas,Periods,Exclamation_points,Question_marks,Colon,Semi-colons,\
Number_of_sentences,Mean_sentence_length"

# open a file, write header and newline
outfile = open("engineered_tweet_data.csv", "w")
outfile.write(header + "\n")

# get metrics for the text of each tweet, append them to row, write to file

for row in data:
	row[1] = row[1].replace(",","")
	row[1] = row[1].replace("\n","")	
	row[1] = row[1].replace("'","")
	row[1] = row[1].replace('"',"")
	row[1] = row[1].replace('"',"")
	row[1] = row[1].replace("  "," ")
	if "&" in row[1]:
		pass
	else:	
		current = get_metrics(row[1])
		row = row + current
		print(row)
		print(len(row))
		for item in row:
			outfile.write(str(item) + ",")
		outfile.write("\n")
# for row in data:
# 	print(type(row))
# 	analysis = get_metrics(row[1])
# 	for item in analysis:
# 		row.append(item)
# 	print(analysis)
# 	for feature in row:
# 		if feature != '':
# 			outfile.write(str(feature) + ",")
# outfile.close()