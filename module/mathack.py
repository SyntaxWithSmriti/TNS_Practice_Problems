# EXERCISE 10a - Your own module
# Topic: writing a module + if _name_ == "_main_"

# This file is a MODULE. Another file will import it.

# TASK
# ----
# 1. Complete the three functions below.
# 2. Add the _name_ guard at the bottom so the demo prints ONLY when you
#    run this file directly - not when main.py imports it.

# Then run BOTH of these in the terminal and compare the output:
#     python mathutils.py
#     python main.py


# PI = 3.14159

PI = 3.14

def per_rect (l,b):
    return (2*l) +(2*b)

def area_circle (r):
    return PI*r**2

print("mathack imported successfully !!")

if __name__ == "__main__":
    print (f"Testing : Perimeter of rectangle is : {per_rect(4,2)} ")
