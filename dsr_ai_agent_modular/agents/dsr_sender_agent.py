from core.generator import generate_dsr_email
from core.email_client import authenticate_gmail, create_message, send_message
from core.env import get_config
from datetime import datetime
import os
import json

def run(today, weekday, today_data):
    config = get_config()
    subject = f"Status Report {today.strftime('%d %B %Y')} {weekday}"
    body = generate_dsr_email(today, weekday, config, today_data)

    service = authenticate_gmail()
    msg = create_message(
        sender=config["email"],
        to="akshaydubey004@gmail.com",
        cc="akshaydubey2060@gmail.com",
        subject=subject,
        message_text=body
    )
    send_message(service, msg)
    print(f"📨 Sent DSR for {today.strftime('%Y-%m-%d')}")