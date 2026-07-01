import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from dotenv import load_dotenv
import os


class EmailSender:
    def __init__(self):
        load_dotenv()
        self.username = os.getenv('USER')
        self.password = os.getenv('PASSWORD')
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587

    def send_email(self, subject, body, to_email, image_path=None):
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        if image_path:
            with open(image_path, 'rb') as img_file:
                img = MIMEImage(img_file.read())
                img.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(image_path)}"')
                msg.attach(img)

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)
                print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def cerrar_conexion(self):
        pass


if __name__ == "__main__":
    email_sender = EmailSender()
    email_sender.send_email(
        subject="Test Email",
        body="<h1>This is a test email</h1>",
        to_email="recipient@example.com"
    )