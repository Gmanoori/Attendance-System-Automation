import os

# Access the environment variable
my_variable_value = os.environ.get("MY_VARIABLE")
login_time = os.environ.get("LOGIN_TIME")
first_name = os.environ.get("FIRST_NAME")
final_date = os.environ.get("FINAL_DATE")


print(f"The login time is: {login_time}")
print(f"The first name is: {first_name}")
print(f"The login date is: {final_date}")

if my_variable_value:
    print(f"The variable from GitHub Actions is: {my_variable_value}")
    print(f"The login time is: {login_time}")
    print(f"The first name is: {first_name}")
    print(f"The login date is: {final_date}")

else:
    print("MY_VARIABLE not found in environment.")