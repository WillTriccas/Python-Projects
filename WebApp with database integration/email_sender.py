from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, total_users):

    #the email and height variables are the variables that are going to get typed by the user in the app and requested from the python script

    from_email = "willtriccas@gmail.com"
    from_password = "redteds4"
    to_email = email 

    subject = "Your Height Data"
    message = "Hey there, your height is <strong>%s<strong> <br> \
    The average height of all users is <strong>%s<strong> <br>\
    This is from a total of <strong>%s<strong> users <br><br><br>\
    Miss you bubs xxx" %(height , average_height, total_users)

    msg = MIMEText(message, 'html')  #this means that our message is parsed in html so we can add elements like <Strong> to our message
    msg['Subject'] = subject
    msg['To'] = email
    msg['From'] = from_email

    #Set up Gmail SMTP server
    gmail = smtplib.SMTP('smtp.gmail.com' , 25) #25 is the port of smtp
    gmail.ehlo() # Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)