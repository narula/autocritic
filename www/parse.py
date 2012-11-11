
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
    return results
