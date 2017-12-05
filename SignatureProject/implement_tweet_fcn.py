from url import analyze_tweet

x = "If we stand together, there's nothing we can't do! Make; sure you're ready to VOTE: https://t.co/tTgeqxNqYm https://t.co/Q3Ymbb7UNy #GetFucked"

#test = analyze_tweet(x)

import csv

with open('tweets2.csv') as infile:
	raw_data = csv.reader(infile)
	data = list(raw_data)[1:] # from the header on


for item in data:
	print(item[1], "\n")
	print(analyze_tweet(item[1]), "\n")

