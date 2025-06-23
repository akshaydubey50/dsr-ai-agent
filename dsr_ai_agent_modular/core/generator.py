from core.gpt_assistant import summarize_tasks
from core.env import get_config

def generate_dsr_email(date_obj, day_name, info, daily_data):
    start_time = daily_data.get("start_time", info["start_time"])
    leaving_time = daily_data.get("leaving_time", info["leaving_time"])
    performed_tasks = daily_data.get("performed_tasks", [])
    performed_summary = summarize_tasks(performed_tasks)

    def html_list(items):
        if not items or items == "NA":
            return "<li>NA</li>"
        return "".join(f"<li>{task}</li>" for task in items)

    # Email subject as header
    subject_heading = f"Status Report {date_obj.strftime('%d %B %Y')} {day_name}"

    html = f"""
    <html>
    <body style="font-family: Arial, sans-serif; font-size: 14px; color: #333;">
      <h2>{subject_heading}</h2>
      <table cellpadding="6" cellspacing="0" border="1" style="border-collapse: collapse; width: 100%;">
        <tr><th align="left" style="background:#f2f2f2;">NAME</th><td>{info['name']}</td></tr>
        <tr><th align="left" style="background:#f2f2f2;">DESIGNATION</th><td>{info['designation']}</td></tr>
        <tr><th align="left" style="background:#f2f2f2;">EMP CODE</th><td>{info['emp_code']}</td></tr>
        <tr><th align="left" style="background:#f2f2f2;">PROJECT NAME</th><td>{info['project_name']}</td></tr>
        <tr><th align="left" style="background:#f2f2f2;">CRM/PM/RM NAME</th><td>{info['crm_name']}</td></tr>
        <tr><th align="left" style="background:#f2f2f2;">PARALLEL REPORTING TO</th><td>{info.get('reporting_to', 'NA')}</td></tr>
        <tr><th align="left" style="background:#f2f2f2;">START TIME</th><td>{start_time}</td></tr>
        <tr><th align="left" style="background:#f2f2f2;">LEAVING TIME</th><td>{leaving_time}</td></tr>
      </table>

      <h3 style="margin-top:20px;">ACTIVITIES</h3>

      <p><strong>INCOMPLETE TASKS OF THE PREVIOUS DAY</strong></p>
      <ul>{html_list([daily_data.get('prev_incomplete', 'NA')])}</ul>

      <p><strong>NEW TASKS FOR THE DAY</strong></p>
      <ul>{html_list(daily_data.get('new_tasks', []))}</ul>

      <p><strong>ACTIVITIES PERFORMED</strong></p>
      <ul>{html_list(performed_summary.splitlines())}</ul>

      <p><strong>INCOMPLETE TASKS AT THE END OF DAY</strong></p>
      <ul>{html_list([daily_data.get('end_incomplete', 'NA')])}</ul>

    </body>
    </html>
    """
    return html
