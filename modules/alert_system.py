import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()  # Memuat variabel lingkungan dari file .env

def send_alert(device_ip, message):
    sender = os.getenv('EMAIL_ADDRESS')
    password = os.getenv('EMAIL_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')
    receivers = os.getenv('RECEIVERS').split(',')

    msg = MIMEText(message)
    msg['Subject'] = f'Alert for device {device_ip}'
    msg['From'] = sender
    msg['To'] = ', '.join(receivers)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receivers, msg.as_string())
        print(f"Alert sent to {', '.join(receivers)} for device {device_ip}")
    except Exception as e:
        print(f"Failed to send alert: {e}")
