import os,praw
from googleapiclient.discovery import build

REDDIT_CLIENT_ID = os.environ.get("reddit_client_id")
REDDIT_CLIENT_SECRET = os.environ.get("reddit_client_secret")
REDDIT_CLIENT_USERNAME = os.environ.get("reddit_username")
REDDIT_CLIENT_PASSWORD = os.environ.get("reddit_password")
REDDIT_CLIENT_USER_NAME = os.environ.get("subreddit_name")
REDDIT_CLIENT_SUBREDDIT_POST_LIST = [
    "gaming", 
    "SmallYTChannel", #gaming
    "youtube", #promotion
    "YouTubeSubscribeBoost",
]


# import praw

# # Authenticate with Reddit
# reddit = praw.Reddit(
#     client_id='YOUR_CLIENT_ID',
#     client_secret='YOUR_CLIENT_SECRET',
#     username='YOUR_REDDIT_USERNAME',
#     password='YOUR_REDDIT_PASSWORD',
#     user_agent='YourApp by /u/YourRedditUsername'
# )

# # Authenticate with YouTube API
# youtube_api_key = 'YOUR_YOUTUBE_API_KEY'
# youtube = build('youtube', 'v3', developerKey=youtube_api_key)

# # Fetch the latest video URL from your YouTube channel
# channel_id = 'YOUR_YOUTUBE_CHANNEL_ID'
# playlist_id = 'YOUR_YOUTUBE_PLAYLIST_ID'

# playlist_items = youtube.playlistItems().list(
#     part='snippet',
#     playlistId=playlist_id,
#     maxResults=1,
# ).execute()

# latest_video = playlist_items['items'][0]['snippet']
# video_title = latest_video['title']
# video_url = f"https://www.youtube.com/watch?v={latest_video['resourceId']['videoId']}"

# # Submit the post on Reddit with the desired flair name
# subreddit = reddit.subreddit('YOUR_SUBREDDIT_NAME')
# subreddit.submit(
#     title=video_title,
#     url=video_url,
#     flair_id=None,  # Set to None
#     flair_text='Your Flair Name'  # Specify the flair name here
# )
