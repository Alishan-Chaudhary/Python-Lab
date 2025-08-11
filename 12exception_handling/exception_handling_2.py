import datetime as dt

def user_age(dob):
    try:
         user_dob = dt.datetime.strptime(dob,"%Y-%m-%d").date()
    except ValueError:
         raise Exception("Enter DOB in 'YYYY-MM-DD' format.")

    todaydate = dt.date.today()
    if user_dob > todaydate:
         raise Exception("DOB can't be in future.")
    
    age = (todaydate - user_dob).days
    return age // 365

try:
     user = input("Enter the you dob=")
     print(user_age(user))
    
except Exception as e:
     print(e)