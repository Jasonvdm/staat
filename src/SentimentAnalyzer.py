import ImportData
import sys


def analyze_topic(topic):
	sentiment_dict = ImportData.get_sentiment_dictionary()
	topic = "#"+topic
	tweets = ImportData.get_tweets(topic)
	num_pos = 0;
	total_num_words = 0;
	for tweet in tweets:
		for word in tweet:
			total_num_words+=1
			if "Positiv" in sentiment_dict[word]: num_pos+=1
	return num_pos/total_num_words

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print 'usage:\tSpamLord.py <topic>'
        sys.exit(0)
    analyze_topic(sys.argv[1])