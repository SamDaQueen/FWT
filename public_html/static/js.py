import json

data = [      
      {
        'title':'Shyam Varshik Mahotsav',
        'start': '2019-12-15T09:00',
        'end': '2019-12-15T23:00'
      },
    ]
print("file run")
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)