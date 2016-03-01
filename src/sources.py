import feedparser
import requests
from bs4 import BeautifulSoup
from .parser import valid_anchor

active_sources = []
active_feeds = []

class Source:

    def __init__(self, name, base_url, active=True):
        self.name = name
        self.url = base_url
        self.active = active

    def add(self, feed_url, active=True):
        """
        Add a feed to this source
        :param feed_args:
        :return:
        """

        if active and self.active:
            url = feed_url.get('href')
            # append the path to the domain name if this isn't a full domain name
            if 'http' not in url:
                url = self.url + url
            feed = feedparser.parse(url)

            if feed not in active_feeds:
                active_feeds.append(feed)

    def scan(self):
        """
        Searches the base url for rss feed links and adds them all
        :return: None
        """
        request = requests.get(self.url)
        soup = BeautifulSoup(request.content, "html.parser")

        for anchor in soup.find_all('a'):
            if valid_anchor(anchor):
                self.add(anchor)


# cnn = Source("CNN", "http://rss.cnn.com/rss/", active=False)
# cnn.add("cnn_allpolitics.rss")
# cnn.add("cnn_topstories.rss")
# cnn.add("cnn_us.rss")

# usnews = Source("US News and World Report", "http://www.usnews.com/")
# usnews.add("blogrss/data-mine")

cnn = Source("CNN", "http://www.cnn.com/services/rss/")
cnn.scan()

usnews = Source("US News and World Report", "http://www.usnews.com/info/features/rss-feeds")
usnews.scan()
