from pytube import YouTube,Channel

def get_latest_video(channel_url):
    try:
        channel = Channel(channel_url)
        latest_video = channel.videos
        return latest_video
    except Exception as e:
        return str(e)

# Replace 'CHANNEL_URL' with the URL of the channel you want to track.
channel_url = 'https://www.youtube.com/@GameNoShame'
latest_video_url = get_latest_video(channel_url)
print("Latest video URL:", latest_video_url)

# from pytube import Channel

# def get_latest_video(channel_url):
#     try:
#         channel = Channel(channel_url)
#         latest_video = channel.video_urls[0]
#         return latest_video
#     except Exception as e:
#         return str(e)

# # Example usage:
# channel_url = "https://www.youtube.com/c/ChannelName"
# latest_video_link = get_latest_video(channel_url)
# print("Latest Video Link:", latest_video_link)
