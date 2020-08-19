import tweepy


auth = tweepy.OAuthHandler("your twitter API key", "your twitter API secret")
auth.set_access_token("your twitter access token", "your twitter access token secret")

api = tweepy.API(auth)


def createtweet() :
    tweet = (input("What would you like to tweet?"))

    print (f"This is your tweet. {tweet}")
    sendtweet = (input("Would you like to send it? y/n\n"))

    if sendtweet == "y" :
        api.update_status (tweet)

    elif sendtweet == "n" :
        loop = False


def homefeed() :
    tweets = api.home_timeline(count = 10)
    for tweet in tweets:
        print('{real_name} (@{name}) said {tweet}\n\n'.format(
            real_name=tweet.author.name, name=tweet.author.screen_name,
            tweet=tweet.text))
    

def finduser() :
    finduser = (input("Enter the username of the person you want to find.\n"))

    user = api.get_user(finduser)
    tweets = api.user_timeline(finduser)
    user.screen_name
    user.name
    for tweet in tweets:
            print(tweet.text)

def listfollowers() :
    followers = api.followers()
    for follower in followers:
        print(follower.screen_name)






