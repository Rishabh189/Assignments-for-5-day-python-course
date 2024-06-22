"""
user - india(current location), if not in india cab cannot be booked

 then airport,if not in airport cab cannot be booked

booked

"""

country = input("Enter your Country: ")
if country == "India":
    cur_loc = input("Enter your current location: ")
    if cur_loc == "Airport":
        print ("Cab booked")
    else:
        print("Cab not available near your location")
else:
    print("Cab not available near your location")   


