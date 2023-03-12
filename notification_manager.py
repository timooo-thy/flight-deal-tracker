from twilio.rest import Client
import smtplib
ACCOUNT = "ACbce78b7fd8250e0ac57a726dc4e1b611"
AUTH_TOKEN = "371198913c7afeed4c62695c12d94ba6"
EMAIL = "matrixavenger2000@gmail.com"
PASSWORD = "mdkkvlixzhxbvunq"


class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT, AUTH_TOKEN)

    def send_msg(self, message):
        message = self.client.messages \
            .create(
            body=message,
            from_='+19034005624',
            to='+6598572155'
        )
        print(message.status)

    def send_email(self, emails, message, link):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n\n{link}".encode('utf-8')
                )