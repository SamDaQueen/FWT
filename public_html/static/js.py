import json

data = [
      
      {"title": "Shyam Jhula Mahotsav", "start": "2019-08-04T16:00", "end": "2019-08-04T22:00"},
      {"title": "Shyam Satsang Mandal Website Launch", "start": "2019-08-04T20:00", "end": "2019-08-04T20:30"},
      {"title": "Shukla Paksh Ekadashi", "start": "2019-08-11T08:00", "end": "2019-08-11T22:00"},
    ]

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)