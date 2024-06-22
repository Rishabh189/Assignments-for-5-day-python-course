# Question 4: Single-line and Multi-line Comments
# Theory: Explain the purpose of comments in Python and differentiate between single-line and multi-line comments.
"""
Answer : 
Comments are used for excluding something from our code. Something written after comments will not be included while executing the code

Single line comment : # (only used for commenting single line)
Multi line comments : """ """ used for commenting multi-lines of program

"""

# Practical: Write a Python code snippet that includes both a single-line comment and a multi-line comment.

"""
taking input from user for length and converting it to float type
    and
taking input from user for length and converting it to float type
"""

len = float(input("Enter lenght of the rectangle: ")) 
wid = float(input("Enter width of the rectangle: ")) 
Area_of_Rec = len * wid
print ("The area of given rectangle= ", Area_of_Rec) # Displaying the area using print statement