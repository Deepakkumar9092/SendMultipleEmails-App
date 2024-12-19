import smtplib as s

ob = s.SMTP('smtp.gmail.com',587) #server port 
ob.ehlo()
ob.starttls() #security
ob.login('deepakjp9092@gmail.com','Deepak@9092')
subject="test python"
body="This is using for Python For Testing to send bulk emails"
message = "subject:{}\n\n{}".format(subject,body)
listadd=['dk9065181292@gmail.com','deepakjb90@gmail.com']

ob.sendmail('deepakjp9092@gmail.com',listadd,message)
print("Send Mail Successfully")
ob.quit()

# import smtplib as s

# # Initialize SMTP connection
# ob = s.SMTP('smtp.gmail.com', 587)  # Server and port
# ob.ehlo()  # Identify to the SMTP server
# ob.starttls()  # Secure the connection
# ob.login("deepakjp9092@gmail.com", "Deepak@9092")  # Replace with your App Password

# # Email details
# subject = "Test Python"
# body = "This is using Python for testing to send bulk emails"
# message = f"Subject: {subject}\n\n{body}"  # Properly formatted subject line
# listadd = ['dk9065181292@gmail.com', 'deepakjb90@gmail.com']

# # Join the recipient list into a single comma-separated string
# recipients = ", ".join(listadd)

# # Send email to multiple recipients
# ob.sendmail('deepakjp9092@gmail.com', recipients, message)

# print("Emails sent successfully!")

# # Quit the SMTP server
# ob.quit()
