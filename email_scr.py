import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import os
from datetime import datetime

# getting current date
TEST_RESULT = os.getenv("TRAVIS_TEST_RESULT")
TRAVIS_EVENT_TYPE = os.getenv("TRAVIS_EVENT_TYPE")
cur_date = datetime.today().strftime('%d-%m-%Y') # + "Test result:" + TEST_RESULT + " | " + TRAVIS_EVENT_TYPE


#recipients_list = ["abavabaraba@gmail.com"] 
recipients_list = ["abavabaraba@gmail.com", "mike_zone@ukr.net", "sridevi.harsha@we.shop", "nik.lalev@weshop.co.uk", "shriharsha.ka@we.shop", "danilo.lapegna@weshop.co.uk"]

GMAIL_ACC_KEY = os.getenv("GMAIL_ACC_KEY")

def email_sender(recipient):
	# travis link
	travis_ci_build_link = os.getenv("TRAVIS_BUILD_WEB_URL")

	subject = f"Travis CI report | iOS automation tests | {cur_date}"
	body = f"Travis CI build link: {travis_ci_build_link}"
	sender_email = "abavabaraba@gmail.com"
	receiver_email = recipient #"abavabaraba@gmail.com", "mike_zone@ukr.net" #"abavabaraba@gmail.com"
	password = GMAIL_ACC_KEY #input("Type your password and press enter:")

	# Create a multipart message and set headers
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = subject
	message["Bcc"] = receiver_email  # Recommended for mass emails

	# Add body to email
	message.attach(MIMEText(body, "plain"))

	filename = os.getcwd() + "/report.html"  # report to send (should be in root folder)

	# Open PDF file in binary mode
	with open(filename, "rb") as attachment:
		# Add file as application/octet-stream
		# Email client can usually download this automatically as attachment
		part = MIMEBase("application", "octet-stream")
		part.set_payload(attachment.read())

	# Encode file in ASCII characters to send by email    
	encoders.encode_base64(part)

	# Add header as key/value pair to attachment part
	part.add_header(
		"Content-Disposition",
		f"attachment; filename= {filename}",
	)

	# Add attachment to message and convert message to string
	message.attach(part)
	text = message.as_string()

	# Log in to server using secure context and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, text)


# send report email(s) on fail and success
if len(recipients_list) > 0:
	for i in recipients_list:
		email_sender(i)
		time.sleep(0.5)

else:
	print(f"{ERORR} RECIPIENT LIST IS EMPTY!")

# send report email(s) only ON FAIL
# if len(recipients_list) > 0:
# 	if TEST_RESULT == '1':
# 		for i in recipients_list:
# 			email_sender(i)
# 			time.sleep(0.5)

# else:
# 	print(f"{ERORR} RECIPIENT LIST IS EMPTY!")


