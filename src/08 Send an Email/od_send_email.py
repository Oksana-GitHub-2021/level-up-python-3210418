import smtplib, ssl

def send_email(receiver_email, subject, body):
  server = smtplib.SMTP("smtp.gmail.com",587)
  context = ssl.create_default_context()
  server.starttls(context = context)
  server.sendmail(receiver_email, subject, body)
  
send_email('oksana.dobriak@gmail.com', 'Notification', 'Everything is awesome!')