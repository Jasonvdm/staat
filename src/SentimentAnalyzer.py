import ImportData
import sys


def analyze_topic(topic):
	sentiment_dict = ImportData.get_sentiment_dictionary()
	topic = "#"+topic
	tweets = ImportData.get_tweets(topic)
	num_pos = 0;
	total_num_words = 0;
	for tweet in tweets:
		has_positive = False
		for word in tweet.split():
			word = word.lower()
			if word in sentiment_dict:
				total_num_words+=1	
				if sentiment_dict[word]["Positiv"] != '': 
					num_pos+=1
					has_positive = True
					print word
			else:
				for i in range(10):
					new_word = word +"#" + str(i)
					if new_word in sentiment_dict:
						total_num_words+=1	
						if sentiment_dict[new_word]["Positiv"] != '': 
							num_pos+=1
							has_positive = True
							print new_word
		if has_positive: print tweet
	print total_num_words
	print num_pos
	print float(num_pos)/float(total_num_words)
	return 

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print 'usage:\tSpamLord.py <topic>'
        sys.exit(0)
    analyze_topic(sys.argv[1])