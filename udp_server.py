'''
UDPServer by: Eoin Lyng
Listens for packets on a particular address and port.
Alpha: 13FEB22
'''

import socket
import settings.udp as settings

#email settings using gmail app password(https://mailtrap.io/blog/python-send-email-gmail/)
#https://docs.python.org/3.4/library/email-examples.html

# Import smtplib for the actual sending function

import smtplib

# Import the email modules we'll need

from email.mime.text import MIMEText

# Define what is in fields - change recipients email address to valid email for testing - password is an app password
subject1 = "Extreme Low Temperature Warning!!"
subject2 = "Extreme High Temperature Warning!!"
body1 = "One of your Temperature Sensors is below 5 Degrees Celsius. The sensor that is showing the low temperatures is "
body2 = "One of your Temperature Sensors is over 30 Degrees Celsius. The sensor that is showing the high temperatures is "
body3 = ".The current "
body4 = " is "
sender =settings.UDP["sender_email_address"]
recipients =settings.UDP["recipient_email_address"]
password =settings.UDP["sender_apppassword"]

#Defining when email sent for low Temperature
def send_email_low_temp(subject1, body1, sender, recipients, password):
    msg = MIMEText(body1)
    msg['Subject'] = subject1
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

#Defining when email sent for high Temperature
def send_email_high_temp(subject2, body2, sender, recipients, password):
    msg = MIMEText(body2)
    msg['Subject'] = subject2
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]
BUFFER_SIZE = 1024

print(f'This is the UDP server, it will open a port at {UDP_IP}:{UDP_PORT} and being listening')
print(f'Make sure the actual server IP address matches {UDP_IP} in the settings file')
print('This script has no error handling, by design')

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind( (UDP_IP, UDP_PORT) )
    print('Listening on', UDP_IP)
    while True:
        data, addr = s.recvfrom(BUFFER_SIZE)
        data = data.decode()

  #Split the ouput data on "comma" in to individual fields      
        field_values = data.split(',')

# Temperature < 5 degrees send email with error logging if simulated data not an integer  
        if (field_values[2]).isalpha():
            print ((field_values[2]),(" Is not a Valid Temp"),file=open('error/error.log', 'a')) 
        else:
            if int((field_values[2])) <5:
                send_email_low_temp(subject1, body1+(field_values[0])+body3+(field_values[1])+body4+(field_values[2]), sender, recipients, password)

#Temperature > 30 degrees send email
       #no error logging as value invalid data logged in  previous step
        if not (field_values[2]).isalpha() and  int((field_values[2])) >30:
             send_email_high_temp(subject2, body2+(field_values[0])+body3+(field_values[1])+body4+(field_values[2]), sender, recipients, password)
         
#Output Readings to individual files in data directory
        if not (field_values[2]).isalpha() and (field_values[0]) == 'SensorOne':
            print(addr, data, file=open('data/Sensor_One_Output.log', 'a'))
        if (field_values[0]) == 'SensorTwo':
            print(addr, data, file=open('data/Sensor_Two_Output.log', 'a'))
        if (field_values[0]) == 'SensorThree':
            print(addr, data, file=open('data/Sensor_Three_Output.log', 'a'))
     








