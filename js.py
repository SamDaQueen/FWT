import json

data = (
			{
				'title': 'kuyt967t97t',
				'start': '2019-03-17T13:13',
				'end': '2019-03-17T15:13'
			}
		)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)