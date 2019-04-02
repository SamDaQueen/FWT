from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def login():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()

	server.login("sssm.mum@gmail.com", "Sssm@1972")

	return server

def send_and_close(server,data):
	server.sendmail("sssm.mum@gmail.com",
	"gncis8@gmail.com", data)

	server.close()

def send_query_mail(query):
	
	server = login()

	msg = MIMEMultipart("alternative")
	msg['Subject'] = 'Query by '  + query['first_name']+" "+query['last_name']
	msg['From'] = 'sssm.mum@gmail.com'
	msg['To'] = "gncis8@gmail.com"

	html_txt = """
	<html>
		<body>

		<h2>Query by """ + query['first_name']+" "+query['last_name']+""" on """+query['date_time']+"""</h2>
			<p>
				"""+ query['query']+"""

			</p>
			<br>
			<h4>This email can be replied to with an <a href = \" mailto:"""+query['email']+""" \">email</a> or call at +91"""+ query['mobile'] + """</h4>
		</body>
	</html>
	"""

	part = MIMEText(html_txt, 'html')

	msg.attach(part)

	send_and_close(server,msg.as_string())

def send_member_mail(member):

	server = login()

	msg = MIMEMultipart("alternative")
	msg['Subject'] = 'New member request by '+ member['first_name']+" "+member['last_name']
	msg['From'] = 'sssm.mum@gmail.com'
	msg['To'] = "gncis8@gmail.com"

	no_of_family=0

	family_html = ''

	if member['fm1_name'] != '':
		family_html += '<tr><td>'+member['fm1_name']+'</td> <td>'+member['fm1_relation']+'</td> <td>'+member['fm1_birth_date']+'</td> </tr>'
		no_of_family +=1
	if member['fm2_name'] != '':
		family_html += '<tr><td>'+member['fm2_name']+'</td> <td>'+member['fm2_relation']+'</td> <td>'+member['fm2_birth_date']+'</td> </tr>'
		no_of_family +=1
	if member['fm3_name'] != '':
		family_html += '<tr><td>'+member['fm3_name']+'</td> <td>'+member['fm3_relation']+'</td> <td>'+member['fm3_birth_date']+'</td> </tr>'
		no_of_family +=1
	if member['fm4_name'] != '':
		family_html += '<tr><td>'+member['fm4_name']+'</td> <td>'+member['fm4_relation']+'</td> <td>'+member['fm4_birth_date']+'</td> </tr>'
		no_of_family +=1
	if member['fm5_name'] != '':
		family_html += '<tr><td>'+member['fm5_name']+'</td> <td>'+member['fm5_relation']+'</td> <td>'+member['fm5_birth_date']+'</td> </tr>'
		no_of_family +=1

	if no_of_family > 0:
		family_html = """<br>

						<h3>They have the following family members</h3>

						<table>
							<tr>
								<th>Name</th>
								<th>Relation</th>
								<th>Birth Date</th>
							</tr>""" + family_html + """
						</table>

						<br>
						"""

	print(type(family_html))

	html_txt = """
	<html>
		<body>

		<h2>Membership request by """ + member['first_name']+" "+member['last_name']+""" on """+member['date_time']+"""</h2>
		<br>
			<h3>The Applicants Details<h3>
			<table>
				<tr>
					<th>Name</th>
					<td>"""+ member['first_name']+" "+member['last_name']+"""</td>
				</tr>
				<tr>
					<th>Email</th>
					<td>"""+ member['email']+"""</td>
				</tr>
				<tr>
					<th>Birth Date</th>
					<td>"""+ member['birth_date']+"""</td>
				</tr>
				<tr>
					<th>Address</th>
					<td>"""+ member['address']+"""</td>
				</tr>
				<tr>
					<th>Occupation</th>
					<td>"""+ member['occupation']+"""</td>
				</tr>
			</table>

			<br>
			<h3>Telephone Details</h3>

			<table>
				<tr>
					<th>Mobile</th>
					<th>Landline</th>
					<th>Office</th>
				</tr>
				<tr>
					<td>"""+member['mobile']+"""
					<td>"""+member['landline']+"""
					<td>"""+member['office']+"""
				</tr>
			</table>

			<br>

			"""+family_html+"""

			<br>
			<h4>This email can be replied to with an <a href=\"mailto:"""+member['email']+"""\">email</a> or call at +91"""+member['mobile']+"""</h4>
		</body>
	</html>
	"""

	part = MIMEText(html_txt, 'html')

	msg.attach(part)

	send_and_close(server,msg.as_string())

def send_booking_mail(booking):

	server = login()

	msg = MIMEMultipart("alternative")
	msg['Subject'] = 'Booking Request by '  + booking['first_name']+" "+booking['last_name']
	msg['From'] = 'sssm.mum@gmail.com'
	msg['To'] = "gncis8@gmail.com"

	html_txt = """
	<html>
		<body>

			<h2>Booking Request by """ + booking['first_name']+" "+booking['last_name']+""" on """+booking['date_time']+"""</h2>
			
			<h4>Address</h4>
			<p>"""+booking['address']+"""</p>

			<table >
				<tr>
					<td></td>
					<th>Date</th>
					<th>Time</th>
				</tr>
				<tr>
					<th>Check In</th>
					<td>"""+booking['check-in-date']+"""</td>
					<td>"""+booking['check-in-time-hour']+":"+booking['check-in-time-minute']+"""</td>
				</tr>
				<tr>
					<th>Check Out</th>
					<td>"""+booking['check-out-date']+"""</td>
					<td>"""+booking['check-out-time-hour']+":"+booking['check-out-time-minute']+"""</td>
				</tr>
			</table>

			<br>
			<h4>Number of People: </h4>"""+booking['no-of-people']+"""
			<h4>Room Type: </h4>"""+booking['room-type']+"""
			<br>
			<h4>This email can be replied to with an <a href = \" mailto:"""+booking['email']+""" \">email</a> or call at +91"""+ booking['mobile'] + """</h4>
		</body>
	</html>
	"""

	part = MIMEText(html_txt, 'html')

	msg.attach(part)

	send_and_close(server,msg.as_string())
