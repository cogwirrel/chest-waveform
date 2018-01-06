from StringIO import StringIO

import base64, png, urllib2

def to_waveform(url):
    px = [x for x in png.Reader(bytes=urllib2.urlopen(url).read()).read()[2]]
    return map(lambda r: 1 - float(sum(r)) / len(r), zip(*px[0:len(px)/2][::-1]))

def main(event, context):
    url = event.get('params', {}).get('querystring', {}).get('url')
    return to_waveform(url)
