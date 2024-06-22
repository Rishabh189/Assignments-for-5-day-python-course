# Roadmap Provider Project:

exp_level = input("Enter user's experience level: ").upper() # Taking input from user for experience level and converting it to upper case
if exp_level == "FRESHER": # Using equal to operator, assigning the interest in case of exp_level = Fresher
    user_int = input("Chose your career interest: 1- Web Dev 2- App Dev 3- DS,ML,AI: ")
    if user_int == '1': # Converting user interest variable to string in order to compare same data type
        print(F"Based on your selection 'Web Dev', you should learn HTML, CSS, JS, Python, Django")
    elif user_int == '2':
        print(F"Based on your selection 'App Dev', you should learn Java + DSA + Build Projects")
    elif user_int == '3':
        print(F"Based on your selection 'DS, ML,AI', you should learn Python, Maths, R")
    else:
        print("Please enter valid choice")
elif exp_level == "EXPERIENCED": # Using equal to operator, assigning the interest in case of exp_level = Experienced
    user_int = input("Chose your career interest: 1- Data Analytics 2- Cloud Computing 3- Front-End: ")
    if user_int == '1':
        print(F"Based on your selection 'Data Analytics', you should learn Python, Excel, Power BI")
    elif user_int == '2':
        print(F"Based on your selection 'Cloud Computing', you should learn DevOps and Python for Automation")
    elif user_int == '3':
        print(F"Based on your selection 'Front End', you should learn Python and Django for Backend")
    else:
        print("Please enter valid choice")
else:
    print("Please try again and chose between Fresher or Experienced") # Using else condition for handling wrong input