import os,praw,requests,random
from pytube import YouTube
from dotenv import load_dotenv
load_dotenv()


REDDIT_CLIENT_ID = os.getenv("reddit_client_id")
REDDIT_CLIENT_SECRET = os.getenv("reddit_client_secret")
REDDIT_CLIENT_USERNAME = os.getenv("reddit_username")
REDDIT_CLIENT_PASSWORD = os.getenv("reddit_password")
REDDIT_CLIENT_USER_NAME = os.getenv("subreddit_name")
YOUTUBE_CLIENT_API = os.getenv('youtube_api_key')
REDDIT_CLIENT_SUBREDDIT_POST_LIST = [
    "gaming", 
    "SmallYTChannel", #gaming
    "youtube", #promotion
    "YouTubeSubscribeBoost",
]

channel_url = 'https://youtu.be/DhAJeQRyi6M'

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    username=REDDIT_CLIENT_USERNAME,
    password=REDDIT_CLIENT_PASSWORD,
    user_agent='YourBotUserAgent'
)

titles=[
    "Unleash Your Creativity: Discover GameNoShame's Latest Masterpiece!",
    "🚀 Get Ready for a Journey with GameNoShame - New Video Alert!",
    "GameNoShame Presents: The Ultimate Guide to Best Gaming",
    "🔥 Don't Miss Out! GameNoShame's Hot New Release - Watch Now!",
    "Epic Adventures Await - Dive into Best Gaming with GameNoShame",
    "📢 Calling All Best Gaming Enthusiasts! GameNoShame Has You Covered!",
    "GameNoShame's Exclusive Premiere - Be the First to Watch!",
    "Discover Hidden Gems: GameNoShame's Latest Video on Best Gaming",
    "🌟 Experience GameNoShame's Magic - New Video Alert!",
    "Ready for a Best Gaming Extravaganza? GameNoShame Delivers!",
]

descriptions = [
    "Discover the secrets to boosting your Reddit karma effortlessly!",
    "Join the discussion on the hottest topics in town!",
    "Unleash your creativity with these captivating Reddit posts.",
    "Get ready to be amazed by the latest viral content!",
    "Don't miss out on these mind-blowing Reddit stories!",
    "Explore a world of knowledge and entertainment on Reddit.",
    "Elevate your Reddit game with these attention-grabbing posts.",
    "Prepare to be entertained - Reddit style!",
    "Experience the best of Reddit's diverse communities.",
    "Join the Reddit revolution with these must-see posts!",
]

for i in REDDIT_CLIENT_SUBREDDIT_POST_LIST:
    print(i)
    try:
        title = random.choice(titles)
        print(title)
        description = random.choice(descriptions)
        print(description)
        for template in reddit.subreddit(i).flair.link_templates:
            if i == "gaming":
                try:
                    subreddit = reddit.subreddit(i)
                    subreddit.submit(
                        title=title,
                        # url=channel_url,
                        selftext=channel_url+description,
                        # flair_id=template["id"]
                    )
                    print(f"{i} Fulfiled --------------->")
                except Exception as error:
                    print(error,"------------->")
                    print(i,' dosen\'t full fill request')
            if i=="SmallYTChannel" and template["text"]=="Gaming":
                try:
                    subreddit = reddit.subreddit(i)
                    subreddit.submit(
                        title=title,
                        # url=channel_url,
                        selftext=channel_url+description,
                        flair_id=template["id"]
                    )
                    print(f"{i} Fulfiled --------------->")
                except Exception as error:
                    print(error,"------------->")
                    print(i,' dosen\'t full fill request')
            if i=="youtube" and template["text"]=="Promotion":
                try:
                    subreddit = reddit.subreddit(i)
                    subreddit.submit(
                        title=title,
                        # url=channel_url,
                        selftext=channel_url+description,
                        flair_id=template["id"]
                    )
                    print(f"{i} Fulfiled --------------->")
                except Exception as error:
                    print(error,"------------->")
                    print(i,' dosen\'t full fill request')
            if i=="YouTubeSubscribeBoost" and template["text"]=="Subscribe!:upvote:":
                try:
                    subreddit = reddit.subreddit(i)
                    subreddit.submit(
                        title=title,
                        # url=channel_url,
                        selftext=channel_url+description,
                        flair_id=template["id"]
                    )
                    print(f"{i} Fulfiled --------------->")
                except Exception as error:
                    print(error,"------------->")
                    print(i,' dosen\'t full fill request')
    except:
        print(f"Can't Find {i} Tags")



