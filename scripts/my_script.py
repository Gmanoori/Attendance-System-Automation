import os

# Access the environment variable
my_variable_value = os.environ.get("MY_VARIABLE")
login_time = os.environ.get("LOGIN_TIME")
logout_time = os.environ.get("LOGOUT_TIME")
user_name = os.environ.get("FULL_NAME")
final_date = os.environ.get("FINAL_DATE")


print(f"The login time is: {login_time}")
print(f"The first name is: {user_name}")
print(f"The login date is: {final_date}")
print(f"The logout time is: {logout_time}")


if my_variable_value:
    print(f"The variable from GitHub Actions is: {my_variable_value}")
    print(f"The login time is: {login_time}")
    print(f"The first name is: {user_name}")
    print(f"The login date is: {final_date}")
    print(f"The logout time is: {logout_time}")

else:
    print("MY_VARIABLE not found in environment.")