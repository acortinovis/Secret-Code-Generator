# TASK: Write a function that shifts each letter in a string by a given number.



# Define a function that takes a string and an integer shift value as parameters  
def function(mes: str, shift: int):
# Create an empty list to store the shifted characters 
    shift_message=[]
# Loop through each character in the string:
    for char in mes:
        if char.isalpha(): #    If the character is a letter (A-Z or a-z):
            shift_car=chr(ord(char) + shift)#        Shift the letter by adding the shift value to its ASCII code (use the ord function)
                                            #        Convert the new ASCII code back to a character (use the chr function)
            
            shift_message.append(shift_car) #        Add the shifted character to the list
#    If the character is not a letter:
        else:
        #        Add the character unchanged to the list
            shift_message.append(char)
# After the loop, join the list into a string and return it  
    return ''.join(shift_message)
# Get user input for the message and shift value  

user=function(input("enter the message "),int(input("enter shift value ")))
# Call the function with the inputs and display the result
print (user)