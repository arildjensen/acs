import feedparser;

lafd_feed = 'https://www.lafd.org/alerts-rss.xml'

d = feedparser.parse(lafd_feed)

if('title' in d.feed):
    print ("Title.........: ", d.feed.title)
else:
    print ("Title.........: MISSING")

if('link' in d.feed):
    print ("Link..........: ", d.feed.link)
else:
    print ("Link..........: MISSING")

if('updated' in d.feed):
    print ("Feed Updated..: ", d.feed.updated)
else:
    print ("Feed Updated..: MISSING")

if('published' in d.feed):
    print ("Feed Published: ", d.feed.published)
else:
    print ("Feed Published: MISSING")