import praw,os
from praw.models.reddit.subreddit import SubredditFlairTemplates
# print(os.environ.get("reddit_client_id"))

reddit_client_id='VF8oKEBuP6lkW-3Fl8ukqg'
reddit_client_secret='SkIODwzOxAgNyrDEoGudfdNxSiw6lQ'
reddit_username='OkBusiness5364'
reddit_password='9376319931@N6a2v8i4n6'
subreddit_name='r/GetMoreViewsYT'

# Authenticate with Reddit API
reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    username=reddit_username,
    password=reddit_password,
    user_agent='YourBotUserAgent'
)

subreddit_name=["r/IndianGaming","r/SmallYTChannel",""]

# Create a new Reddit post
subreddit = reddit.subreddit("r/youtube")

# for subreddit in reddit.user.contributor_subreddits(limit=None):
#     print(str(subreddit))
    
# for subreddit in reddit.user.moderator_subreddits(limit=None):
#     print(str(subreddit))


# preferences = reddit.user.preferences()
# print(preferences["show_link_flair"])

# for subreddit in reddit.user.subreddits(limit=None):
#     print(str(subreddit))

list_of_reddits = reddit.user.subreddits(limit=None)

# for reddit_name in list_of_reddits:
#     print(reddit_name,'----------------->')
#     try:
#         for template in reddit.subreddit("IndianGaming").flair.templates:
#             # if reddit_name=="IndianGaming":
#             print(template['text']+"———————>"+template['id'])
#             # pass
#     except:
#         print("No Flair Found")

for template in reddit.subreddit("gaming").flair.templates:
    print(template)




############################### TRY AND ERROR PART This many Time this script dosent work ##################################


# for template in reddit.subreddit("youtube").flair.templates:#.user_selectable():
#     print(template["id"])
#     template_id = template["id"]
    

# subreddit_flair_instance = subreddit.flair.templates
# print(subreddit_flair_instance,type(subreddit_flair_instance))
# print(dict(subreddit_flair_instance))


# flairs = list(reddit.subreddit("r/youtube").flair.templates)[0]

# for flair in subreddit.flair.templates:
#     print(flair['text'])

# print(flairs)

# subreddit.submit(
#     title='Valorant new short is live now',
#     url="https://youtube.com/shorts/yuDuaT-7_tw?feature=share",
#     flair_id=template_id,  # Set to None
#     flair_text=None
# )


# flair_templates = subreddit.flair.link_templates

# print(flair_templates)

# for template in flair_templates:
    # print(template)
    # print(f"Flair Template ID: {template['id']}")
    # print(f"Flair Template Name: {template['text']}")
    # print("-" * 50)

# title = "New YouTube Video!"
# video_link = "https://www.youtube.com/shorts/4XvuWG91zgQ"

# # Submit the post
# submission = subreddit.submit(title, url=video_link)
# print("Reddit post created:", submission.shortlink)
