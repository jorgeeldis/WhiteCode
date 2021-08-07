import urllib.request
import re
import webbrowser


search_keyword = input("Lets see whats you favorite song? ")
html = urllib.request.urlopen(
    "https://www.youtube.com/results?search_query=" + search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
url = "https://www.youtube.com/watch?v=" + video_ids[0]
webbrowser.open(url)
