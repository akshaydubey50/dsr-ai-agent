
# 🤖 DSR AI Agent Workflow (Modular Architecture)

This project is an intelligent, modular AI agent that automates the process of sending **Daily Status Report (DSR)** emails. It includes **decision-making logic**, **email reminders**, and **Gmail API integration** to streamline daily reporting.

---


## ✅ All Scenarios Covered

| #  | Scenario                                             | Description                                                                 |
|----|------------------------------------------------------|-----------------------------------------------------------------------------|
| 1  | **Daily DSR Email Automation**                       | Sends DSR email based on daily JSON                                         |
| 2  | **Reminder at 9:30 PM**                              | If task file is missing or unchanged                                        |
| 3  | **Skip on Weekends**                                 | No reminder or DSR email on Saturday/Sunday                                 |
| 4  | **Skip if Already Sent**                             | Avoids duplicate emails using Gmail API query                               |
| 5  | **Auto Create Task Template at 9 AM**                | Starts your day with a blank JSON                                           |
| 6  | **Custom or Default Timings**                        | Reads from task file or falls back to `config.json`                         |
| 7  | **Leave Support (Inline & Global)**                  | `"leave": true` or listed in `leaves.json`                                  |
| 8  | **Weekly Summary Report**                            | Lists performed tasks from Mon–Fri                                          |
| 9  | **Monthly Summary Report**                           | Lists all performed tasks for the month                                     |
| 10 | **GPT-Powered Task Explanation**                     | 1-liner explanations per task in summaries                                  |
| 11 | **Intelligent Planning**                             | planner.py decides whether to remind, send, or skip                         |
| 12 | **Email Formatting with Subject and Body**           | Auto-generates DSR content with fixed header and dynamic body               |
| 13 | **M

## 🧠 What It Does

- ⏰ **Prepares** daily task templates
- 📋 **Reads** task files dynamically
- 🤔 **Decides** whether to send email, remind, or skip
- 📧 **Sends emails** through Gmail API
- 📆 **Skips weekends**
- 🔁 **Can be fully automated via cron**

---

## 📦 Folder Structure

```
dsr_ai_agent/
├── agents/
│   ├── planner.py            # Decides whether to remind, send, or skip
│   ├── reminder_agent.py     # Sends reminder if task data is missing or unchanged
│   ├── dsr_sender_agent.py   # Sends the actual DSR email
├── core/
│   ├── env.py                # Loads configuration from config.json
│   ├── email_client.py       # Handles Gmail authentication and sending
│   ├── generator.py          # Formats the DSR content
│   ├── state.py              # Checks task diffs and if email was already sent
├── data/
│   └── tasks/YYYY-MM-DD.json # Daily dynamic task input
├── workflows/
│   └── daily_schedule.py     # Agent orchestrator: runs planner and executes outcome
├── config.json               # Personal info (name, project, email, timings)
├── requirements.txt          # Python packages needed
```

---

## ⚙️ Setup Instructions

### 1. 📁 Unzip and Navigate

```bash
unzip dsr_ai_agent_modular.zip
cd dsr_ai_agent
```

### 2. 🐍 Create Environment and Install

```bash
python -m venv env
source env/bin/activate       # Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 3. 🔐 Setup Gmail API

- Go to [Google Cloud Console](https://console.developers.google.com/)
- Enable Gmail API
- Create OAuth 2.0 Desktop credentials
- Download `credentials.json` into the project root
- On first run, a browser will open for authorization
- It will auto-create `token.json` on success

---

## 📝 Task File Format (`data/tasks/YYYY-MM-DD.json`)

```json
{
  "prev_incomplete": "NA",
  "new_tasks": ["Update APIs", "Write unit tests"],
  "performed_tasks": ["Refactored polygon service"],
  "end_incomplete": "Pending QA",
  "start_time": "10:00 AM",        // optional
  "leaving_time": "07:00 PM"       // optional
}
```

Use `core/prepare_task_template.py` to create this file each day.

---

## 🤖 How the Agent Works

### `python workflows/daily_schedule.py`

- 📆 Skips Saturday & Sunday
- 📂 Loads today & yesterday’s task file
- 📤 If valid + new + not already sent → **Sends DSR email**
- 🔔 If file missing or unchanged → **Sends reminder**
- 💤 If already sent → **Skips**

---

## 🔁 Automation via Cron (Linux/macOS)

```cron
# 9:00 AM - create blank task file (optional)
0 9 * * 1-5 /path/to/python /your/path/core/prepare_task_template.py

# 9:30 PM - check and possibly send reminder
30 21 * * 1-5 /path/to/python /your/path/workflows/daily_schedule.py

# 11:00 PM - check and possibly send DSR
0 23 * * 1-5 /path/to/python /your/path/workflows/daily_schedule.py
```

---

## 📨 Email Output

- **Subject**: `Status Report DD Month YYYY Day`
- **To**: ``
- **Cc**: ``
- **From**: your authorized Gmail

---

## 💡 Extend Ideas

- 🧠 Integrate OpenAI (GPT) to auto-summarize task logs
- 📋 Pull work logs from Jira, GitHub, or Notion
- 🔔 Send reminders to Slack/Telegram
- 🧾 Log all sent emails in a local file or Notion database

---

## ✅ Final Notes

- You only need to maintain **1 task file per day**
- Agent takes care of when and what to do
- It’s built for **autonomy**, **modularity**, and **AI augmentation**

Happy automating! 🎯

TASK_EXPLANATIONS = {
    "Refactored polygon sync logic": "Improved data integrity in location-based delivery system.",
    "Integrated bundle pricing API": "Enabled dynamic pricing for bundled SKUs.",
    "Fixed checkout error on mobile": "Resolved crash issue affecting Android Chrome users.",
    "Added new unit tests for discounts": "Increased test coverage for promotional rules.",
    "Optimized order listing query": "Reduced response time for admin dashboard.",
    "Finalized UI for config editor": "Implemented new layout and validation on settings page."
}
