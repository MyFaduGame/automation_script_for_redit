import os,praw,requests,random
from pytube import YouTube
from dotenv import load_dotenv
load_dotenv()


def Reddit_Post_Function(Video_URL:str,type_of_game:str):
    #Credentials are Declared HERE
    REDDIT_CLIENT_ID = os.getenv("reddit_client_id")
    REDDIT_CLIENT_SECRET = os.getenv("reddit_client_secret")
    REDDIT_CLIENT_USERNAME = os.getenv("reddit_username")
    REDDIT_CLIENT_PASSWORD = os.getenv("reddit_password")
    
    #Reddit Instance
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        username=REDDIT_CLIENT_USERNAME,
        password=REDDIT_CLIENT_PASSWORD,
        user_agent='YourBotUserAgent'
    )
    #Chat GPT Latest TITLEs
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
    if type_of_game == "bgmi":
        for template in reddit.subreddit("BGMI").flair.link_templates:
            if template['text']=="🎮 Gameplay":
                flair_id_template = template['id']
        reddit.subreddit('bgmi').submit(
            title=random.choice(titles),
            url = Video_URL,
            flair_id=flair_id_template
        )
    reddit.subreddit('videos').submit(
        title=random.choice(titles),
        url = Video_URL
    )
    print("Post Uploaded into r/videos")

    for template in reddit.subreddit("SmallStreamers").flair.link_templates:
        if template["text"]=="Video":
            flair_id_template = template['id']
    reddit.subreddit('SmallStreamers').submit(
        title=random.choice(titles),
        selftext=random.choice(descriptions)+"\nSubscribe to GameNoShame for more Content",
        flair_id=flair_id_template
    )
    print("Post uploaded into r/smallstreamers")

    for template in reddit.subreddit("gaming").flair.templates:
        if template["text"]=="PC":
            flair_id_template = template['id']
    reddit.subreddit('gaming').submit(
        title=random.choice(titles),
        selftext=Video_URL+" "+random.choice(descriptions),
        # flair_id=flair_id_template
    )
    print("Post is Published on Gaming Reddit")

    if "twich.tv" in Video_URL:
        reddit.subreddit('LivestreamFail').submit(
            title=random.choice(titles),
            selftext=Video_URL+" "+random.choice(descriptions)
        )
        print("Post is Published on LivestreamFail")
        reddit.subreddit('LivestreamFails').submit(
            title=random.choice(titles),
            url=Video_URL
        )
        print("Post is Published on LivestreamFails")

    for template in reddit.subreddit("NewTubers").flair.link_templates:
        if template['text'] == "COMMUNITY":
            flair_id_template = template['id']
    reddit.subreddit('NewTubers').submit(
        title=random.choice(titles),
        selftext=random.choice(descriptions)+"\n Subscribe to GameNoShame on yt",
        flair_id=flair_id_template
    )


    for template in reddit.subreddit("youtube").flair.link_templates:
        if template["text"]=="Promotion":
            flair_id_template = template['id']
    reddit.subreddit('youtube').submit(
        title=random.choice(titles),
        selftext=random.choice(descriptions)+"\n Subscribe to GameNoShame for more Information",
        flair_id=flair_id_template
    )
    print("Post is Published on youtube")

    for template in reddit.subreddit("YouTubeSubscribeBoost").flair.link_templates:
        if template["text"]=="Subscribe!:upvote:":
            flair_id_template=template['id']
    reddit.subreddit('YouTubeSubscribeBoost').submit(
        title=random.choice(titles),
        url=Video_URL,
        flair_id=flair_id_template
    )
    print("Post is published on YouTubeSubscriberBoost")

    reddit.subreddit('IndianGaming').submit(
        title=random.choice(titles),
        url=Video_URL
    )
    print("Post is Published in IndianGaming")

    '''
    NewTubers
    Promote_Your_Channel
    SmallStreamers
    SmallStreams
    '''

video_url = input("enter your Video URL:- ")
type_of_game = input("Enter the type of game:- ")
Reddit_Post_Function(Video_URL=video_url,type_of_game=type_of_game)
