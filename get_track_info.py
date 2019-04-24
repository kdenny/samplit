import requests
from pprint import pprint
import base64 as b64
import json

def do_auth():
    u = 'https://accounts.spotify.com/api/token'

    data = {
        'grant_type': 'client_credentials'
    }
    cl = {
        'client_id': '7568b9fd0cbb44958ba19d038ff51d05',
        'client_secret': '453d007f79704d27a4b8befcf6a02602'
    }
    g = b64.b64encode(cl['client_id'] + ':' + cl['client_secret'])
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'authorization': 'Basic ' + g
    }


    r = requests.post(u, data=data, headers=headers)
    print(r.text)
    j = json.loads(r.text)
    headers['authorization'] = 'Bearer ' + j['access_token']

    return headers


def get_track(headers, track_id):
    u = 'https://api.spotify.com/v1/audio-analysis/' + str(track_id)
    r = requests.get(u, headers=headers)
    j = json.loads(r.text)
    fname = track_id + '.json'
    with open(fname, 'wb') as ofile:
        json.dump(j, ofile)
    print(j.keys())
    sections = j['sections']
    pprint(sections)

def parse_uri_from_link(link):
    l = 'https://open.spotify.com/track/6Rqn2GFlmvmV4w9Ala0I1e?si=CJxz9MDvTZyxxZP4Gl5etA'
    if '/track/' in link:
        u1 = link.split('/track/')[1]
        if '?' in u1:
            return u1.split('?')[0]
        else:
            return u1



headers = do_auth()
link = 'https://open.spotify.com/track/6Rqn2GFlmvmV4w9Ala0I1e?si=CJxz9MDvTZyxxZP4Gl5etA'
uri = parse_uri_from_link(link)
get_track(headers, uri)