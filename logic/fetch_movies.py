import requests

def fetch_movie_count(name):
    num = 0
    try:
        r = requests.get('https://swapi.co/api/planets?search={}'
                  .format(name)).json()
        if(int(r['count']) > 0):
            num = len(r['results'][0]['films'])
    except Exception as e:
        raise e
    return num