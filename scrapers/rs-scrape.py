from BeautifulSoup import BeautifulSoup, SoupStrainer
import urllib2
import re
import cPickle
from os import system

base="http://www.rollingstone.com/music/songreviews/"

reviews = []
more_pages = []


def get_review_links(base_url):
    request = urllib2.Request(base_url)
    response = urllib2.urlopen(request)
    links = SoupStrainer('a',{'title': ''})
    linksNoAttr = SoupStrainer(lambda name, attrs: name == 'a' and len(attrs) == 1)
    soup = BeautifulSoup(response.read(), parseOnlyThese=linksNoAttr)
    for y in soup:
        if y.has_key('href') and 'songreviews' in y['href']:
            reviews.append(base+y['href'])
    return reviews

def get_all_review_links():
    all_pages = []
    all_review_links = []
    # this gets like waaay too many repeated links.  But I can
    # sort|uniq them after
    for i in range(1, 50):
        all_pages.append(base+"?page=%d" % i)
    f = open('rs_reviews', 'w')
    for a in all_pages:
        x = get_review_links(a)
        for link in x:
            f.write(link)
            f.write('\n')
    f.close()
    system("sort rs_reviews | uniq > rs_links")

def get_review_data(base_url):
    request = urllib2.Request(base_url)
    response = urllib2.urlopen(request)
    links = SoupStrainer('div',{'itemprop': 'reviewBody'})
    text = response.read()
    parsed = BeautifulSoup(text)
    review = parsed.findAll('div', {'itemprop': 'reviewBody'})
    print review[0].p.text
    title = parsed.findAll('h4', {'itemprop': 'name'})
    print title[0].string
    artist = parsed.findAll('a', {'itemprop': 'name'})
    print artist[0].string

get_review_data("http://www.rollingstone.com/music/songreviews/stray-heart-20121028")
