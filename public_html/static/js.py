import json

data = [{"title": "Shyam Varshik Mahotsav", "start": "2019-12-15T09:00", "end": "2019-12-15T23:00"},
 {"title": "Shyam Satsang Mandal Website Launch", "start": "2019-12-15T20:00", "end": "2019-12-15T20:30"},
 {"title": "Shukla Paksh Ekadashi", "start": "2019-08-11T08:00", "end": "2019-08-11T22:00"}]

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)