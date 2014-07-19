import ImportData
import sys


def analyze_topic(topic):
	sentiment_dict = ImportData.get_sentiment_dictionary()
	tweets = ImportData.pull_tweets(topic)
	num_pos = 0;
	num_neg = 0;
	total_num_words = 0;
	for tweet in tweets:
		has_positive = False
		has_negative = False
		for word in tweet.split():
			word = word.lower()
			if word in sentiment_dict:
				total_num_words+=1	
				if sentiment_dict[word]["Positiv"] != '': 
					num_pos+=1
					has_positive = True
				if sentiment_dict[word]["Negativ"] != '':
					has_negative = True
					num_neg+=1
			else:
				for i in range(2):
					new_word = word +"#" + str(i)
					if new_word in sentiment_dict:
						total_num_words+=1	
						if sentiment_dict[new_word]["Positiv"] != '': 
							num_pos+=1
							has_positive = True
						if sentiment_dict[new_word]["Negativ"] != '': 
							has_negative = True
							num_neg+=1
		if has_positive: 
			print "Positive: " + tweet + "\n"
		if has_negative: 
			print "Negative: " + tweet + "\n"

	print num_neg
	print num_pos
	print float(num_pos)/float(num_neg + num_pos)
	return 

if __name__ == '__main__':
	if (len(sys.argv) < 2):
	    print 'usage:\tSpamLord.py <topics>'
	    sys.exit(0)
	topic = ""
	for i in range(1,len(sys.argv)):topic += " #" + sys.argv[i]
	topic = topic[1:]
	print topic
	analyze_topic(topic)