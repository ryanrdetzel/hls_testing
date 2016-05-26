import time
from urlparse import parse_qs

def application(environ, start_response):
    qs = parse_qs(environ['QUERY_STRING'])
    seq = qs.get('seq')[0]
    delay = qs.get('delay')[0]

    time_delay = float(delay) / 1000
    time.sleep(time_delay)

    if seq == 'fail' or seq == '500':
        start_response('500 Server Error', [('Content-Type', 'text/plain')])
        return ['Not Found']
    if seq == '404':
        start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
        return ['Not Found']

    start_response('302 Moved Permanently', [('Location','http://dxxd.net/hls/gear2/fileSequence' + seq + '.ts')])
    return ""
