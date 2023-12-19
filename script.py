import tweepy
import facebook

# Twitter and Facebook Account Credentials
TWITTER_CONSUMER_KEY = "28191312"
TWITTER_CONSUMER_SECRET = "****smb889"
TWITTER_ACCESS_TOKEN = "1736947871004708864-ZYNiXiK8WVuSZchAbulvCMtG98HaAG"
TWITTER_ACCESS_TOKEN_SECRET = "P2J0ZAt0a2edVtxoMl14F4dyeUPDhAc0LG3Do1gP0GkvZ"

FACEBOOK_APP_ID = "7088963741143423"
FACEBOOK_APP_SECRET = "96f36d1b7419a3c655ce155e79441e14"
FACEBOOK_ACCESS_TOKEN = "EABkvXZC2d0X8BO13j2lXvI4MiQUrtP4SiHmdIIZAqZCOEe6CXb8AZAHgqteIb3Bvg3UMsIAMM4HOpozwGxyVLF5RDFNyutuPFnIIaPSvnZAtmOa4iZAyPVu1ZBUaZArJcP6tVwiNjAqzyr6QGZBFxnaPjvMY3O6VR7qVDSh0YFnZB0BXujiZBYtmgPFiRTDr7mLr866Wnl0U21ypoGZBKJWoaI4TfVGjrgofwARidjVZCiMmpEUkBbZA0yRVxvAJyh9YKZBKwZDZD"

# Enter your post content
user_choice = input().upper()

if user_choice == 'Text':
    # User wants to input text
    post_content = input("Enter your text message: ")
elif user_choice == 'picture/video':

    # User wants to upload a picture/video
    post_content = f"Uploaded a picture/video: {file_path}"


# Initialize Twitter API client
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Initialize Facebook Graph API client
graph = facebook.GraphAPI(FACEBOOK_ACCESS_TOKEN)

# Send the post to Twitter
api.update_status(status=post_content)

# Send the post to Facebook
graph.post('/me/feed', message=post_content)

print("Post sent to Twitter and Facebook successfully!")