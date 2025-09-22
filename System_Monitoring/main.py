import psutil
import time
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from plyer import notification

import os

# Load environment variables
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
TO_EMAIL = os.getenv("TO_EMAIL")

# Thresholds
CPU_THRESHOLD = 80
RAM_THRESHOLD = 80
DISK_THRESHOLD = 85



def send_desktop_alert(message):
    """Send desktop notification."""
    notification.notify(
        title="🚨 Server Health Alert",
        message=message,
        timeout=5
    )

def send_email_alert(subject, message):
    """Send an email alert using SMTP."""
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = TO_EMAIL

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"📧 Alert email sent: {subject}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

def check_health():
    alerts = []

    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent

    if cpu_usage > CPU_THRESHOLD:
        alerts.append(f"⚠️ High CPU usage: {cpu_usage}%")
    if ram_usage > RAM_THRESHOLD:
        alerts.append(f"⚠️ High RAM usage: {ram_usage}%")
    if disk_usage > DISK_THRESHOLD:
        alerts.append(f"⚠️ High Disk usage: {disk_usage}%")

    return alerts, cpu_usage, ram_usage, disk_usage

def monitor():
    print("🔍 Starting Server Health Monitor with Email Alerts...")
    try:
        while True:
            alerts, cpu, ram, disk = check_health()
            print(f"\nCPU: {cpu}% | RAM: {ram}% | Disk: {disk}%")

            if alerts:
                print("🚨 ALERTS:")
                for alert in alerts:
                    print(alert)
                # Send email
                send_email_alert("🚨 Server Alert", "\n".join(alerts))
                send_desktop_alert("\n".join(alerts))
            else:
                print("✅ All systems normal.")

            time.sleep(5)
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped.")

if __name__ == "__main__":
    monitor()
