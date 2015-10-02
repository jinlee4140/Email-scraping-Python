from bs4 import BeautifulSoup
import re
import urllib2
from sys import argv

script, filename = argv

html = urllib2.urlopen("http://" + filename).read()

soup = BeautifulSoup(html, "html.parser") #Don't know why we need "html.parser". I am just putting this to get rid of the warning sign

all_text = soup.get_text(' ')
all_words = all_text.split(' ')

# print all_words
email_addresses = list()

for word in all_words:
  email_addresses += re.findall(r'\S+@\S+.com|net', word)

print "These are the following e-mails that were retrieved in this following site: %s" %filename

# print set(email_addresses)
print set(email_addresses)