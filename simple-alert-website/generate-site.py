import feedparser
import re

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

lafd_feed = 'https://www.lafd.org/alerts-rss.xml'
web_file = 'index.html'
max_entries = 100

d = feedparser.parse(lafd_feed)
f = open(web_file,"w")

f.write ("<!DOCTYPE html>" + "\n")
f.write ("<html lang=\"en\">" + "\n")
f.write ("  <head>" + "\n")
f.write ("    <meta charset=\"UTF-8\">" + "\n")
f.write ("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">" + "\n")
f.write ("    <title>LAFD Feed</title>" + "\n")
f.write ("  </head>" + "\n")
f.write ("  <body style=\"font-family:arial;\">" + "\n")

if('title' in d.feed):
    f.write ("<h1>" + d.feed.title + "</h1>\n")
else:
    f.write ("<h1>Title  MISSING</h1>\n")

if('link' in d.feed):
    f.write ("<p>" + d.feed.link + "</p>\n")
else:
    f.write ("<p>Link MISSING</p>\n")

#if('updated' in d.feed):
#    f.write ("<p>Feed Updated: " + d.feed.updated + "</p>\n")
#else:
#    f.write ("<p>Feed Updated: MISSING</p>\n")

if('published' in d.feed):
    f.write ("<p>Feed Published: " + d.feed.published + "</p>\n")
else:
    f.write ("<p>Feed Published: MISSING</p>\n")

i = 0
while i < max_entries:
    try:
        ('title' in d.entries[i])
    except:
        #f.write ("--END-------------------------------------------------------\n")
        break
    #f.write ("------------------------------------------------------------\n")
    f.write ("<! Entry: " + str(i) + ">\n")
    f.write ("<h2>" + striphtml(d.entries[i].title)      + "</h2>\n")
    f.write ("<h3>"  + d.entries[i].published            + "</h3>\n")
    summary_clean = striphtml(d.entries[i].summary_detail.value)
    summary_clean = re.sub(r"http\S+", "", summary_clean)
    summary_clean = re.sub(r"MAP: ", "", summary_clean)
    f.write ("<p>"  + summary_clean + "</p>\n")
    i += 1



f.write ("  </body>" + "\n")
f.write ("</html>" + "\n")

f.close()