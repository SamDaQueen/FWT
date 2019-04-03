import database_handler
import datetime

import email_handler

from flask import Flask, render_template, send_from_directory, json, request, jsonify, send_file, request,abort 

import os
import threading

app = Flask(__name__)

class WrongEntry(Exception):
    pass

@app.route('/')
def base():
    
    return render_template('sssm-home.html')

@app.route('/sssm-home')
def home():
    print("entering loop")
    image_names=os.listdir('./static/images/home')
    print("2")
    print(image_names)
    return render_template('sssm-home.html',image_names=image_names)
    
@app.route('/sssm-gallery')
def gallery():
    
    print("entering loop")
    image_names=os.listdir('./static/images/gallery')
    print("2")
    print(image_names)
    return render_template('sssm-gallery.html',image_names=image_names)

@app.route('/sssm-committee')
def commitee():
    
    return render_template('sssm-committee.html')

@app.route('/sssm-developers')
def developers():
    
    return render_template('sssm-developers.html')

@app.route('/sssm-shyambaba')
def shyambaba():
    
    return render_template('sssm-shyambaba.html')

@app.route('/sssm-dharamshala')
def dharamshala():
       return render_template('sssm-dharamshala.html')

@app.route('/sssm-downloads',methods = ['POST','GET'])
def downloads():
    if request.method=='POST':
    	name = request.form['filename']
    	if name=='aarti':
    		return send_file('static/bhajans/aarti.pdf')
    	if name=='bbook':
    		return send_file('static/bhajans/bhajanbook.pdf')
    	if name=='b388':
    		return send_file('static/bhajans/bhajan388.pdf')
    	if name=='shiv':
    		return send_file('static/bhajans/shiv.zip', as_attachment=True, attachment_filename='Bhajan_lal_gulab.zip')
    elif(request.method=='GET'):
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

@app.route('/sssm-404')
def error():
    
    return render_template('sssm-404.html')

@app.route('/sssm-membership',methods = ['POST','GET'])
def membership():

    if request.method == "GET":
        return render_template('sssm-membership.html',form=1)
    elif request.method == "POST":
        try:

            member = { 'first_name':request.form['firstName'],'last_name':request.form['lastName'],
            'email':request.form['email'],'birth_date':request.form['birth_date'],
            'address':request.form['address'],'occupation':request.form['occupation'],
            'mobile':request.form['mobile']}
            
            member['landline']= request.form['landline']
            member['office']= request.form['office']

            member['fm1_name']= request.form['fm1_name']
            member['fm1_relation']= request.form['fm1_relation']
            member['fm1_birth_date']= request.form['fm1_birth_date']

            member['fm2_name']= request.form['fm2_name']
            member['fm2_relation']= request.form['fm2_relation']
            member['fm2_birth_date']= request.form['fm2_birth_date']

            member['fm3_name']= request.form['fm3_name']
            member['fm3_relation']= request.form['fm3_relation']
            member['fm3_birth_date']= request.form['fm3_birth_date']

            member['fm4_name']= request.form['fm4_name']
            member['fm4_relation']= request.form['fm4_relation']
            member['fm4_birth_date']= request.form['fm4_birth_date']

            member['fm5_name']= request.form['fm5_name']
            member['fm5_relation']= request.form['fm5_relation']
            member['fm5_birth_date']= request.form['fm5_birth_date']

            member['date_time'] = datetime.datetime.now().strftime("%d %B %Y at %X")


            #t1 = threading.Thread(target=database_handler.Member, args=(member,)) 
            #t2 = threading.Thread(target=email_handler.send_member_mail, args=(member,)) 

            database_handler.Member(member)
            email_handler.send_member_mail(member)

        except WrongEntry:
            return render_template('sssm-membership.html',form=1)
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

            #t1 = threading.Thread(target=database_handler.Query, args=(query,)) 
            #t2 = threading.Thread(target=email_handler.send_query_mail, args=(query,)) 

            #t1.start() 
            #t2.start() 
        
            #t1.join() 
            #t2.join() 

            database_handler.Query(query)
            email_handler.send_query_mail(query)

        except WrongEntry:
            return render_template('sssm-query.html',form=1)
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
            'check-in-date':request.form['check_in_date'],'check-in-time-hour':request.form['check-in-time-hour'],
            'check-in-time-minute':request.form['check-in-time-minute'],'check-out-date':request.form['check_out_date'],
            'check-out-time-hour':request.form['check-out-time-hour'],'check-out-time-minute':request.form['check-out-time-minute'],
            'no-of-people':request.form['people'],'room-type':request.form['room-type']}

            booking['date_time'] = datetime.datetime.now().strftime("%d %B %Y at %X")

            # t1 = threading.Thread(target=database_handler.Booking, args=(booking,)) 
            # t2 = threading.Thread(target=email_handler.send_booking_mail, args=(booking,)) 
            
            # t1.start() 
            # t2.start() 
          
            # t1.join() 
            # t2.join() 

            database_handler.Booking(booking)
            email_handler.send_booking_mail(booking)

        except WrongEntry:
            return render_template('sssm-roombooking.html',form=1)
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

@app.errorhandler(404) 
def not_found(e): 

    return render_template("sssm-404.html") 

if __name__ == "__main__":
     app.run(debug=True)



