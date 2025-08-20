import os

# Access the environment variable
my_variable_value = os.environ.get("MY_VARIABLE")
login_time = os.environ.get("LOGIN_TIME")


if my_variable_value:
    print(f"The variable from GitHub Actions is: {my_variable_value}")
    print(f"{login_time}")
else:
    print("MY_VARIABLE not found in environment.")