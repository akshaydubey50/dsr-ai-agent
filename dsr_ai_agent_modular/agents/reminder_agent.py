from core.email_client import authenticate_gmail, create_message, send_message
from core.env import get_config
from datetime import datetime

def run():
    config = get_config()
    subject = "🛑 DSR Reminder: Missing or Repeated Tasks"
    today_str = datetime.now().strftime("%A, %d %B %Y")
    body = f"Reminder: Please update your task data for {today_str} before 11:00 PM."

    service = authenticate_gmail()
    msg = create_message(
        sender=config["email"],
        to=config["email"],
        cc="",
        subject=subject,
        message_text=body
    )
    send_message(service, msg)
    print("🔔 Reminder email sent.")