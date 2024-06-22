# Certificate Eligibility Program Guide:

user_ip = input("Have you attended all classed without any gap? Chose: Yes/No ").upper() # Taking input from user if he/she attended all classes
if user_ip == 'YES':
# Using Nested if condition to check for all conditions to be eligible for certificate
    assi = input("Have you submitted all the assignments: Yes/No ").upper()
    if assi == 'YES':
        live_class = input("Have you attended all the live classes: Yes/No ").upper()
        if live_class == 'YES':
            cam = input("Have you switched on camera during live class: Yes/No ").upper()
            if cam == 'YES':
                print("Congrats, You are eligible for certificate")
            else:
                print("You are not eligible for certificate")
        else:
            print("You are not eligible for certificate")
    else:
        print("You are not eligible for certificate")
elif user_ip == 'NO':
    print("You are not eligible for certificate as there is a day gap, thank you")   
else:
    print("Please enter valid choice out of tow options: Yes/No") 

# As a suggestion, we can use while loop (till the while condition is true), that will allow multiple checks without restarting the program.
