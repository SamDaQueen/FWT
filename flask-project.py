import os
from flask import Flask, render_template,json,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('sssm-home.html')

@app.route('/sssm-calender.html')

def event():
	if request.method == 'GET':
		dat = renderblog();	
		return render_template('sssm-calender.html',dat=dat);

def renderblog():
   	filename = os.path.join(app.static_folder, 'data.json')
   	with open(filename) as blog_file:
   		data = json.load(blog_file)
   	return data;

if __name__ == "__main__":
    app.run(debug=True)