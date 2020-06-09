import feedparser
import pandas as pd
from bs4 import BeautifulSoup

sources = ['https://www.zdnet.com/topic/security/rss.xml',
'https://www.databreaches.net/feed/', 'https://threatpost.com/feed/',
'https://www.kaspersky.com/blog/feed/',
#'https://www.theregister.co.uk/security/headlines.atom',
'https://www.securitylab.ru/_Services/Export/RSS/news/',
'https://motherboard.vice.com/en_us/rss', 'https://theintercept.com/feed/?lang=en',
'https://www.bleepingcomputer.com/feed/', 'http://feeds.feedburner.com/TheHackersNews?format=xml',
'https://www.ghacks.net/feed/', 'https://www.cyberscoop.com/feed/',
'https://www.darkreading.com/rss_simple.asp', 'https://www.securitymagazine.com/rss/topic/2236-cyber-security-news',
'https://www.infosecurity-magazine.com/rss/news/',
'http://feeds.trendmicro.com/TrendMicroSimplySecurity',
'https://portswigger.net/daily-swig/rss', 'http://www.cbronline.com/feed',
'https://www.forbes.com/cybersecurity/feed/',
'https://feeds.feedburner.com/HaveIBeenPwnedLatestBreaches',
'https://eugene.kaspersky.ru/feed/', 'https://www.digitaltrends.com/feed/',
'https://www.theverge.com/rss/index.xml', 'https://www.engadget.com/rss.xml',
'https://www.slashgear.com/feed/']

news_list = []

for source in sources:
    feed = feedparser.parse(source)
    if len(feed.entries) > 20:
        for i in range(0, 20):
            news = {}
            news['title'] = feed.entries[i].title
            news['date'] = feed.entries[i].published
            news['URL'] = feed.entries[i].link
            news['summary'] = BeautifulSoup(feed.entries[i].summary, "lxml").text
            if 'data' in news['summary']:
                news['topic'] = 'data issues'
            elif 'phishing' in news['summary']:
                news['topic'] = 'phishing'
            elif 'vulnerability' in news['summary']:
                news['topic'] = 'vulnerabilities'
            else:
                news['topic'] = 'other'
            news_list.append(news)
    else:
        for i in range(0, len(feed.entries)):
            news = {}
            news['title'] = feed.entries[i].title
            news['date'] = feed.entries[i].published
            news['URL'] = feed.entries[i].link
            news['summary'] = BeautifulSoup(feed.entries[i].summary, "lxml").text
            if 'data' in news['summary']:
                news['topic'] = 'data issues'
            elif 'phishing' in news['summary']:
                news['topic'] = 'phishing'
            elif 'vulnerability' in news['summary']:
                news['topic'] = 'vulnerabilities'
            else:
                news['topic'] = 'other'
            news_list.append(news)

all_news = pd.DataFrame(news_list)
all_news.to_csv('secnews.csv')
