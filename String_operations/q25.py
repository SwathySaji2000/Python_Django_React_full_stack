
f_name = input("Enter your first name: ")

if len(f_name) < 5:

    s_name = input("Enter your sur name:")
     
    full_name = f_name+s_name

    print(full_name.upper())

else:

    print(f_name.lower())