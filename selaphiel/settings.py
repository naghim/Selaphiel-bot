import json

class Settings(object):

    def __init__(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        twitter = data['twitter']
        discord = data['discord']
        self.twitter_api_key = twitter['api_key']
        self.twitter_api_secret = twitter['api_secret']
        self.twitter_access_token = twitter['access_token']
        self.twitter_access_secret = twitter['access_secret']
        self.discord_token = discord['token']
        self.discord_channel_ids = discord['channel_ids']
