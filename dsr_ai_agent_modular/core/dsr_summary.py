import os
import json
from datetime import datetime, timedelta

def collect_task_data(start_date, end_date):
    data = []
    current = start_date
    while current <= end_date:
        path = f"data/tasks/{current.strftime('%Y-%m-%d')}.json"
        if os.path.exists(path):
            with open(path) as f:
                task_data = json.load(f)
                data.append((current.strftime('%Y-%m-%d'), task_data))
        current += timedelta(days=1)
    return data

def summarize_tasks(task_entries):
    summary = {
        "dates": [],
        "performed_tasks": [],
        "new_tasks": [],
        "prev_incomplete": [],
        "end_incomplete": []
    }
    for date_str, entry in task_entries:
        summary["dates"].append(date_str)
        summary["performed_tasks"].extend(entry.get("performed_tasks", []))
        summary["new_tasks"].extend(entry.get("new_tasks", []))
        pi = entry.get("prev_incomplete", "")
        ei = entry.get("end_incomplete", "")
        if pi and pi != "NA":
            summary["prev_incomplete"].append(f"{date_str}: {pi}")
        if ei and ei != "NA":
            summary["end_incomplete"].append(f"{date_str}: {ei}")
    return summary

def print_summary(summary, label="DSR"):
    print(f"\n📅 {label} Summary ({summary['dates'][0]} to {summary['dates'][-1]})\n")
    print("✔️  Tasks Performed:")
    for task in summary["performed_tasks"]:
        print(f" - {task}")
    print("\n🆕 New Tasks Planned:")
    for task in summary["new_tasks"]:
        print(f" - {task}")
    print("\n⚠️ Previous Day Incomplete Tasks:")
    for item in summary["prev_incomplete"]:
        print(f" - {item}")
    print("\n🚧 End of Day Incomplete Tasks:")
    for item in summary["end_incomplete"]:
        print(f" - {item}")
