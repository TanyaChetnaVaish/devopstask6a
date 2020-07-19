import smtplib
import urllib.request as urllib
# Senders email
sender_email = "tanya.vaish.743@gmail.com"
# Receivers email
rec_email = ""tanya.vaish.743@gmail.com"

message = "Kuberenetes cluster not running.Do the required changes."
# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)
# Start the server connection
server.starttls()
# Login
server.login(""tanya.vaish.743@gmail.com", "writeyourpasswordhere")
print("Login Success!")
# Send Email
server.sendmail("Tanya Chetna Vaish", ""tanya.vaish.743@gmail.com", message)
