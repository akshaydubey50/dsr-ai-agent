from datetime import datetime
from calendar import monthrange
from core.dsr_summary import collect_task_data, summarize_tasks, print_summary

today = datetime.now()
start = today.replace(day=1)
last_day = monthrange(today.year, today.month)[1]
end = today.replace(day=last_day)

data = collect_task_data(start, end)
if data:
    summary = summarize_tasks(data)
    print_summary(summary, "Monthly DSR")
else:
    print("No task data found for this month.")
