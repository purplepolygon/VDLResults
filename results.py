#!/usr/bin/env python3


''' Result sender bot for international users
 Sunset and Western street in good ol' Tinseltown, California
 TDX/MALEK/VDL'''


''' Twilio will post message contents through a webhook '''
# Once posted, python will click url ? What Database? FFS it feels over engineered
# Extract the url variable from the text message
# url = url from text


''' Download the pdf from url variable'''
# import requests
#
# url = 'http://www.hrecos.org//images/Data/forweb/HRTVBSH.Metadata.pdf'
# r = requests.get(url, stream=True)
#
# with open('/tmp/metadata.pdf', 'wb') as fd:
#     for chunk in r.iter_content(chunk_size):
#         fd.write(chunk)


''' Once pdf is downloaded, python will parse the pdf'''
# importing required modules
# import PyPDF2

# creating a pdf file object
# pdfFileObj = open('example.pdf', 'rb')
# extracting text from page
# print(pageObj.extractText())


'''Parse the PDF'''
# Regular Expression to parse name:
# re.filter:
# VDL Has it formatted PATIENT NAME: LAST NAME, FIRST NAME
# Switch it to FIRST NAME (strip comma) LAST NAME

'''Compare to DB value'''
# SELECT Name from Name, Email from Email -> Store to Database.Name, Database.Email
# Compare FIRST NAME LAST NAME to FIRST NAME LAST NAME in database
# If FIRSTNAME LAST NAME == Database.NAME:
# E-mail PDF to Database.Email
# Else: Throw error to manually check (Lab error, handwriting, bad text message, w/e)

'''Where did we get this DB value from?
Well, when they take the test we send a text message in strict format: FIRST NAME LAST NAME E-MAIL
This creates a store in the database 3 columns
When we receive the .json from Twilio, we compare FIRST NAME LAST NAME to that sent in the database, if they are equal, we send the pdf to email.
That's it.
Simple.
Now since we have a webhook we can either run it as text-message comes in or on a cron job.'''



# g00gle:
# https://www.twilio.com/docs/sms/tutorials/how-to-receive-and-reply-python