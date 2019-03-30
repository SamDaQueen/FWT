import database_handler
import datetime
import email_handler
from flask import Flask, render_template, send_from_directory, json, request, jsonify,request,abort 
import os
import threading

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

@app.route('/sssm-membership',methods = ['POST','GET'])
def membership():

    if request.method == "GET":
        return render_template('sssm-membership.html',form=1)
    elif request.method == "POST":
        try:

            member = { 'first_name':request.form['firstName'],'last_name':request.form['lastName'],
            'email':request.form['email'],'birth_date':request.form['birth-date'],
            'address':request.form['address'],'occupation':request.form['occupation'],
            'mobile':request.form['mobile']}
            
            member['landline']= request.form['landline']
            member['office']= request.form['office']

            member['fm1-name']= request.form['fm1-name']
            member['fm1-relation']= request.form['fm1-relation']
            member['fm1-birth-date']= request.form['fm1-birth-date']

            member['fm2-name']= request.form['fm2-name']
            member['fm2-relation']= request.form['fm2-relation']
            member['fm2-birth-date']= request.form['fm2-birth-date']

            member['fm3-name']= request.form['fm3-name']
            member['fm3-relation']= request.form['fm3-relation']
            member['fm3-birth-date']= request.form['fm3-birth-date']

            member['fm4-name']= request.form['fm4-name']
            member['fm4-relation']= request.form['fm4-relation']
            member['fm4-birth-date']= request.form['fm4-birth-date']

            member['fm5-name']= request.form['fm5-name']
            member['fm5-relation']= request.form['fm5-relation']
            member['fm5-birth-date']= request.form['fm5-birth-date']

            member['date_time'] = datetime.datetime.now().strftime("%d %B %Y at %X")

            t1 = threading.Thread(target=database_handler.Member, args=(member,)) 
            t2 = threading.Thread(target=email_handler.send_member_mail, args=(member,)) 

        except Exception as e:
            return render_template('sssm-membership.html',form=3)

        else:
            return render_template('sssm-membership.html',form=2)

@app.route('/sssm-query',methods = ['POST','GET'])
def query_page():
    if request.method == "GET":
    	return render_template('sssm-query.html',form=1)
    elif request.method == "POST":
        try:
            query = { 'first_name':request.form['firstName'],'last_name':request.form['lastName'],
            'email':request.form['email'],'mobile':request.form['mobile'],'query':request.form['query']}
            query['date_time'] = datetime.datetime.now().strftime("%d %B %Y at %X")

            t1 = threading.Thread(target=database_handler.Query, args=(query,)) 
            t2 = threading.Thread(target=email_handler.send_query_mail, args=(query,)) 

            # starting thread 1 
            t1.start() 
            # starting thread 2 
            t2.start() 
          
            # wait until thread 1 is completely executed 
            t1.join() 
            # wait until thread 2 is completely executed 
            t2.join() 

        except Exception as e:
            return render_template('sssm-query.html',form=3)
        else:
            return render_template('sssm-query.html',form=2)

@app.route('/sssm-roombooking',methods = ['POST','GET'])
def roombooking():

    if request.method == "GET":
        return render_template('sssm-roombooking.html',form=1)
    elif request.method == "POST":
        try:
            booking = { 'first_name':request.form['firstName'],'last_name':request.form['lastName'],
            'email':request.form['email'],'mobile':request.form['mobile'],'address':request.form['address'],
            'check-in-date':request.form['check-in-date'],'check-in-time-hour':request.form['check-in-time-hour'],
            'check-in-time-minute':request.form['check-in-time-minute'],'check-out-date':request.form['check-out-date'],
            'check-out-time-hour':request.form['check-out-time-hour'],'check-out-time-minute':request.form['check-out-time-minute'],
            'no-of-people':request.form['people'],'room-type':request.form['room-type']}

            booking['date_time'] = datetime.datetime.now().strftime("%d %B %Y at %X")

            t1 = threading.Thread(target=database_handler.Booking, args=(booking,)) 
            t2 = threading.Thread(target=email_handler.send_booking_mail, args=(booking,)) 
            
            # starting thread 1 
            t1.start() 
            # starting thread 2 
            t2.start() 
          
            # wait until thread 1 is completely executed 
            t1.join() 
            # wait until thread 2 is completely executed 
            t2.join() 

        except Exception as e:
            return render_template('sssm-roombooking.html',form=3)
        else:
            return render_template('sssm-roombooking.html',form=2)

@app.route('/sssm-supportus')
def supportus():
    
    return render_template('sssm-supportus.html')

@app.route('/sssm-trustees')
def trustees():
    
    return render_template('sssm-trustees.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),'sssm-logo.png')

@app.route('/js')
def renderblog():
    filename = os.path.join(app.static_folder, 'data.json')
    with open(filename) as blog_file:
        data = json.load(blog_file)
    return jsonify(data);

if __name__ == "__main__":
    app.run(debug=True)