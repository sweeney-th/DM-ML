
s = "If we stand together, there's nothing we can't do. Make sure you're ready to vote: https://t.co/tTgeqxNqYm https://t.co/Q3Ymbb7UNy #GetFucked"

# we can make three functions for this
def tweet_words(tweet):
	word_count = len([item for item in tweet.split(" ") if "http" not in item and '#' not in item])
	return word_count

def tweet_hastags(tweet):
	hashtag_count = len([item for item in tweet.split(" ") if "#" in item])
	return hashtag_count

def tweet_urls(tweet):
	url_count = len([item for item in tweet.split(" ") if "http" in item])
	return url_count

# or one that retuns an array
def analyze_tweet(tweet):
	results = []
	word_count = len([item for item in tweet.split(" ") if "http" not in item and '#' not in item])
	hashtag_count = len([item for item in tweet.split(" ") if "#" in item])
	url_count = len([item for item in tweet.split(" ") if "http" in item])
	results.append(word_count)
	results.append(hashtag_count)
	results.append(url_count)
	return results



print(tweet_words(s))
print(tweet_hastags(s))
print(tweet_urls(s))

data = analyze_tweet(s)
print(data[0])
print(data[1])
print(data[2])