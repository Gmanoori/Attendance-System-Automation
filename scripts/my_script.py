import os
from datetime import datetime, timedelta

comment_body = os.environ.get("COMMENT_BODY", "")
user_login = os.environ.get("USER_LOGIN", "")
created_at = os.environ.get("CREATED_AT", "")
issue_number = os.environ.get("ISSUE_NUMBER", "")

IST_OFFSET = timedelta(hours=5, minutes=30)

# 1. Parse comment and timestamps
def convert_to_ist(iso_time_str):
    dt = datetime.strptime(iso_time_str, "%Y-%m-%dT%H:%M:%SZ")
    ist_dt = dt + IST_OFFSET
    return ist_dt.strftime("%H:%M"), ist_dt.strftime("%d-%m-%Y")

ist_time, final_date = convert_to_ist(created_at)

first_name = user_login.split("-")[0]

# 2. Command check
if '/login' in comment_body:
    # Save login to file
    with open("test/login_time.txt", "w") as f:
        f.write(f"{user_login}|{final_date}|{ist_time}")
    print(f"Good Morning {first_name}! :D Your login has been recorded at {ist_time}")
    print("Run: git commit and push here if you want")
elif '/logout' in comment_body:
    # Read existing login
    try:
        with open("test/login_time.txt", "r") as f:
            login_data = f.read().strip().split("|")
            login_user, login_date, login_time = login_data
        # Calculate work hours
        fmt = "%H:%M"
        login_dt = datetime.strptime(login_time, fmt)
        logout_dt = datetime.strptime(ist_time, fmt)
        diff = (logout_dt - login_dt)
        work_hours = f"{diff.seconds//3600:02d}:{(diff.seconds//60)%60:02d}"
        # Save attendance
        with open("test/attendance.md", "a") as f:
            f.write(f"| {user_login} | {final_date} | {login_time} | {ist_time} | {work_hours} |\n")
        os.remove("test/login_time.txt")
        print(f"See You Tomorrow, {first_name}! ;) Your logout has been recorded at {ist_time}. Work hours: {work_hours}")
        print("Run: git commit and push here if you want")
    except FileNotFoundError:
        print("Login file not found!")
else:
    print("No login/logout command detected.")
