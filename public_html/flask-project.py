from flask import Flask, render_template, send_from_directory, json, request, jsonify
import os
app = Flask(__name__)

@app.route('/')
def base():
    
    return render_template('sssm-home.html')

@app.route('/sssm-home')
def home():
    
    return render_template('sssm-home.html')

@app.route('/sssm-gallery')
def gallery():
    
    return render_template('sssm-gallery.html')

@app.route('/sssm-committee')
def commitee():
    
    return render_template('sssm-committee.html')

@app.route('/sssm-developers')
def developers():
    
    return render_template('sssm-developers.html')

@app.route('/sssm-dharamshala')
def dharamshala():
    
    return render_template('sssm-dharamshala.html')

@app.route('/sssm-downloads')
def downloads():
    
    return render_template('sssm-downloads.html')

@app.route('/sssm-calender')
def calendar():
   
    return render_template('sssm-calender.html')

@app.route('/sssm-login')
def login():
    
    return render_template('sssm-login.html')

@app.route('/sssm-mandal')
def mandal():
    
    return render_template('sssm-mandal.html')

@app.route('/sssm-membership')
def membership():
    
    return render_template('sssm-membership.html')

@app.route('/sssm-query')
def query():
    
    return render_template('sssm-query.html')

@app.route('/sssm-roombooking')
def roombooking():
    
    return render_template('sssm-roombooking.html')

@app.route('/sssm-supportus')
def supportus():
    
    return render_template('sssm-supportus.html')

@app.route('/sssm-trustees')
def trustees():
    
    return render_template('sssm-trustees.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),
                          'sssm-logo.png')

@app.route('/js')
def renderblog():
    filename = os.path.join(app.static_folder, 'data.json')
    with open(filename) as blog_file:
        data = json.load(blog_file)
    return jsonify(data);


if __name__ == "__main__":
    app.run(debug=True)