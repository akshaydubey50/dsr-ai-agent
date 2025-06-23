from datetime import datetime, timedelta
from core.dsr_summary import collect_task_data, summarize_tasks, print_summary

today = datetime.now()
start = today - timedelta(days=today.weekday())  # Monday
end = start + timedelta(days=4)  # Friday

data = collect_task_data(start, end)
if data:
    summary = summarize_tasks(data)
    print_summary(summary, "Weekly DSR")
else:
    print("No task data found for the current week.")
