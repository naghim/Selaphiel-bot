from selaphiel.settings import Settings
import discord
import tweepy

TWITTER_MAX_LENGTH = 280

settings = Settings('settings.json')

twitter = tweepy.Client(
   consumer_key=settings.twitter_api_key, consumer_secret=settings.twitter_api_secret,
   access_token=settings.twitter_access_token, access_token_secret=settings.twitter_access_secret
)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def split_tweet(content):
    contents = []

    while content:
        contents.append(content[:TWITTER_MAX_LENGTH])
        content = content[TWITTER_MAX_LENGTH:]
    
    return contents

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.channel.id not in settings.discord_channel_ids:
        return

    content = f'{message.content} ({message.author.global_name})'
    contents = split_tweet(content)
    
    for content in contents:
        result = twitter.create_tweet(text=content)
        print(result)

client.run(settings.discord_token)
