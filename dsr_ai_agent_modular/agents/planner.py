# Decides whether to remind, send or skip
from datetime import datetime, timedelta
import calendar
from core.state import (
    load_task_file,
    tasks_are_same,
    already_sent_today,
    is_on_leave
)

def plan_action(today: datetime) -> str:
    weekday = calendar.day_name[today.weekday()]

    # 1. Skip if weekend
    if weekday in ['Saturday', 'Sunday']:
        return "skip"

    # 2. Skip if on leave
    if is_on_leave(today):
        return "skip"

    # 3. Check today's and yesterday's task files
    today_data = load_task_file(today)
    yesterday = today - timedelta(days=1)
    yesterday_data = load_task_file(yesterday)

    # 4. If today's file is missing
    if not today_data:
        return "remind"

    # 5. If today's file is identical to yesterday's
    if tasks_are_same(today_data, yesterday_data):
        return "remind"

    # 6. If already sent today
    subject = f"Status Report {today.strftime('%d %B %Y')} {weekday}"
    if already_sent_today(subject):
        return "skip"

    # 7. Otherwise, send DSR
    return "send"
