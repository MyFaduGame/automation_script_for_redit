import requests
from bs4 import BeautifulSoup

def get_latest_video_url(channel_url):
    try:
        # Send a GET request to the channel's URL
        response = requests.get(channel_url)
        response.raise_for_status()

        # Parse the HTML content of the channel page
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        # Find the element containing the latest video link
        latest_video_link = soup.find('a', {'id': 'video-title'})
        print(latest_video_link)

        if latest_video_link:
            return "https://www.youtube.com" + latest_video_link['href']
        else:
            return "Latest video link not found."

    except requests.exceptions.RequestException as e:
        return str(e)
    except Exception as e:
        return str(e)

# Example usage:
channel_url = "https://www.youtube.com/c/GameNoShame"
latest_video_url = get_latest_video_url(channel_url)
print("Latest Video URL:", latest_video_url)
