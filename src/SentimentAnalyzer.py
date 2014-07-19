import ImportData
import sys


def analyze_topic(topic):
	sentiment_dict = ImportData.get_sentiment_dictionary()
	topic = "#"+topic
	tweets = ImportData.get_tweets(topic)
	num_pos = 0;
	total_num_words = 0;
	for tweet in tweets:
		for word in tweet.split():
			word = word.lower()+"#1"
			if word in sentiment_dict:
				total_num_words+=1	
				print 
				if sentiment_dict[word]["Positiv"] != '':
					print "tes"
				if sentiment_dict[word]["Positiv"] != '': num_pos+=1
	print total_num_words
	print num_pos
	print float(num_pos)/float(total_num_words)
	return 

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print 'usage:\tSpamLord.py <topic>'
        sys.exit(0)
    analyze_topic(sys.argv[1])