import sys
import os

# Add the project root directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime, timedelta
import calendar
from agents import planner, reminder_agent, dsr_sender_agent
from core.state import load_task_file
from core.env import get_config

def main():
    today = datetime.now()
    weekday = calendar.day_name[today.weekday()]
    config = get_config()

    print(f"📅 Running DSR agent for {today.strftime('%Y-%m-%d')} ({weekday})")

    # action = planner.plan_action(today)
    action = "send"  # 🚨 FOR TESTING ONLY — forces send
    if action == "skip":
        print("⏭️ Skipping (weekend, on leave, or already sent).")
    elif action == "remind":
        reminder_agent.run()
    elif action == "send":
        today_data = load_task_file(today)
        dsr_sender_agent.run(today, weekday, today_data)

if __name__ == "__main__":
    main()