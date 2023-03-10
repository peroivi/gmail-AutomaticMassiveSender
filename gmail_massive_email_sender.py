#!/usr/bin/python
# -*- coding: utf-8 -*-

#Libraries
import os
import time


#Email and server libraries
from email.mime.text import MIMEText
from smtplib import SMTP

#Config  library
import configparser

#List of email
message='''Hello we are the UPC Vilanova E3Team,


We are a team formed by several students from the five engineering disciplines taught at the EPSEVG campus of the Polytechnic University of Catalonia (UPC) Spain. 

We are participating in the renowned MotoStudent competition. This event brings together the best engineering universities at national and international level, in order to present their projects of design and prototyping of an electric racing motorcycle. Our team’s principle is competitive and efficient sustainability.


We are contacting because we believe that you could be interested in a collaboration agreement with the team and in being able to be part of this project.


We believe that the union between our ambition and commitment, together with your experience and business projection, will lead us to achieve success wherever we compete and will bring added value to your company. We would be proud to display your brand in the MotoStudent 2021-2023 competition that we will soon partake in.


In the attached file you can find a detailed description of the project you would be investing in and what the sponsorship consists of.


However, we would like to be able to present our proposal in more detail and answer any questions if needed. We hope you will consider our proposal and let us know your decision.


Yours sincerely.


The UPC VILANOVA E3TEAM'''


#Open and read the file of emails address
emails_file=open("emails_file.txt")
list_of_emails=emails_file.readlines()

for index in range(len(list_of_emails)):
    list_of_emails[index]=list_of_emails[index].replace("\n","")

#list_of_emails=["defaultemail@gmail.com","defaultemail@gmail.com","defaultemail@gmail.com","defaultemail@gmail.com"]

class gmail_account:
    def new(self,user,password):
        self.password=str(password)
        self.user=str(user)
    def get_user(self):
        return self.user
    def get_password(self):
        return self.password

class email:
    def new(self,from_address, to_address,subject, message):
        self.from_address=str(from_address)
        self.to_address=str(to_address)
        self.subject=str(subject)
        self.message=str(message)
    def get_from_address(self):
        return self.from_address
    def get_to_address(self):
        return self.to_address
    def get_subject(self):
        return self.subject

def main():

    #User data
    print ("[+] Reading config file... ")
    print("Done")
    config = configparser.ConfigParser()
    config.read([os.path.expanduser('./config')])

    user=gmail_account()
    user.new(config.get('user_email','user_name'),config.get('user_email','password'))

    #parse email message to include new lines and paragraphs
    message1 = message
    message1.replace('\\n', '\n')

    #Email data
    email_to_send=email()
    email_to_send.new(user.get_user(),"defaultemail@gmail.com",config.get('email_data','subject'),message1)

    #Load of packages control


    counter_factor=1
    for index in range(len(list_of_emails)):
        #Sending the email

        mime_message = MIMEText(message)
        #mime_message["From"] = email_to_send.get_from_address()
        mime_message["From"] = user.get_user()
        mime_message["To"] =list_of_emails[index]
        #mime_message["To"] =email_to_send.get_to_address()
        mime_message["Subject"] = email_to_send.get_subject()

        smtp = SMTP("smtp.gmail.com", 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(user.get_user(), user.get_password())
        smtp.sendmail(email_to_send.get_from_address(), list_of_emails[index], mime_message.as_string())
        print("\nEmail sended to: "+list_of_emails[index]+ " from: "+email_to_send.get_from_address())
        smtp.quit()


        if(index>=counter_factor*int(config.get('packages_control','emails_in_package'))-1):
            print ("\nWaiting "+config.get('packages_control','sleeping_time')+" for the next package")
            time.sleep(float(config.get('packages_control','sleeping_time')))
            counter_factor=counter_factor+1

if __name__ == "__main__":
 main()
