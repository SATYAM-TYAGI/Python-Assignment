#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Taking  user input for first and last name
first_name = input("Enter your first name: ").strip()  # Removes any leading/trailing whitespace
last_name = input("Enter your last name: ").strip()    # Removes any leading/trailing whitespace

# Reverse the order of the names and capitalize them
reversed_name = last_name.capitalize() + " " + first_name.capitalize()

# Print the reversed name
print("Your name in reverse order is:", reversed_name)


# In[2]:


# Taking input from the user
user_input = input("Enter a number: ")

# Converting the input to an integer
int_value = int(user_input)  # Integer: Whole number without a decimal point
print("Integer value:", int_value)

# Converting the input to a float
float_value = float(user_input)  # Float: Number with a decimal point
print("Float value:", float_value)

# Converting the input to a complex number
complex_value = complex(user_input)  # Complex: Number with a real and an imaginary part
print("Complex value:", complex_value)


# In[3]:


#  the user to enter the length of the rectangle
length = float(input("Enter the length of the rectangle: "))

#  the user to enter the width of the rectangle
width = float(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
area = length * width  # Area = length * width

# Display the result
print("The area of the rectangle is:", area)


# In[4]:


# the user to enter the length of the rectangle
length = float(input("Enter the length of the rectangle: "))

# the user to enter the width of the rectangle
width = float(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
area = length * width  # Area = length * width

# Display the result with two decimal places
print("The area of the rectangle is: {:.2f}".format(area))


# In[9]:


# the user enter the value of num1,num2,num3
num1=float(input("Enter the first value"))
num2=float(input("Enter the second value"))
num3=float(input("Enter the third value "))
# Calculate the average
average = (num1+num2+num3)/3
# printing the average
print("The average of the three numbers is:%2f" % average)


# In[ ]:




