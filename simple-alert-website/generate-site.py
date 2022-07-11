import feedparser;

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
f.write ("  <body>" + "\n")

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
    f.write ("<h2>" + d.entries[i].title                + "</h2>\n")
    f.write ("<p>"  + d.entries[i].published            + "</p>\n")
    f.write ("<p>"  + d.entries[i].summary_detail.value + "</p>\n")
    i += 1



f.write ("  </body>" + "\n")
f.write ("</html>" + "\n")

f.close()