import cPickle
import os
import random

def parse_sample():
    f = open("sample.txt", 'r')
    images = os.listdir("static/img/")
    images = filter( lambda x : x.find('.jpg') > 0, images)
    print images
    results = []
    count = 0
    artist = ""
    title = ""
    review = ""
    imgIdx = 0
    for y in f.readlines():
        x = y.rstrip();
        if count % 3 == 0:
            artist = x
        elif count % 3 == 1:
            title = x
        elif count % 3 == 2:
            review = x
            i = images[imgIdx % len(images)]
            results.append({'artist' : artist, 'title' : title, 'review' : review, 'image' : "static/img/%s" % i})
            imgIdx = imgIdx + 1
        count = count + 1
    res = cPickle.dumps(results)
    out = open('sample_out.txt', 'w')
    out.write(res)
    print len(results)
    return results

def get_results():
    results = parse_sample()
    return results

def get_results_cached():
    f = open('sample_out.txt', 'r')
    results = cPickle.loads(f.read())
    return results

if __name__ == "__main__":
    parse_sample()
    
