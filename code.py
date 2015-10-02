from bs4 import BeautifulSoup
import re
import urllib2
from sys import argv

script, filename = argv


html = urllib2.urlopen("http://" + filename).read()


soup = BeautifulSoup(html, "html.parser") #Don't know why we need "html.parser". I am just putting this to get rid of the warning sign

text = soup.get_text()

print text

results = soup('a')

print "These are the following e-mails that were retrieved in this following site: %s" %filename
for tag in results:
	if re.match(r'\S+@\S+.com|net', tag['href']):
		print tag['href']



# '\S+@\S+\.(?:(?:com)|(?:net))'

# '[^@]+@[^@]+\.[^@]+'