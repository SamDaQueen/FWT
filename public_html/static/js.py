import json

data = [
      {
        'title': 'Event 1',
        'start': '2019-03-19T17:13',
        'end': '2019-03-20T18:13'
      },
      {
        'title': 'Holiday',
        'start': '2019-03-01T18:13',
        'end': '2019-03-25T19:13'
      },
      {
        'title': 'Holis',
        'start': '2019-03-23T18:13',
        'end': '2019-03-23T19:13'
      },
      {
        'title':'FWT Project Subbmission',
        'start': '2019-03-27T18:13',
        'end': '2019-03-27T19:13'
      },
    ]

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)