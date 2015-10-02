from bs4 import BeautifulSoup
import re
import urllib2
from sys import argv

def extract_emails_from_text(text):
  addresses = list()
  for word in text.split(' '):
    addresses += re.findall(r'[a-z]+[A-Za-z0-9._%+-]+@\S+\.com', word)
    
  return addresses
  

script, filename = argv

html = urllib2.urlopen("http://" + filename).read()
soup = BeautifulSoup(html, "html.parser") #Don't know why we need "html.parser". I am just putting this to get rid of the warning sign
all_text = soup.get_text(' ')
email_addresses = extract_emails_from_text(all_text)

for link in soup.find_all('a'):
    try:
      html = urllib2.urlopen(link.get('href')).read()
      soup = BeautifulSoup(html, "html.parser")
      text = soup.get_text(' ')
      email_addresses += extract_emails_from_text(text)
    except:
      pass

print "These are the following e-mails that were retrieved in this following site: %s" %filename

for email in set(email_addresses):
  print email