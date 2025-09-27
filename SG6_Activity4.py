#Libraries for String Manipulation and Operations Activity #4

def name(name_format):
    
    name_split = name_format.split(",")
    
    if len(name_split) != 3:
        print("Invalid format")
        return
    else:
        return name_split
        

# --- Main Program ---

name_input = str(input("Enter your full name (First, Middle, Last):"))

name_split = name(name_input)

first_name = name_split[0].strip()
middle_name = name_split[1].strip()
last_name = name_split[2].strip()
last_name_split = last_name.split()
first_name_split = first_name.split()

if len(first_name_split) == 2:
    first_name_1 = first_name_split[0].strip()
    first_name_2 = first_name_split[1].strip()

    first_name_1 = first_name_1.capitalize()
    first_name_2 = first_name_2.capitalize()

    first_name = first_name_1 + " " + first_name_2
else:
    first_name = first_name.capitalize()
    
if len(last_name_split) == 2:
    last_name_1 = last_name_split[0].strip()
    last_name_2 = last_name_split[1].strip()

    last_name_1 = last_name_1.capitalize()
    last_name_2 = last_name_2.capitalize()

    last_name = last_name_1 + " " + last_name_2
else:
    last_name = last_name.capitalize()
    
mi = middle_name[0].capitalize()

name_format = f"{last_name}, {first_name} {mi}"

print(f"Formatted Name: {name_format}.")
