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


    def calculate_tweet_store():


    def parse_tweet():