import cPickle

def parse_sample():
    f = open("sample.txt", 'r')
    results = []
    count = 0
    artist = ""
    title = ""
    review = ""
    for y in f.readlines():
        x = y.rstrip();
        if count % 3 == 0:
            artist = x
        elif count % 3 == 1:
            title = x
        elif count % 3 == 2:
            review = x
            results.append({'artist' : artist, 'title' : title, 'review' : review, 'image' : "static/img/slide-04.jpg"})
        count = count + 1
    res = cPickle.dumps(results)
    out = open('sample_out.txt', 'w')
    out.write(res)
    return results

def get_results():
    f = open('sample_out.txt', 'r')
    results = cPickle.loads(f.read())
    return results[:20]

if __name__ == "__main__":
    parse_sample()
    
