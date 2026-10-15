from email.message import EmailMessage
from dotenv import load_dotenv, find_dotenv
import os
import smtplib

load_dotenv(find_dotenv(), override=True)

app_password = os.getenv("APP_PASSWORD")
from_email = os.getenv("FROM_EMAIL")

business_contacts = [
    {
    "name": "RC",
    "email": "xohigoh958@juicehour.com",
    "project": "General Format of Project Report",
    "report": "Format Project Report.pdf",
    "known_issue": "by Maulana Abul Kalam Azad University of Technology in West Bengal"
    }
]

message = EmailMessage()

# message["Subject"] = "CyberCoder by Nick"
# message["From"] = str(from_email)
# message["To"] = "ishan240401@gmail.com"

# message.set_content("Greeting Everyone, I am a Nick Fernandez, I live in Calgary in Canada. "
#                     "I passed out my Cybersecurity Speciality at Harvard University in 2026. "
#                     "My Skills Experience is Python and Kali-Linux Tools. "
#                     "I learn a new skills for doing any Job in the USA")

# print(message)

# profile_photo = open("Nick Fernandez.jpg", "rb").read()
#
# message.add_attachment(
#     profile_photo,
#     maintype="image",
#     subtype="jpg"
# )

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as email_server:
    email_server.login(
        str(from_email), str(app_password)
    )

    for contact in business_contacts:
        message["Subject"] = contact["project"] + " Status Update"
        message["From"] = str(from_email)
        message["To"] = contact["email"]

        message.set_content(
            f"""
            Hi {contact['name']},

            I have an update on the {contact['project']}.
            
            Everything is running according to plan. 
            However, we're currently dealing with {contact['known_issue']}.
            
            I'd appreciate your input on the matter.
            
            PS. Full report is attached.
            Rudrashis Chowdhury
            """
        )

        report_pdf = open(contact["report"], "rb").read()
        message.add_attachment(
            report_pdf,
            maintype="application",
            subtype="pdf",
            filename=contact["report"]
        )

        email_server.send_message(message)
        print("Email was sent to", contact["name"])

