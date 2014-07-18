import csv
import re


def get_sentiment_dictionary():
	sentiment_file = open("../data/inquirerbasic.csv", 'rU')
	return csv.DictReader(sentiment_file)


def import_tweets():
	tweet_dictionary = dict()
	raw_tweets = open("../data/tweets.txt", 'r')
	for line in raw_tweets:
		hashtag = line[:line.find(" ")]
		full_tweets = line[line.find(" "):]
		final_tweets = []
		for tweet in full_tweets.split("||"):
			final_tweets.append(curate_line(tweet))
		tweet_dictionary[hashtag] = final_tweets
	return tweet_dictionary
	



def get_tweets(hashtag="#mh17"):
	print hashtag
	hashtag = hashtag.lower()
	tweets = import_tweets()
	return tweets[hashtag]
	

def curate_line(tweet):
	print tweet
	tweet = re.sub('[^\ \w]', '', tweet)
	print tweet
	return tweet