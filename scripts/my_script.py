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
    print(f"Good Morning @{first_name}! 😊 Your login has been recorded at {ist_time}")
    # Set GitHub Actions outputs
    with open(os.environ.get('GITHUB_OUTPUT', ''), 'a') as f:
        f.write(f"first_name={first_name}\n")
        f.write(f"timestamp={ist_time}\n")
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
        diff = (logout_dt - login_dt - break_time) if 'break_time' in locals() else (logout_dt - login_dt)
        work_hours = f"{diff.seconds//3600:02d}:{(diff.seconds//60)%60:02d}"
        # Save attendance
        with open("test/attendance.md", "a") as f:
            f.write(f"| {user_login} | {final_date} | {login_time} | {ist_time} | {work_hours} |\n")
        os.remove("test/login_time.txt")
        print(f"See You Tomorrow, @{first_name}!😉 Your logout has been recorded at {ist_time}. Work hours: {work_hours}")
        # Set GitHub Actions outputs
        with open(os.environ.get('GITHUB_OUTPUT', ''), 'a') as f:
            f.write(f"first_name={first_name}\n")
            f.write(f"timestamp={ist_time}\n")
            f.write(f"work_hours={work_hours}\n")
    except FileNotFoundError:
        print("Login file not found!")
        # --- Handle break command ---
elif '/break' in comment_body:
    break_log_path = "test/break_log.txt"
    # Count previous breaks for this user and date
    break_count = 0
    last_start_time = None
    if os.path.exists(break_log_path):
        with open(break_log_path, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4 and parts[0] == user_login and parts[1] == final_date:
                    break_count += 1
                    if parts[3] == "start":
                        last_start_time = parts[2]

    # Odd count: start break, Even count: stop break
    if break_count % 2 == 0:
    # Start break
        with open(break_log_path, "a") as f:
            f.write(f"{user_login}|{final_date}|{ist_time}|start\n")
            print(f"Hello {first_name}, your break has started at {ist_time}. Enjoy your time off! :)")
    else:
    # Stop break
        with open(break_log_path, "a") as f:
            f.write(f"{user_login}|{final_date}|{ist_time}|stop\n")
    
    # Calculate break_time
    if last_start_time:
        fmt = "%H:%M"
        break_start = datetime.strptime(last_start_time, fmt)
        break_stop = datetime.strptime(ist_time, fmt)
        break_time = break_stop - break_start
        print(f"Welcome back {first_name}! Your break has ended at {ist_time}. Break duration: {break_time}.")
    else:
        print(f"Welcome back {first_name}! Your break has ended at {ist_time}.")
else:
    print("No login/logout command detected.")
