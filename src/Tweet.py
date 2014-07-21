from enum import Enum

class Tweet:

	Polarity = Enum(Positive, Negative, Neutral)
 
	def __init__(self, tweet_id, text, retweet_count, favorited, user_location):
         self.id = tweet_id
         self.text = text
         self.retweet_count = retweet_count
         self.favorited = favorited
         self.user_location = user_location

         self.score = 0
         self.num_pos = 0
         self.num_neg = 0
         self.pos_words = []
         self.neg_words = []
         self.tweet_polarity = Polarity.Neutral


    def calculate_tweet_score():
        return self.num_pos()/float(self.num_pos + self.num_neg)


    def parse_tweet():


    def is_positive(word):
        if word in sentiment_dict: 
            if sentiment_dict[word]["Positiv"] != '': 
                return True
        else:
            new_word = word +"#" + str(1)
                if new_word in sentiment_dict:
                    if sentiment_dict[new_word]["Positiv"] != '': 
                        return True
        return False

     def is_negative(word):
        if word in sentiment_dict: 
            if sentiment_dict[word]["Negativ"] != '': 
                return True
        else:
            new_word = word +"#" + str(1)
                if new_word in sentiment_dict:
                    if sentiment_dict[new_word]["Negativ"] != '': 
                        return True
        return False