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

	msg_2 = MIMEMultipart("alternative")
	msg_2['Subject'] = 'Query by '  + query['first_name']+" "+query['last_name']
	msg_2['From'] = 'sssm.mum@gmail.com'
	msg_2['To'] = "gncis8@gmail.com"

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

	msg_2.attach(part)

	send_and_close(server,msg_2.as_string())

	return 'It works'

def send_membership_mail(member):

	server = login()

	msg_2 = MIMEMultipart("alternative")
	msg_2['Subject'] = 'New member request by '+ member['first_name']+" "+member['last_name']
	msg_2['From'] = 'sssm.mum@gmail.com'
	msg_2['To'] = "gncis8@gmail.com"

	no_of_family=0

	family_html = ''

	if member['fm1-name'] != '':
		family_html += '<tr><td>'+member['fm1-name']+'</td> <td>'+member['fm1-relation']+'</td> <td>'+member['fm1-birth-date']+'</td> </tr>'
		no_of_family +=1
	if member['fm2-name'] != '':
		family_html += '<tr><td>'+member['fm2-name']+'</td> <td>'+member['fm2-relation']+'</td> <td>'+member['fm2-birth-date']+'</td> </tr>'
		no_of_family +=1
	if member['fm3-name'] != '':
		family_html += '<tr><td>'+member['fm3-name']+'</td> <td>'+member['fm3-relation']+'</td> <td>'+member['fm3-birth-date']+'</td> </tr>'
		no_of_family +=1
	if member['fm4-name'] != '':
		family_html += '<tr><td>'+member['fm4-name']+'</td> <td>'+member['fm4-relation']+'</td> <td>'+member['fm4-birth-date']+'</td> </tr>'
		no_of_family +=1
	if member['fm5-name'] != '':
		family_html += '<tr><td>'+member['fm5-name']+'</td> <td>'+member['fm5-relation']+'</td> <td>'+member['fm5-birth-date']+'</td> </tr>'
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

	msg_2.attach(part)

	send_and_close(server,msg_2.as_string())

	return 'YEs'