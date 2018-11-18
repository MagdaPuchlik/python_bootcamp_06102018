import smtplib
user="madziapuchlik@wp.pl"
password="grymiaczki7"

sent_from="madziapuchlik@wp.pl"
to=["puchlik.magdalena@gmail.com"]
subject = "try this"
body = "To jest treść"

email_txt=f"""
From:{sent_from}
To:{','.join(to)}
Suhject: {subject}

{body}

"""

try:
    server = smtplib.SMTP_SSL("smtp.wp.pl",465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(sent_from,to,email_txt)
    server.close()
except Exception as e:
    print(e)
    print("Coś poszło żle")