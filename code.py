import urllib2
import re
from bs4 import BeautifulSoup



html = urllib2.urlopen('http://www.cogolabs.com').read()

print html

# Extract all email addresses present in html

# 1. Regex matching
m = re.findall(r'\S+@\S+\.(?:(?:com)|(?:net))', html)
print m