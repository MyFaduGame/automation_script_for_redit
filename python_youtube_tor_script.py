from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from stem import Signal
from stem.control import Controller
import time

# Function to start Tor
def start_tor():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="your_password")
        controller.signal(Signal.NEWNYM)

# Function to open Tor Browser using Selenium
def open_tor_browser():
    options = Options()
    options.binary_location = "D:\\Tor\\Tor Browser\\Browser\\firefox.exe"
    # proxy = Proxy()
    # proxy.proxy_type = ProxyType.MANUAL
    # proxy.http_proxy = "127.0.0.1:9150"
    # proxy.socks_proxy = "127.0.0.1:9150"
    # proxy.ssl_proxy = "127.0.0.1:9150"

    options.add_argument("--headless")  # Optional: Run in headless mode
    options.add_argument("--no-sandbox")  # Optional: Disable sandbox for headless mode
    options.add_argument("--disable-dev-shm-usage")  # Optional: Disable shared memory for headless mode
    options.add_argument("--disable-gpu")  # Optional: Disable GPU for headless mode

    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.socks", "127.0.0.1")
    profile.set_preference("network.proxy.socks_port", 9150)

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                               options=options, firefox_profile=profile)
    return driver

# Function to search for a YouTube channel and play a video
def search_and_play_youtube():
    driver = open_tor_browser()
    driver.get("https://www.youtube.com")

    # Replace 'YourChannel' with the channel you want to search for
    search_query = "GameNoShame"
    search_box = driver.find_element_by_name("search_query")
    search_box.send_keys(search_query)
    search_box.submit()
    time.sleep(5)  # Wait for search results to load

    # Click on the channel name in search results
    channel_link = driver.find_element_by_xpath("//a[@class='style-scope ytd-channel-renderer']")
    channel_link.click()
    time.sleep(5)  # Wait for the channel page to load

    # Click on the first video in the channel
    video_link = driver.find_element_by_xpath("//a[@id='video-title']")
    video_link.click()

    # Keep the script running for video playback
    input("Press Enter to exit and stop playback...")
    driver.quit()

if __name__ == "__main__":
    start_tor()
    search_and_play_youtube()
