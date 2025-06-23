# Handles task comparisons and email sent checks
import os
import json
from datetime import datetime, timedelta
from core.email_client import authenticate_gmail

def load_task_file(date_obj):
    path = f"data/tasks/{date_obj.strftime('%Y-%m-%d')}.json"
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return None

def tasks_are_same(today_data, yesterday_data):
    if not today_data or not yesterday_data:
        return False

    # Ignore leave and timing when comparing
    exclude_keys = {"leave", "start_time", "leaving_time"}
    clean_today = {k: v for k, v in today_data.items() if k not in exclude_keys}
    clean_yesterday = {k: v for k, v in yesterday_data.items() if k not in exclude_keys}
    
    return clean_today == clean_yesterday

def already_sent_today(subject: str) -> bool:
    service = authenticate_gmail()
    today = datetime.now().strftime("%Y/%m/%d")
    query = f'subject:"{subject}" after:{today}'
    result = service.users().messages().list(userId='me', q=query, maxResults=1).execute()
    return 'messages' in result

def is_on_leave(date_obj: datetime) -> bool:
    # Check data/tasks/YYYY-MM-DD.json → { "leave": true }
    task_data = load_task_file(date_obj)
    if task_data and task_data.get("leave") is True:
        return True

    # Check data/leaves.json list
    leave_path = "data/leaves.json"
    if os.path.exists(leave_path):
        with open(leave_path) as f:
            leave_dates = json.load(f)
        return date_obj.strftime("%Y-%m-%d") in leave_dates

    return False
