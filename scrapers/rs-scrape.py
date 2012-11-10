from BeautifulSoup import BeautifulSoup, SoupStrainer
import urllib2
import re
import cPickle
from os import system

base="http://www.rollingstone.com"
songreviews = base + "/music/songreviews"

reviews = []
more_pages = []


def get_review_links(base_url):
    request = urllib2.Request(base_url)
    try:
        response = urllib2.urlopen(request)
    except:
        return None
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
        all_pages.append(songreviews+"?page=%d" % i)
    f = open('rs_reviews', 'w')
    for a in all_pages:
        x = get_review_links(a)
        for link in x:
            f.write(link)
            f.write('\n')
    f.close()
    system("sort rs_reviews | uniq > rs_links")

def get_review_data(base_url):
    one = {}
    request = urllib2.Request(base_url)
    try:
        response = urllib2.urlopen(request)
    except:
        return None
    links = SoupStrainer('div',{'itemprop': 'reviewBody'})
    text = response.read()
    parsed = BeautifulSoup(text)
    review = parsed.findAll('div', {'itemprop': 'reviewBody'})
    one['review'] = review[0].p.text
    title = parsed.findAll('h4', {'itemprop': 'name'})
    one['title'] = title[0].string.replace('&quot;', '')
    artist = parsed.findAll('a', {'itemprop': 'name'})
    if not len(artist):
        artist = parsed.findAll('span', {'itemprop': 'name'})
    if not len(artist):
        print "FAIL!"
        print base_url
        exit()
    one['artist'] = artist[0].string
    return one

def generate_review_text(fn, out):
    f = open(fn, 'r')
    o = open(out, 'w')
    for url in f.readlines():
        print "Processing... ", url.strip()
        one = get_review_data(url)
        if one:
            try:
                o.write("%s\n%s\n%s\n\n" % (one['artist'].encode('utf-8'), one['title'].encode('utf-8'), one['review'].encode('utf-8')))
            except:
                print "FAIL!"
                print url, one
                continue

if __name__ == "__main__":
    #get_all_review_links()
    generate_review_text('rs_links', 'rs_review_text')
    #print get_review_data("http://www.rollingstone.com/music/songreviews/stray-heart-20121028")
    #print get_review_data("http://www.rollingstone.com/music/songreviews/am-fm-20100714")
