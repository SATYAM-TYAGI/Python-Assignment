#!/usr/bin/env python
# coding: utf-8

# In[1]:


while True:  # Start an infinite loop
    user_input = input("Enter a number (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':  # Check if the user wants to exit
        break  # Exit the loop

    try:
        number = float(user_input)  # Convert the input to a floating-point number

        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number or type 'exit' to quit.")

# The program ends when the loop is broken
print("Program terminated.")


# In[5]:


num1 = int(input("Enter the first value = "))
num2 = int(input("Enter the second value = "))

if num1 % 2==0 and num2 % 2==0:
  print("Both the number are even")
    
elif num1 % 2!=0 and num2 % 2!=0:
  print ("Both the numbers are odd ")

else:
    print("one number is odd and one number is even")


# In[6]:


# Prompt the user to enter an integer
num = int(input("Enter an integer: "))

# Define a dictionary to store the number bases and their respective formats
formats = {
    'Binary': 2,
    'Octal': 8,
    'Hexadecimal': 16
}

# Iterate over the dictionary to convert and print the number in each format
for base_name, base in formats.items():
    if base == 2:
        # Convert to binary using bitwise shift and mask
        binary = ""
        for i in range(num.bit_length() - 1, -1, -1):
            binary += str((num >> i) & 1)
        print(f"{base_name}: {binary}")
    elif base == 8:
        # Convert to octal using format function
        octal = format(num, 'o')
        print(f"{base_name}: {octal}")
    elif base == 16:
        # Convert to hexadecimal using format function
        hexadecimal = format(num, 'x').upper()
        print(f"{base_name}: {hexadecimal}")


# In[ ]:




