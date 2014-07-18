import csv
import re
import sys

def get_sentiment_dictionary():
	sentiment_file = open("../data/inquirerbasic.csv", 'rU')
	return csv.DictReader(sentiment_file)


def import_tweets():
	tweet_dictionary = dict()
	raw_tweets = open("../data/tweets.txt", 'r')
	for line in raw_tweets:
		hashtag = line[:line.find(" ")]
		full_tweets = line[line.find(" ")+1:]
		final_tweets = []
		for tweet in full_tweets.split("||"):
			if tweet != '': final_tweets.append(curate_line(tweet))
		tweet_dictionary[hashtag.lower()] = final_tweets
	return tweet_dictionary
	



def get_tweets(hashtag="#mh17"):
	hashtag = hashtag.lower()
	tweets = import_tweets()
	return tweets[hashtag]
	

def curate_line(tweet):
	return re.sub('[^\ \w]', '', tweet)
	


"""
commandline interface takes a directory name and gold file.
It then processes each file within that directory and extracts any
matching e-mails or phone numbers and compares them to the gold file
"""
if __name__ == '__main__':
    get_tweets()