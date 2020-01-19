import unidecode as u
import datetime
import requests


def get_safe_web_name(web_name):
    '''remove accents and casing from web name'''
    return u.unidecode(web_name).lower()


def update_return_dict(d, k, v):
    '''update and return a dictionary'''
    if not (isinstance(k, list) and isinstance(v, list) and len(k) == len(v)):
        raise Exception

    for i in range(0, len(k)):
        d[k[i]] = v[i]
    return d


def get_dict_keys(d, k):
    '''filter dictionary for relevant keys'''
    if not (isinstance, k, list):
        raise Exception
    arr = []
    for i in k:
        arr.append((i, d[i]))

    return dict(arr)


def check_next_event_deadlinetime():
    bootstrap_request = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
    events = bootstrap_request.json()['events']

    deadlinetime_str = [i for i in events if i['is_next']][0]['deadline_time']
    deadlinetime = datetime.datetime.strptime(deadlinetime_str, '%Y-%m-%dT%H:%M:%SZ')

    return deadlinetime < datetime.datetime.now() + datetime.timedelta(hours=24)
