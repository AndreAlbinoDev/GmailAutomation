#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
import email.message

def send_email():
    body = """
    <p>paragraph1</p>
    <p>paragraph2</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "write email subject in this field"
    msg['From'] = 'write from in this field'
    msg['To'] = 'write recipient in this field'
    password = 'app passwords provided by google'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email send')


# In[ ]:


send_email()

